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
    <!-- Top of page -->
    <xsl:apply-templates select="." mode="helpIcon"/>    
    <xsl:apply-templates select="." mode="collapsibleInfo" />

    <!-- Content -->
    <xsl:apply-templates select="DatatypeProperty" mode="page"/>
    <xsl:apply-templates select="ObjectProperty" mode="page"/>
    
    <!-- Bottom of page -->
    <xsl:apply-templates select="." mode="footer"/>
  </xsl:template>

  <!-- FOOTER -->
  <xsl:template match="/SemanticClass" mode="footer">
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
    ===<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>===
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    <!--Property value-->
    <xsl:choose>
      <xsl:when test="@cardinality='FunctionalProperty'">
	[[<xsl:value-of select="@name" />::{{{<xsl:value-of select="@name" />|}}}]]
      </xsl:when>
      <xsl:otherwise>
	{{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|;|x|*x|\n\n}}
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  
  <!--
      ##########################
      Process an object property
      ##########################
  -->
  <xsl:template match="ObjectProperty" mode="page">
    <!-- Property name (localized) and help icon-->
    ===<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>===
    
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <!--Property value-->
    <xsl:choose>
      <xsl:when test="@cardinality='FunctionalProperty'">
	[[<xsl:value-of select="@name" />::{{{<xsl:value-of select="@name" />|}}}]]
      </xsl:when>
      <xsl:otherwise>
	{{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|*[[x]]|\n\n}}
	{{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|{{#set: <xsl:value-of select="@name" />=x }}|}}
      </xsl:otherwise>
    </xsl:choose>    
  </xsl:template>
  
</xsl:stylesheet>
