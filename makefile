# Provides an ontology import service.
# Usage: configure, make, make install (see README.md)
# Edit confguration in the file config.ini

.DEFAULT_GOAL := build
.PHONY: test

# Path to the mount on the host, where persistent files will be stored
MOUNT=./mount
# Name of the Docker container with the ontology import script (RDF-to_SemanticWiki)
ONTOLOGY_CONTAINER_NAME=ontology-import

build:rm
# delete old image
	-docker rmi rdf-to-semanticwiki_ontology
# make volumes directories on the host, copy configuration
	-mkdir ${MOUNT}
	-mkdir ${MOUNT}/rdf
	cp config.ini ${MOUNT}/rdf
# build and start the container
	export MOUNT=${MOUNT} && \
	export ONTOLOGY_CONTAINER_NAME=${ONTOLOGY_CONTAINER_NAME} && \
	docker-compose -f docker-compose.yml up &

up:
	export MOUNT=${MOUNT} && \
	export ONTOLOGY_CONTAINER_NAME=${ONTOLOGY_CONTAINER_NAME} && \
	docker-compose -f docker-compose.yml up &

test:up
	docker exec -ti ${ONTOLOGY_CONTAINER_NAME} script -q -c " \
	cd /test && ./test.sh"	

rm:
	-docker stop ${ONTOLOGY_CONTAINER_NAME}
	-docker rm ${ONTOLOGY_CONTAINER_NAME}
