---
title: 'Creating ontology-based semantic wikis at the natural history museum'
tags:
  - semantic web
  - ontology engineering
  - collaborative authoring
authors:
 - name: Alvaro Ortiz-Troncoso
   orcid: 0000-0001-7620-1907
   affiliation: 1
affiliations:
 - name: Museum für Naturkunde Berlin
   index: 1
date: 12 September 2019
bibliography: paper.bib
---

# Pitch
## Idea
Semantic wikis have been supporting research at the Museum für Naturkunde Berlin (Museum of Natural History Berlin) in multiple ways since 2015, and the experience gained demonstrates that creating and maintaining a semantic wiki is challenging, and requires a methodical approach.

## Pitch title
Creating ontology-based semantic wikis at the Museum of Natural History Berlin

## Key Points
* Semantic wikis support research at the natural history museum by providing services for developing and documenting collection management and imaging procedures or annotating archive material. On the other hand, some wikis are available on the Web, as publication medium for conference presentations or providing additional material for exhibitions. A total of 15 semantic wikis are currently online on the museum's servers.
* Semantic wikis combine the metadata and conformance aspects required by knowledge management, with the possibility to access and build-upon a corpus of collaboratively collected knowledge. On the down side, maintaining a semantic wiki is challenging.
* Coping with increasing complexity of the wikis led to the development of a methodical approach for simplifying the creation and maintenance of semantic wikis: modelling the semantic relationships underlying the information in the wiki as an ontology, and then automatically creating the wiki from the ontology constructs.
* Benefits gained: a methodical approach for creating and maintaining wikis greatly simplifies these tasks, so ensures that wikis will continue to be supported at the Museum of Natural History Berlin. Reusing vocabularies and taxonomies throught several projects becomes much more manageable.

## Type & Section
Analytic commentary, Learning About CS Disciplines


# Creating ontology-based semantic wikis at the Museum of Natural History Berlin

## Introduction
Wikis are web platforms allowing for collaborative authoring of information. With certainty, the best known wiki is Wikipedia, but wikis are also being used to setup corporate intranets, private collaboration environments or knowledge bases. A semantic wiki is a wiki whose functionality has been extended to encode information in a structured and machine-readable way: information encoded semantically forms a "consistent logical web of data" [@berners1998semantic], that can be used for enriching information with metadata, checking the conformance of information against an agreed upon schema, or accessing and combining data from different sources [@oren2006semantic]. Semantic wikis therefore combine the metadata and conformance aspects required by knowledge management, with the possibility to access and build-upon a corpus of collaboratively collected knowledge. 

Semantic wikis have been used at the Museum für Naturkunde Berlin (Museum of Natural History Berlin) since 2015. A total of 15 semantic wikis are currently online on the museum's server. Most of these wikis are part of the museum's intranet, and support research by providing services for developing and documenting collection management and imaging procedures or annotating archive material. On the other hand, some wikis are available on the Web, as publication medium for conference presentations or providing additional material for exhibitions. An example of a publicly accessible semantic wiki running at the Museum of Natural History Berlin is the [Wiki supplementing the Panda exhibition](http://biowikifarm.net/v-mfn/panda_en/index.php). The construction and provisioning of wikis has been the subject of two research projects at the Museum of Natural History Berlin [@patzschke2016]. The experience gained demonstrates that creating and maintaining a semantic wiki is challenging, a major difficulty being that the complexity of the information stored in the wiki tends to increase as the user base grows, and new ideas are integrated into the wiki's semantic structure [@kiniti2013wikis].

## Methodical approach
Coping with this increasing complexity led to the development of a methodical approach for simplifying the creation and maintenance of semantic wikis. One way to create a semantic wiki is to model the semantic relationships underlying the information in the wiki as an ontology, and then to customize a wiki to reflect the constructs described by the ontology [@di2006automatic]. Ontology engineering is a vast topic by itself, yet a simple methodology could follow these basic steps [@noy2001ontology]: obtaining domain information by consulting experts and gathering specific vocabularies (e.g. in the case of Museum of Natural History Berlin, zoological taxonomy, stratigraphical vocabulary and others); subsequently, modelling the ontology in an external tool such as Protégé [@DBLP:journals/aimatters/Musen15], and storing the result as an RDF/XML file [@rdfspec]. Software implemented at the Museum of Natural History Berlin automates the conversion of the ontology file into web pages and forms in the wiki. This software is [distributed under an Open Source License](https://github.com/MfN-Berlin/RDF-to-SemanticWiki), in the hope that it can be useful for computer scientists researching computer-mediated collaboration and ontology engineering.

## Implementation details
The process by which the conversion of the ontology into a wiki is automated is implemented as follows: the RDF/XML file representing the ontology is parsed into an in-memory semantic model. Then, for each object in the model, a data access object (DAO) is created using a factory class. A connection is established with the wiki's web service (API). Finally, each DAO object saves itself to the wiki, using the wiki's API. With an ontology as input, the software knows two commands: "import" creates the necessary wiki pages, "delete" removes the corresponding wiki pages. The layout of the wiki is customizable through templating: templates can be used to specify the order in which elements should appear, as well as to filter out or hide some elements. The software is written in Python, templates are in XSLT. The resulting wiki pages are compatible with the semantic extension to the popular MediaWiki software [@smw].

Ontology constructs are mapped to the wiki artefacts according to these rules: ontology classes are mapped to forms, templates and page categories; data attributes are mapped to property pages of the corresponding data type; relations between objects are rendered as links between pages. The cardinality of attributes is enforced through appropriate form input fields. Class inheritance is supported. Furthermore, navigation elements are added to the wiki, to enable creating, listing and editing content following the structure defined by the ontology. The information stored in the wiki using these forms and templates is thus structured and consistent, and can be accessed using semantic queries [@smw].

## Future work
The software supports research at the Museum of Natural History Berlin by providing a way to create collaboration environments for working on complex scientific projects, while enforcing structure and consistency. As ontologies can be reused and extended [@noy2001ontology], the methodical approach facilitates knowledge transfer between projects, as taxonomies and vocabularies found useful in one project can be used to construct a wiki for a second project. As discussed above, the implemented software supports the conversion of semantic classes, attributes and relations, class inheritance and cardinality. This is a subset of the constructs defined by the RDF/XML specification [@rdfspec]. More work is needed to extend the possibilities of the software so as to pave the way for more expressive collaboration environments.

## Acknowledgements
Software development at Museum für Naturkunde Berlin was sustained in part by the project "Knowledge Transfer Concept for Research Contents, Methods and Competences in Research Museums", funded by the German Federal Ministry of Education and Research (BMBF), grant no. 01IO1632.


# References
