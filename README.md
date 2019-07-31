
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

The second step is to convert the ontology into categories, templates, forms and property pages in the wiki. This script takes an ontology file in RDF/XML format as input and creates the necessary wiki pages using the MediaWiki API.

# Installation
A wiki is provided as a Docker container for running the tests. You will need to install Docker on your machine to run it. Install [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/), then do:

# Testing
Start the test wiki and run the tests
```
docker-compose up -d
make test
```


# OLD
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

## Install the wiki
If the tests pass successfully, you can install the wiki by calling
```
make install
```
This will create a directory `mount/basic-wiki` on the host, to persist the wiki settings and database.

# Basic usage
You can now import an ontology into a wiki. In the following example, I will use the basic wiki installed during testing.

1. Create the configuration for the ontology importer by running ```./configure```. Accept the defaults.
2. Open `http://localhost` to make sure the basic wiki is running.
3. Call the ontology import script, import the example ontology provided, using the default templates:
```
sudo make ontology=example/Calendar.rdf templates=src/smw/templates import
```

1. Open the page `http://localhost/html/Special:Categories`, you should see 2 categories: `Entry`and `Location`.
These correspond to the classes in the example ontology provided in example/Calendar.rdf.
2. Click on `Location`, create a new Location called `The Met`.

# Advanced usage
## Removing an ontology
This will remove all forms, templates, attributes and categories corresponding to the last imported ontology
```
sudo make remove
```
