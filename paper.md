---
title: 'RDF-to-SemanticWiki: Creating ontology-based semantic wikis'
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
date: 29 August 2019
bibliography: paper.bib
---

# Summary

Wikis are web platforms allowing for collaborative authoring of information. A semantic wiki is a wiki whose functionality has been extended to encode information in a structured and machine-readable way: information encoded semantically forms a "consistent logical web of data" [@berners1998semantic], that can be used for enriching information with metadata, checking the conformance of information against an agreed upon schema, or accessing and combining data from different sources [@oren2006semantic].

Semantic wikis have been used at the Museum für Naturkunde Berlin (natural history museum, MfN) since 2015. A total of 15 semantic wikis are currently online at the MfN and support research by providing services for developing and documenting collection management and imaging procedures, annotating archive material, as publication medium for conference presentations and supplement temporary exhibitions [@ortiz2016]. The construction and provisioning of wikis has been the subject of two research projects at the MfN [@patzschke2016]. The experience gained demonstrates that creating and maintaining a semantic wiki is challenging, a major difficulty being that the complexity of the information stored in the wiki tends to increase as the user base grows and new ideas are integrated into the wiki's semantic structure [@kiniti2013wikis]. Coping with the increasing complexity of the wikis led to the development of ``RDF-to-SemanticWiki``.

``RDF-to-SemanticWiki`` aims to simplify the process of creating and maintaining a semantic wiki. One way to create a semantic wiki is to model the semantic relationships underlying the information in the wiki as an ontology, and then to customize a wiki to reflect the constructs described by the ontology [@di2006automatic]. The first step of this process is to obtain domain information by consulting experts and gathering specific taxonomies and vocabularies (e.g. in the case of MfN, zoological taxonomy, stratigraphical vocabulary and others). Subsequently, an ontology is modelled in an external tool such as Protégé [@DBLP:journals/aimatters/Musen15], and stored as an RDF/XML file [@rdfspec]. ``RDF-to-SemanticWiki`` automates the conversion of the ontology constructs into web pages and forms in the wiki. 

The process by which ``RDF-to-SemanticWiki`` automates the conversion of the ontology into a wiki follows these steps: the RDF/XML file representing the ontology is parsed into an in-memory semantic model. Then, for each object in the model, a data access object (DAO) is created using a factory class. A connection is established with the wiki's web service (API). Finally, each DAO object saves itself to the wiki, using the wiki's API. With an ontology as input, ``RDF-to-SemanticWiki`` knows two commands: "import" creates the necessary wiki pages, "delete" removes the corresponding wiki pages. The layout of the wiki is customizable through templating: templates can be used to specify the order in which elements should appear, as well as to filter out or hide some elements. ``RDF-to-SemanticWiki`` is written in Python, templates are in XSLT. The output of ``RDF-to-SemanticWiki`` can be published using the Semantic MediaWiki extension to the popular MediaWiki software [@smw].

The mapping between the ontology constructs and the wiki artefacts is as follows: ontology classes are mapped to forms, templates and page categories; data attributes are mapped to property pages of the corresponding type; relations between objects are rendered as links between pages. The cardinality of attributes is enforced through appropriate form input fields. Class inheritance is supported. Furthermore, navigation elements are added to the wiki, to enable creating, listing and editing content following the structure defined by the ontology. The information stored in the wiki using these forms and templates is thus structured and consistent, and can be accessed using semantic queries [@smw].

``RDF-to-SemanticWiki`` is designed to be used by computer scientists researching computer-mediated collaboration and ontology engineering. ``RDF-to-SemanticWiki`` supports research by providing a way to create collaboration environments for working on complex scientific projects, while enforcing structure and consistency. As ontologies can be reused and extended [noy2001ontology], ``RDF-to-SemanticWiki`` facilitates knowledge transfer between projects, as taxonomies and vocabularies found useful in one project can be used to construct a wiki for a second project. As discussed above, ``RDF-to-SemanticWiki`` supports the conversion of semantic classes, attributes and relations, class inheritance and cardinality. This is a subset of the constructs defined by the RDF/XML specification [@rdfspec]. More work is needed to extend the possibilities of ``RDF-to-SemanticWiki`` so as to pave the way for more expressive collaboration environments.

# Acknowledgements
``RDF-to-SemanticWiki`` development was sustained in part by the project "Knowledge Transfer Concept for Research Contents, Methods and Competences in Research Museums" at the Museum für Naturkunde Berlin, funded by the German Federal Ministry of Education and Research (BMBF), grant no. 01IO1632.


# References
