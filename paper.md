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
date: 16 August 2019
bibliography: paper.bib
---

# Summary

Wikis are web platforms allowing for collaborative authoring of information. A semantic wiki is a wiki whose functionality has been extended to encode information in a structured and machine-readable way [@wikipediasemantic]. Information encoded semantically forms a "consistent logical web of data" [@berners1998semantic], that can be used for enriching information with metadata, checking the consistency of information against an agreed upon schema, or accessing and combining data from different sources. 

Semantic wikis have been used at the Museum für Naturkunde Berlin (natural history museum, MfN) since 2015. A total of 15 semantic wikis are currently online at the MfN and support research projects by providing services for developing and documenting collection management and imaging procedures, annotating archive material, as publication medium for conference presentations and supplement temporary exhibitions [@ortiz2016]. The construction and provisioning of wikis has been the subject of two research projects at the MfN [@patzschke2016]. The experience gained demonstrates that creating and maintaining a semantic wiki is challenging, a major difficulty being that the complexity of the information stored in the wiki tends to increase as the user base grows and new ideas are integrated into the wiki's semantic structure [@kiniti2013wikis]. One way to simplify this process is to model the semantic relationships underlying the information in the wiki as an ontology, and then to customize a wiki to reflect the concepts described by the ontology [@di2006automatic]. 

``RDF-to-SemanticWiki`` aims to simplify the process of creating and maintaining a semantic wiki. The first step of this process is to obtain domain information by consulting experts and gathering specific taxonomies and vocabularies (e.g. in the case of MfN, zoological taxonomy, stratigraphical vocabulary and others). Subsequently, an ontology is modelled in an external tool such as Protégé [@DBLP:journals/aimatters/Musen15], and stored as an RDF/XML file [@rdfspec]. In a wiki, semantic information is recorded in the pages themselves: metadata is encoded as page annotations, consistent input and output of information is implemented through page forms and templates, and accessing information is achieved through queries embedded in the page source [@smw]. ``RDF-to-SemanticWiki`` automates the convertion of the ontology into templates, forms and attribute pages in the wiki. The software is designed to be used by computer scientists researching computer-mediated collaboration and ontology engineering. The user interface of the wiki is customizable through templating. An example implementation using Semantic MediaWiki [@smw] is provided.

# Acknowledgements
This software was written as part of the project "Knowledge Transfer Concept for Research Contents, Methods and Competences in Research Museums" at the Museum für Naturkunde Berlin, funded by the Federal Ministry of Education and Research.

# References
