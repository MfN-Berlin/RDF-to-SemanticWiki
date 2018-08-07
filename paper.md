---
title: 'RDF-to-MediaWiki: Import an ontology into a semantic wiki'
tags:
  - semantic web
  - wiki
  - ontology
authors:
 - name: Alvaro Ortiz-Troncoso
   orcid: 0000-0001-7620-1907
   affiliation: 1
affiliations:
 - name: Museum für Naturkunde Berlin
   index: 1
date: 8 August 2018
bibliography: paper.bib
---

# Summary

Wikis are web platforms allowing for collaborative authoring of information. A semantic wiki is a wiki whose functionality has been extended to encode information in a structured and machine-readable way [@wikipediasemantic].

Creating and maintaining a wiki can be challenging, since the complexity of the information stored in the wiki tends to increase as the user base grows and new ideas are integrated into the wiki's structure [@kiniti2013wikis].

One way to simplify this process is to model the semantic relationships underlying the information in the wiki as an ontology, and then to convert the ontology into templates, forms and attribute pages in the wiki programmatically [@di2006automatic].

RDF-to-Mediawiki automates the conversion process. An ontology modelled in an external tool such as Protégé [@protege], can be used to create a new wiki or to enhance an existing one. RDF-to-Mediawiki is designed to be extendable and customizable. An example implementation for Semantic MediaWiki is provided [@smw].

