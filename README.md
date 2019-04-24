
# RDF-to-MediaWiki
Maintaining a semantic MediaWiki can be a lot of work, as any reasonably complex semantic wiki will require dozens of templates, forms and attribute pages.
By separating the model from its implementation, it becomes easier to keep an overview of the semantic components used.

The first step to do this is to model the semantic relationships as an ontology, using a modelling tool such as Protege.

The second step is to convert the ontology into templates, forms and attributes pages in the wiki. This script takes an ontology file in RDF format as input and creates the necessary wiki pages using the MediaWiki API.

# Installation
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



