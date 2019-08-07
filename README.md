
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

The second step is to convert the ontology into categories, templates, forms and property pages in the wiki. This script takes an ontology file in RDF/XML format as input and creates the necessary wiki pages using the MediaWiki API.

# Install using Docker
A wiki is provided as a Docker container for running the tests. You will need to install Docker on your machine to run it. Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/), then do:
```
docker-compose up -d
make install
```
This will install a basic semantic MediaWiki in 3 Docker containers. You try out the wiki by opening `http://localhost`.

## Testing
Make sure the wiki is running, the do:
```
make test
```
This will run unit test and integratin tests. Integration test use the wiki API and can take a while to run.
When test are finished, you should see a test coverage report.

## Usage
If all tests passed, you now have a running wiki and a functioning environment for managing a semantic wiki using an ontology.
To bring it up again do `docker-compose up -d`. Check that the wiki started by opening `http://localhost`.
Do `docker ps` to get an overview of running containers.
You should see 4 containers:
* `ontology-import` contains the Python interpreter and libraries necessary for working with ontologies.make install
* `basic-wiki` provides the web server and PHP scripts for the wiki.
* `basic-db` provides the database engine. The data for your wiki installation is mounted on your file system in `mount/db`.
* `basic-data` contains installation data and is only used during installation.

To stop the wiki do: `docker-compose down`

## Example
The example shows how to create a wikis forms, templates, categories and properties by importing an ontology in to the wiki.
The example ontology is "Friend of a Friend" (FOAF), a well-known ontology for describing social networks (Brickley, Miller, 2015).
FOAF is provided here in RDF/XML format: `example/foaf.rdf`. You can get an overview of FOAF using an ontology visualizer, like [VOWL](http://www.visualdataweb.de/webvowl/).

To load FOAF into the wiki, do:
```
cp example/foaf.rdf mount/rdf/ # copy the ontology into the mount point, so that it is accessible from the container
docker exec -ti ontology-import bash # open a terminal into the container
python /src/rdf2mw.py -i /rdf/foaf.rdf # import FOAF into the wiki
```

# References
Brickley, D. and Miller, L., 2015. FOAF Vocabulary Specification 0.99 (2014). Namespace Document. Available online: http://xmlns.com/foaf/spec/ (accessed on 5 August 2019).

#############################################
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
