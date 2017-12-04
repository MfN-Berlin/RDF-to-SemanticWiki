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
    <!-- Property name and info -->
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
    <!-- Property name and info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <!--Property value-->
    {{#arraymap:{{{<xsl:value-of select="@name"/>|}}}|@|x|*[[::[[<xsl:value-of select="@name"/>::x]]|[[<xsl:value-of select="@name"/>::x]]]]|}}
    {{#if: {{{<xsl:value-of select="@name"/>}}} | {{#set: <xsl:value-of select="@name"/>={{{<xsl:value-of select="@name"/>|}}} }} |}}
  </xsl:template>

  <!--
      ########################
      Collapsible info element
      ########################
  -->
  <xsl:template match="DatatypeProperty|ObjectProperty" mode="collapsibleInfo">
    <!-- Property name (localized) and help icon-->
    ==<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>==
    
    &lt;div class="tip mw-collapsible mw-collapsed" id="mw-customcollapsible-<xsl:value-of select="@name"/>"&gt;
      &lt;div class="mw-collapsible-content"&gt;
	<!-- Property comment -->
	<xsl:apply-templates select="." mode="comment"/>
	<!-- Link to attribute page -->
	[<xsl:value-of select="$baseUrl" />Property:<xsl:value-of select="@name" /><xsl:text> </xsl:text><xsl:apply-templates select="." mode="label" />]
      &lt;/div&gt;
    &lt;/div&gt; 
  </xsl:template>

  <!--
      ########################
      Help icon
      ########################
  -->
  <xsl:variable name="helpIcon">https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Help-browser.svg/21px-Help-browser.svg.png</xsl:variable>
  <xsl:template match="DatatypeProperty|ObjectProperty" mode="helpIcon">&lt;span class="mw-customtoggle mw-customtoggle-<xsl:value-of select="@name"/>"&gt;<xsl:value-of select="$helpIcon"/>&lt;/span&gt;</xsl:template>
  
</xsl:stylesheet>
