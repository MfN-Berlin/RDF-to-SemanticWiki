# Provides an ontology import service.
# Usage: configure, make, make install (see README.md)
# Edit confguration in the file config.ini

.DEFAULT_GOAL := build
.PHONY: test

# Read config file
include config.ini

build:rm
# delete old image
	-docker rmi rdf-to-semanticwiki_ontology
# make volumes directories on the host, copy configuration
	-mkdir ${MOUNT}
	cp config.ini ${MOUNT}
# build and start the container
	export MOUNT=${MOUNT} && \
	export ONTOLOGY_CONTAINER_NAME=${ONTOLOGY_CONTAINER_NAME} && \
	docker-compose -f docker-compose.yml up &

test:
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c " \
	cd /test && ./test.sh"	

rm:
	-docker stop ${ONTOLOGY_CONTAINER_NAME}
	-docker rm ${ONTOLOGY_CONTAINER_NAME}
