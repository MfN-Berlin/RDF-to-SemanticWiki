# Provides an ontology import service.
# Usage: configure, make, make install (see README.md)
# Edit confguration in the file config.ini

.DEFAULT_GOAL := build
.PHONY: test

# Path to the mount on the host, where persistent files will be stored
MOUNT=./mount
# Name of the Docker container with the ontology import script (RDF-to_SemanticWiki)
ONTOLOGY_CONTAINER_NAME=ontology-import

### TESTS ###
INSTALLDBPASS=secret123
# Name of the Docker container with the wiki and the webserver
TEST_SMW_CONTAINER_NAME=basic-wiki
# Name of the Docker container with the database engine
TEST_DB_CONTAINER_NAME=basic-db
# Name of the Docker container with the data for restoring the wiki
TEST_DATA_CONTAINER_NAME=basic-data
# The DB user to use for this script.
# This value appears in LocalSettings.php for $wgDBuser.
# If --installdbuser and --installdbpass are given,
# this value will be used to create a new account
TEST_DBUSER=root
# The password to use for this script.
# This value appears in LocalSettings.php for $wgDBpassword.
# If --installdbuser and --installdbpass are given,
# this value will be used to create a new account
TEST_DBPASS=secret123
# The database name
TEST_DBNAME=basic_wiki

# Run test with coverage.
# See https://stackoverflow.com/questions/36517137/how-to-properly-use-coverage-py-in-python#36524004
test:
# update tests, in case they have changed
	cp -r test ${MOUNT}
# cleanup old coverage report
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "rm test/.coverage"
# run unit tests
	echo "Running unit tests..."
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "cd /test && export PYTHONPATH=${PYTHONPATH}:../src:./unit && py.test unit/*.py --cov=../src --cov-report="
# run integration tests
	echo "Running integration tests..."
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "cd /test && export PYTHONPATH=${PYTHONPATH}:../src:./integration && py.test integration/*.py --cov=../src --cov-report="
# show test coverage report
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "cd /test && coverage report -m"

install:
# re-create the database in the test container
	docker exec -ti ${TEST_DB_CONTAINER_NAME} script -q -c "echo \"drop database if exists ${TEST_DBNAME};\" > /tmp/query.sql"
	docker exec -ti ${TEST_DB_CONTAINER_NAME} script -q -c "mysql -u${TEST_DBUSER} -p${TEST_DBPASS} ${TEST_DBNAME} < /tmp/query.sql"
	docker exec -ti ${TEST_DB_CONTAINER_NAME} script -q -c "mysqladmin -u${TEST_DBUSER} -p${TEST_DBPASS} create ${TEST_DBNAME}"
# import database dump
	docker cp ${TEST_DATA_CONTAINER_NAME}:/dump.sql /tmp/
	docker cp /tmp/dump.sql ${TEST_DB_CONTAINER_NAME}:/tmp
	docker exec -ti ${TEST_DB_CONTAINER_NAME} script -q -c "mysql -u${TEST_DBUSER} -p${TEST_DBPASS} ${TEST_DBNAME} < /tmp/dump.sql"
	echo "You can try out the wiki at http://localhost"


# Stop and remove test data and containers
rm_test_data:
	docker-compose down
	-docker rm ${TEST_SMW_CONTAINER_NAME}
	-docker rm ${TEST_DB_CONTAINER_NAME}
	-docker rm ${TEST_DATA_CONTAINER_NAME}
	-docker rm ${ONTOLOGY_CONTAINER_NAME}

# import an ontology into the wiki
import:
# copy configuration, templates and ontology to mount, start importer
# 'ontology' and 'templates' are passed from the command-line as 'make ontology=xxx.owl templates=src/smw/templates import'
	-sudo mkdir -p ${MOUNT}/rdf
	sudo cp config.ini ${MOUNT}/rdf/
	sudo cp $(ontology) ${MOUNT}/rdf/ontology.owl
	sudo cp -r $(templates) ${MOUNT}/rdf/
# load the ontology into the wiki
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "\
	export PYTHONPATH=.:/src && \
	python src/rdf2mw.py -a import -i /ontology.owl -l en -t /templates/"

# remove the current ontology from the wiki
remove:
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "\
	export PYTHONPATH=.:/src && \
	python src/rdf2mw.py -a remove -i /ontology.owl"

###################################
#       Commands
###################################

define up
	$(export_env) && \
	docker-compose -f docker-compose.yml up -d
endef

define down
	$(export_env) && \
	docker-compose down
endef

define export_env
	export ONTOLOGY_CONTAINER_NAME=${ONTOLOGY_CONTAINER_NAME} && \
	export INSTALLDBPASS=${INSTALLDBPASS} && \
	export MOUNT=${MOUNT}
endef
