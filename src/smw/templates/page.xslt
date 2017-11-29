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

    <!-- Class comment -->
    <xsl:apply-templates select="." mode="comment"/>
    
    <xsl:apply-templates select="DatatypeProperty"/>
    <xsl:apply-templates select="ObjectProperty"/>
    
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
    <xsl:if test="@name!=''">
      <!-- Property name (localized) -->
      ==<xsl:apply-templates select="." mode="label"/>==

      <!-- Property comment -->
      <xsl:apply-templates select="." mode="comment"/>

      <!--Property value-->
      [[<xsl:value-of select="@name" />::{{{<xsl:value-of select="@name" />|}}}]]
      
      <!-- Link to attribute page -->
      [<xsl:value-of select="$baseUrl" />Property:<xsl:value-of select="@name" /><xsl:text> </xsl:text><xsl:apply-templates select="." mode="label" />]
    </xsl:if>
  </xsl:template>
  
  <!--
      ##########################
      Process an object property
      ##########################
  -->
  <xsl:template match="ObjectProperty">

    <xsl:if test="@range!=''">
      <!-- Property name (localized) -->
      ==<xsl:apply-templates select="." mode="label" />==
      
      <!-- Property comment -->
      <xsl:apply-templates select="." mode="comment"/>

      <!--Property value-->
      {{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|*[[::[[<xsl:value-of select="@name"/>::x]]|[[<xsl:value-of select="@name"/>::x]]]]|\n\n}}
      {{#if: {{{<xsl:value-of select="@name"/>}}} | {{#set: <xsl:value-of select="@name"/>={{{<xsl:value-of select="@name"/>|}}} }} |}}
      
    </xsl:if>

  </xsl:template>

</xsl:stylesheet>
