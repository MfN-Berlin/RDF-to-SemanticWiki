<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Imports -->
  <xsl:import href="label.xslt" />
  
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
    
    <xsl:apply-templates match="DatatypeProperty" />
    <xsl:apply-templates match="ObjectProperty" />

    <!--Suppress table-of-contents and paragraph edit links-->
    __NOTOC__
    __NOEDITSECTION__
	
    <!-- Add a category for all classes using this template -->
    &lt;includeonly&gt;[[Category:<xsl:value-of select="@name" />]]&lt;/includeonly&gt;
  </xsl:template>

  <!--
      ###########################
      Process a datatype property
      ###########################
  -->
  <xsl:template match="DatatypeProperty">
    <!-- Property name (localized) -->
    ==<xsl:apply-templates select="." mode="label"/>==

    <!-- Property comment -->
    <xsl:if test="comments/comment[@lang=$lang]">
      ''<xsl:value-of select="comments/comment[@lang=$lang]" />''
    </xsl:if>

    <!--Property value-->
    [[<xsl:value-of select="@name" />::{{{<xsl:value-of select="@name" />|}}}]]
    
    <!-- Link to attribute page -->
    [<xsl:value-of select="$baseUrl" />Property:<xsl:value-of select="@name" /><xsl:text> </xsl:text><xsl:apply-templates select="." mode="label" />]
    
  </xsl:template>
  
  <!--
      ##########################
      Process an object property
      ##########################
  -->
  <xsl:template match="ObjectProperty">
    
    <!-- Property name (localized) -->
    ==<xsl:apply-templates select="." mode="label" />==
    
    <!-- Property comment -->
    <xsl:if test="comments/comment[@lang=$lang]">
      ''<xsl:value-of select="comments/comment[@lang=$lang]" />''
    </xsl:if>

    <!--Property value-->
    {{#arraymap:{{{<xsl:value-of select="@range" />|}}}|@|x|*[[<xsl:value-of select="@range" />::x]]|\n\n}}

    {{#if: {{{<xsl:value-of select="@range" />}}} | {{#set: %s={{{<xsl:value-of select="@range" />|}}} }} |}}

  </xsl:template>

</xsl:stylesheet>
