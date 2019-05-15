# Provides an ontology import service.
# Usage: configure, make, make install (see README.md)
# Edit confguration in the file config.ini

.DEFAULT_GOAL := build
.PHONY: test

# Path to the mount on the host, where persistent files will be stored
MOUNT=./mount
# Name of the Docker container with the ontology import script (RDF-to_SemanticWiki)
ONTOLOGY_CONTAINER_NAME=ontology-import
SMW_CONTAINER_NAME=smw-wiki
DB_CONTAINER_NAME=smw-db
INSTALLDBPASS=secret123

build:
	$(down)
	$(remove)
# delete old image
	-docker rmi rdf-to-semanticwiki_ontology
# make volumes directories on the host, copy configuration
	-sudo mkdir -p ${MOUNT}/rdf
	-sudo rm -rf ${MOUNT}/rdf/config.ini
	-sudo cp config.ini ${MOUNT}/rdf
# build and start the container
	$(up)

start:
# start the container
	$(up)

stop:
	$(down)

test:install
# build the ontology-importer
	${export_env} && \
	docker-compose -f docker-compose-test.yml up -d

# connect the ontology importer to the wiki
	docker network connect basic-wiki_default ${ONTOLOGY_CONTAINER_NAME}

# run tests
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c " \
	cd /test && ./test.sh"

	docker network disconnect basic-wiki_default ontology-import

# stop and remove all containers
	$(remove)
# delete the test data
	sudo rm -rf mount

install:
# build and install a basic wiki
	-mkdir -p ${MOUNT}/basic-wiki
	cp test/basic-wiki.ini test/basic-wiki/config.ini
	$(MAKE) -C test/basic-wiki/ build	
	echo wait for the database container to start
	sleep 30
	$(MAKE) -C test/basic-wiki/ install

import:
	$(down)
	$(remove)
# copy configuration, templates and ontology to mount, start importer
# 'ontology' and 'templates' are passed from the command-line as 'make ontology=xxx.owl templates=src/smw/templates import'
	-sudo mkdir -p ${MOUNT}/rdf
	-sudo rm -rf ${MOUNT}/rdf/config.ini
	sudo cp config.ini ${MOUNT}/rdf/
	sudo cp $(ontology) ${MOUNT}/rdf/ontology.owl
	sudo cp -r $(templates) ${MOUNT}/rdf/
	$(up)
# load the ontology into the wiki
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c "\
	export PYTHONPATH=.:/src && \
	python src/rdf2mw.py -a import -i /ontology.owl -l en -t /templates/"

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
	export SMW_CONTAINER_NAME=${SMW_CONTAINER_NAME} && \
	export DB_CONTAINER_NAME=${DB_CONTAINER_NAME} && \
	export ONTOLOGY_CONTAINER_NAME=${ONTOLOGY_CONTAINER_NAME} && \
	export INSTALLDBPASS=${INSTALLDBPASS} && \
	export MOUNT=${MOUNT}
endef

define remove
	-docker stop ${SMW_CONTAINER_NAME}
	-docker stop ${ONTOLOGY_CONTAINER_NAME}
	-docker stop ${DB_CONTAINER_NAME}
	-docker rm ${SMW_CONTAINER_NAME}
	-docker rm ${DB_CONTAINER_NAME}
	-docker rm ${ONTOLOGY_CONTAINER_NAME}
endef
