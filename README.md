
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

The second step is to convert the ontology into categories, templates, forms and property pages in the wiki. This script takes an ontology file in RDF/XML format as input and creates the necessary wiki pages using the MediaWiki API.

# Installation
## Get Docker
This script is provided as a Docker container. You will need to install Docker on your machine to run it. Get Docker at: https://www.docker.com/get-started

## Cloning with submodules
This project uses submodules. To clone with submodules, see: https://git-scm.com/book/en/v2/Git-Tools-Submodules

Basically, if you have not cloned already, do:
```
git clone --recurse-submodules git@gitlab.com:alvarosaurus/RDF-to-SemanticWiki.git
```

## Test using the example ontology and the example wiki.
Build the docker images and containers, start a test wiki, load the example ontology, run the unit tests
```
make test
```

# Usage
If the test pass succesfully, then `docker ps` should show a Docker container for the importer ("ontology-import"), as well as a wiki and a database ("smw-wiki" and "smw-db").
You can now import an ontology into a wiki. In the following example, I will use the basic wiki installed during testing.

1. Open http://localhost to make sure the basic wiki is running.
2. Create the configuration for the ontology importer by running ```./configure```. Accept the defaults.

Build the docker images, create volumes on the host, copy configuration, start
```
make
```

Run the tests
```
make test
```



