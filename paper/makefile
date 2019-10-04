default: article

# the name of the article file (without extension)
ARTICLE = paper

# Name of the container with Latex
LTX_CONTAINER=pdflatex

# Mount point of the project files on the docker container
MOUNT=/files

# Create the article and
# copy the article to the root folder of the project
# the project files are mounted on /files in the container (see docker-compose.yml)
article:clean prepare
	${up}
	docker exec -ti ${LTX_CONTAINER} script -q -c " \
	cd ${MOUNT}/temp && \
	pdflatex $(ARTICLE).tex && \
	pdflatex $(ARTICLE) && \
	pdflatex $(ARTICLE).tex"
	mv -f ./temp/$(ARTICLE).pdf .
	echo created $(ARTICLE).pdf

# cleanup output and temp files
clean:
	rm -f $(ARTICLE).pdf; \
	rm -fr paper/temp/*

# copy all files required by latex to the temp dir
prepare:
	-mkdir -p temp && \
	cp -r ./templates/* temp && \
	cp *.tex *.bib temp

###################################
#       Commands
###################################

# call docker-compose up,
# with required environment variables
define up
	export LTX_CONTAINER=${LTX_CONTAINER} && \
	export MOUNT=${MOUNT} && \
	docker-compose up -d
endef
