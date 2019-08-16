
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki is challenging, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
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
Make sure the wiki is running, then do:
```
make test
```
This will run unit test and integration tests. Integration test use the wiki API and can take a while to run.
When tests are finished, you should see a test coverage report.

# Usage
If all tests passed, you now have a running wiki and a functioning environment for managing a semantic wiki using an ontology.
To bring it up again do `docker-compose up -d`. Check that the wiki started by opening `http://localhost`.

Do `docker ps` to get an overview of running containers.
You should see 4 containers:
* `ontology-import` contains the Python interpreter and libraries necessary for working with ontologies.make install
* `basic-wiki` provides the web server and PHP scripts for the wiki.
* `basic-db` provides the database engine. The data for your wiki installation is mounted on your file system in `mount/db`.
* `basic-data` contains installation data and is only used during installation.

To stop the wiki do: `docker-compose down`

# Example
The example shows how to create a wikis forms, templates, categories and properties by importing an ontology in to the wiki.
The example ontology is "Friend of a Friend" (FOAF), a well-known ontology for describing social networks (Brickley, Miller, 2015).
FOAF is provided here in RDF/XML format: `example/foaf.rdf`. You can get an overview of FOAF using an ontology visualizer, like [VOWL](http://www.visualdataweb.de/webvowl/).

To load FOAF into the wiki, make sure the wiki is running,
```
docker-compose up -d
```
then do:
```
cp example/foaf.rdf mount/rdf/ # copy the ontology into the mount point, so that it is accessible from the container
docker exec -ti ontology-import bash # open a terminal into the container
python /src/rdf2mw.py -i /rdf/foaf.rdf # import FOAF into the wiki
```

# Contributing
If you wish to contribute to the software or need support, please [contact the maintainer](mailto:alvaro,ortiztroncoso@mfn.berlin).
Please report problems using the [issue tracker](https://gitlab.com/alvarosaurus/RDF-to-SemanticWiki/issues).

# References
Brickley, D. and Miller, L., 2015. FOAF Vocabulary Specification 0.99 (2014). Namespace Document. Available online: http://xmlns.com/foaf/spec/ (accessed on 5 August 2019).

