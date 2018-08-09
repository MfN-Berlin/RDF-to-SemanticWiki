
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of templates, forms and attribute pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

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
This is a work in progress. See [here](https://gitlab.com/alvarosaurus/RDF-to-SemanticWiki/wikis/home) for usage.

