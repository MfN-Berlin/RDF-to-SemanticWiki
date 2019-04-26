
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of categories, templates, forms and property pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

The second step is to convert the ontology into categories, templates, forms and property pages in the wiki. This script takes an ontology file in RDF/XML format as input and creates the necessary wiki pages using the MediaWiki API.

# Installation
## Cloning with submodules
This project uses submodules. To clone with submodules, see: https://git-scm.com/book/en/v2/Git-Tools-Submodules

Basically, if you have not cloned already, do:
```
git clone --recurse-submodules git@gitlab.com:alvarosaurus/RDF-to-SemanticWiki.git
```

Use `configure`, `make` to setup the container.

Create the wiki configuration
```
./configure
```
You can edit the file `config.ini` for additional settings.

Build the docker images, create volumes on the host, copy configuration, start
```
make
```

Run the tests
```
make test
```



