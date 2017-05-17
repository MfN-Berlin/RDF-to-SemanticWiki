
# mwOWLBridge
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of templates, properties and forms.
A solution is to model the semantic relationships as an ontology, using a modeling tool such as Protege, and then importing the ontology into the wiki.
By separating the model from its implementation, it becomes easier to keep an overview of the entities and properties used.
Additionally, ontologies can be visualized using VOWL, and discussed with less technical stakeholders.

## Dependencies
Depends on python3 >= 3.4.2; additional modules: requests >= 2.4.3, configparser >= 3.5.0, urllib3 >= 1.9.1

MediaWiki, SemanticMediaWiki.

## Installation
Make sure your Wiki is up and running, and tht the Semantic MediaWiki extension is installed.

Copy the file mwOWLBridge/example/example.ini to mwOWLBridge/example/config.ini
Edit config.ini to suit your configuration.


## OWL2mw
__Import an ontology into a semantic MediaWiki.__

The provided example ontology is very simple. It can be automatically imported into a semantic MediaWiki using the scripts provided. 
The semantic Mediawiki templates, properties and forms created can be used to test the viability of the concept.

### Usage example
An example ontology is included in the folder "example". This ontology, Calendar.owl, models an event calendar, such as from thunderbird etc. 

A graphical representation is provided in Calendar.svg. You can view the svg file using an SVG viewer.The graphical representation was made using VOWL (http://vowl.visualdataweb.org/webvowl.html).

To edit the example ontology, use an ontology editor such as Protege (http://webprotege.stanford.edu) to edit the Calendar.owl file.

The provided example ontology can be imported into a semantic MediaWiki following these steps.


The semantic Mediawiki templates, properties and forms created can be used to test the viability of the concept.
