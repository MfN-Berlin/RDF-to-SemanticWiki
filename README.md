
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of templates, forms and attribute pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege. Alternatively, simple ontologies can modelled visually using UML and then converted into RDF (see https://github.com/AlvaroOrtizTroncoso/UML-ODM-to-OWL-XML).

The second step is to convert the ontology into templates, forms and attributes pages in the wiki. This script takes an ontology file in RDF format as input and creates the necessary wiki pages using the MediaWiki API.

## Prerequisites
* Python 3
* To install the necessary Python packages, do: `pip3 install -r requirements.txt`
* [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), [SemanticMediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki).
* Additional MediaWiki extensions:
[Page Forms](https://www.semantic-mediawiki.org/wiki/Extension:Page_Forms),
[User Functions](https://www.mediawiki.org/wiki/Extension:UserFunctions),
[Header Tabs](https://www.mediawiki.org/wiki/Extension:Header_Tabs),
[Parser Functions](https://www.mediawiki.org/wiki/Extension:ParserFunctions)

## Usage
This is a work in progress. See https://github.com/AlvaroOrtizTroncoso/RDF-to-MediaWiki/wiki for usage.

## Tests
To run the tests, I recommend you install "green" and "coverage", which should be installed if you did `pip3 install -r requirements.txt`.

To run the tests and get code coverage:

```
cd test
bash test.sh
```

### Example
An example ontology is included in the folder "example". This ontology, Calendar.rdf, models an event calendar, such as from thunderbird etc.

A graphical representation is provided in Calendar.svg. You can view the svg file using an SVG viewer.The graphical representation was made using VOWL (http://vowl.visualdataweb.org/webvowl.html).

To edit the example ontology, use an ontology editor such as Protege (http://webprotege.stanford.edu) to edit the Calendar.rdf file.

The provided example ontology can be imported into a semantic MediaWiki following these steps.


The semantic Mediawiki templates, properties and forms created can be used to test the viability of the concept.

## Developer documentation
The directory docs contains UML diagrams. These can be opened using [ArgoUML](http://argouml.tigris.org).