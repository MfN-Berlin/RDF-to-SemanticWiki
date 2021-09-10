# RDF-to-SemanticWiki
Maintaining a semantic MediaWiki is challenging, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
This script takes an ontology file in RDF/XML format as input and creates the necessary wiki pages using the MediaWiki API.

# Install using Docker

**Install Docker on Linux:**
A wiki is provided as a Docker container for running the tests. You will need to install Docker on your machine to run it. Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

**Install Docker on Windows:**
The recommended way to install Docker on Windows is to install a Linux virtual machine using Oracle Virtual Box (https://www.virtualbox.org/) and then to proceed as above. For the Linux virtual machine, you might want to choose a command-line oriented or a server version of some distribution, such as Debian (https://www.debian.org/distrib/index.en.html).

Clone the repository, then start the containers:
```
git clone git@gitlab.com:alvarosaurus/RDF-to-SemanticWiki.git
cd RDF-to-SemanticWiki
```
You now need to create a configuration file. For testing, accept the defaults given by the configure script:
```
docker-compose up -d
./configure
```
This will install RDF-to-MediaWiki along with a basic semantic MediaWiki for testing:
```
make install
```
Do `docker ps` to get an overview of running containers.
You should see 4 containers:
* `ontology-import` contains the Python interpreter and libraries necessary for working with ontologies.
* `basic-wiki` provides the web server and PHP libraries for the wiki.
* `basic-db` provides the database engine. The data for your wiki installation is mounted on your file system in `mount/db`.
* `basic-data` contains installation data and is only used during installation.

Try out the wiki by opening `http://localhost` in a browser.

## Testing
Make sure the wiki is running, then do:
```
make test
```
This will run unit test and integration tests. Integration test use the wiki API and can take a while to run.
When tests are finished, you should see a test coverage report.

If all tests passed, you now have a running wiki and a functioning environment for managing a semantic wiki using an ontology.
Check that the wiki started by opening `http://localhost`. If necessary, bring it up again by calling `docker-compose up -d`.

# Example
The example shows how to create wiki forms, templates, categories and properties by importing an ontology in to the wiki. Then some data is created using these forms and the data is retrieved using semantic queries.

## Importing the example ontology
The example ontology is "Friend of a Friend" (FOAF), a well-known ontology for describing social networks (Brickley, Miller, 2015).
FOAF is provided here in RDF/XML format: `example/foaf.rdf`. You can get an overview of FOAF using an ontology visualizer, like [VOWL](http://vowl.visualdataweb.org/webvowl.html#installation).

To load FOAF into the wiki, make sure the wiki is running, then do:
```
./rdf2smw --input /rdf/foaf.rdf
```

Once the example ontology has been imported, open the wiki in a browser `http://localhost`. You should now see an additional section on the sidebar menu containing all the classes in the FOAF ontology (if you don't, try reloading the page).

## Creating some example content
The example ontology, Friend-of-a-Friend (FOAF) can be used to model social networks. This example shows how to model a simple human network.
1. Open `http://localhost` and login using the defaul credentials stored in config.ini: "Sysop", "secret123"
2. Find the "Ontology" menu on the left hand-side of the page
3. Click on "Person", type-in "Alice", ignore the rest of the form, scroll to the bottom, save the page.
4. Repeat with "Bob", "Caroline" and "David".
5. Click on "Person", you should see 4 entries. Open "Alice", klick on "Edit with form" (upper right). If you can't see the "Edit with form" Button, try the "More->Refresh" menu item.
6. Scroll down to the input field "knows", click one or more persons Alice knows (it doesn't matter which ones), "Save".
7. Repeat for "Bob", "Caroline" and "David".

## Retreiving data using semantic queries
Now that you have some example content, you can leverage the capabilities of Semantic MediaWiki to access your data.

Login ("Sysop"/"secret123"), open your user page, "User:Sysop" (upper right corner), create it. 
Type this query and save the page
```
==Who knows who?==
{{#ask: [[Category:Person]]
|mainlabel=who
|?knows
}}
```
You can now see an tabular overview of the simple social network you just recorded.

You can also query for specific values, e.g. to get a list of Bob's friends:
```
==Who knows Bob?==
{{#ask: [[Category:Person]][[knows::~Bob]]}} are friends of Bob.
```
You can also export your data in a format suitable for further processing. This code will add a download link. Click on it to open the data in a spreadsheet or to import the data in a visualization tool (e.g. [Palladio](http://hdlab.stanford.edu/palladio-app/#/visualization))
```
==Export==
{{#ask: [[Category:Person]]
|mainlabel=who
|?knows
|format=csv
|sep=;
}}
```
There are many more possibilities for querying data, plese see the Semantic mediawiki documentation on [inline queries](https://www.semantic-mediawiki.org/wiki/Help:Inline_queries) and [result formats](https://www.semantic-mediawiki.org/wiki/Help:Result_formats).

## Importing other ontologies

This software was created to import the [IKON ontology](https://via.naturkundemuseum.berlin/ontologies/ikon.rdf) for documenting scientific research activities. If you wish to import this or other ontologies, then place the ontology in the /rdf folder and import using the import command, i.e. 

```
./rdf2smw --input /rdf/ikon.rdf
```

__Note that the path to the rdf file is as seen from within the Docker container, so should start with `/rdf`.__

Please see the project's documentation on Gitlab for information on [advanced usage](https://gitlab.com/alvarosaurus/RDF-to-SemanticWiki/wikis/).

# Contributing
If you wish to contribute to the software or need support, please [contact the maintainer](mailto:alvaro.ortiztroncoso@mfn.berlin).
Please report problems using the [issue tracker](https://gitlab.com/alvarosaurus/RDF-to-SemanticWiki/issues).

# References
Brickley, D. and Miller, L., 2015. FOAF Vocabulary Specification 0.99 (2014). Namespace Document. Available online: http://xmlns.com/foaf/spec/ (accessed on 5 August 2019).

