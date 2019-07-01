---
title: 'RDF-to-MediaWiki: Creating ontology-based semantic wikis'
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
date: 1 July 2019
bibliography: paper.bib
---

# Summary

Wikis are web platforms allowing for collaborative authoring of information. A semantic wiki is a wiki whose functionality has been extended to encode information in a structured and machine-readable way [@wikipediasemantic]. Information encoded semantically forms a "consistent logical web of data", that can be used for enriching information with metadata, checking the consistency of information against an agreed upon schema, accessing and combining data from different sources [@berners1998semantic].

In a wiki, semantic information is stored in the pages themselves: metadata is encoded as page annotations, consistent input and output of information is implemented through page forms and templates, and accessing information is achieved through queries stored in the page source [@smw]. Nevertheless, creating and maintaining a semantic wiki is challenging, since the complexity of the information stored in the wiki tends to increase as the user base grows and new ideas are integrated into the wiki's structure [@kiniti2013wikis].

One way to simplify this process is to model the semantic relationships underlying the information in the wiki as an ontology, and then to convert the ontology into templates, forms and attribute pages in the wiki [@di2006automatic]. The software described here automates the conversion process: an ontology modelled in an external tool such as Protégé [@protege], once stored as an RDF/XML-schema[@rdfspec] can be used to create a new wiki or to enhance an existing one. The software is designed to be extendable and customizable. An example implementation using Semantic MediaWiki[@smw] is provided.

# Acknowledgements
This software was written as part of the project "Knowledge Transfer Concept for Research Contents, Methods and Competences in Research Museums" at the Museum für Naturkunde Berlin, funded by the Federal Ministry of Education and Research.
