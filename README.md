# mwImportOWL
Import an ontology into a semantic MediaWiki

Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of templates, properties and forms.
A solution is to model the semantic relationships as an ontology, using a modeling tool such as Protege, and then importing the ontology into the wiki.
By separating the model from its implementation, it becomes easier to keep an overview of the entities and properties used. 
Additionally, ontologies can be visualized using VOWL, and discussed with less technical stakeholders. 

This project is a proof-of-concept. The provided example ontology is very simple. It can be automatically imported into a semantic MediaWiki using the scripts provided. 
The semantic Mediawiki templates, properties and forms created can be used to test the viability of the concept.

## Usage example
An example ontology is included in the folder "example". This ontology, Calendar.owl, models an event calendar, such as from thunderbird etc. 

1. A graphical representation is provided in Calendar.svg. You can view the svg file using any svg viewer. 
The graphical representation was made using VOWL (http://vowl.visualdataweb.org/webvowl.html)
2. To edit the example, use an ontology editor, such as Protege (webprotege.stanford.edu) to edit the Calendar.owl file
3. When you're done, import the ontology into MediaWiki (in progress)
