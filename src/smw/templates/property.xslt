<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Imports -->
  <xsl:import href="label.xslt" />
  <!-- Output is MediaWiki markup-->
  <xsl:output method="text" encoding="UTF-8" />
  
  <!-- Global variables -->
  <xsl:variable name="lang" select="/*/@lang" />

  <!--
      ###########################################
      Process a datatype property
      ###########################################
  -->
  <xsl:template match="/DatatypeProperty">
    <!-- Property name (localized) -->
    {{DISPLAYTITLE:<xsl:apply-templates select="." mode="label"/>}}

    <!-- Property comment -->
    <xsl:apply-templates select="." mode="comment"/>

    <xsl:variable name="type">
      <xsl:choose>
	<xsl:when test="@range='dateTime'">Date</xsl:when>
	<xsl:when test="@range='boolean'">Boolean</xsl:when>
	<xsl:when test="@range='string'">Text</xsl:when>
	<xsl:when test="@range='DataOneOf'">Text</xsl:when>
	<xsl:otherwise>Text</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
      
    This is a property of type [[Has type::<xsl:value-of select="$type"/>]].

    <xsl:apply-templates select="allowedValues/allowed"/>
      
  </xsl:template>

  <xsl:template match="allowed">
    [[Allows value::<xsl:value-of select="."/>]]
  </xsl:template>
  
  
  <!--
      ###########################################
      Process an object property
      ###########################################
  -->
  <xsl:template match="/ObjectProperty">

    <!-- Property name (localized) -->    
    {{DISPLAYTITLE:<xsl:apply-templates select="." mode="label"/>}}
    
    <!-- Property comment -->
    <xsl:apply-templates select="." mode="comment"/>
    
    This is a property of type [[Has type::Text]].
      
  </xsl:template>

</xsl:stylesheet>

