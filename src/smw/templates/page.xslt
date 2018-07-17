<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Imports -->
  <xsl:import href="ui.xslt" />
  
  <!-- Output is MediaWiki markup-->
  <xsl:output method="text" encoding="UTF-8" />
  
  <!-- Global variables -->
  <xsl:variable name="lang" select="/SemanticClass/@lang" />
  <xsl:variable name="baseUrl" select="/SemanticClass/@baseUrl" />

  <!--
      ###########################################
      Process a semantic class and its properties
      ###########################################
  -->
  <xsl:template match="/SemanticClass">

    <xsl:apply-templates select="." mode="helpIcon"/>
    
    <!-- Class info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <xsl:apply-templates select="DatatypeProperty" mode="page"/>
    <xsl:apply-templates select="ObjectProperty" mode="page"/>
    
    <!--Suppress table-of-contents and paragraph edit links-->
    __NOTOC__
    __NOEDITSECTION__
	
    <!-- Add a category for all classes using this template -->
    &lt;includeonly&gt;[[Category:<xsl:value-of select="@name"/>]]&lt;/includeonly&gt;
  </xsl:template>

  <!--
      ###########################
      Process a datatype property
      ###########################
  -->
  <xsl:template match="DatatypeProperty" mode="page">
    <!-- Property name (localized) and help icon-->
    ==<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>==
    
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />

    <!--Property value-->
    [[<xsl:value-of select="@name" />::{{{<xsl:value-of select="@name" />|}}}]]
    
  </xsl:template>
  
  <!--
      ##########################
      Process an object property
      ##########################
  -->
  <xsl:template match="ObjectProperty" mode="page">
    <!-- Property name (localized) and help icon-->
    ==<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>==
    
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <!--Property value-->
    {{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|*[[::[[<xsl:value-of select="@name"/>::x]]|[[<xsl:value-of select="@name"/>::x]]]]|\n\n}}
    {{#if: {{{<xsl:value-of select="@name"/>}}} | {{#set: <xsl:value-of select="@name"/>={{{<xsl:value-of select="@name"/>|}}} }} |}}
    
    <!--Add page to category for object property-->
    {{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|[[Category:x]]|\n\n}}
  </xsl:template>
  
</xsl:stylesheet>
