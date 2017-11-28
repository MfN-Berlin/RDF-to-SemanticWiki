<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- Imports -->
  <xsl:import href="label.xslt" />
  <!-- Output is MediaWiki markup-->
  <xsl:output method="text" encoding="UTF-8" />
  
  <!-- Global variables -->
  <xsl:variable name="lang" select="/ObjectProperty/@lang" />
  
  <!--
      ###########################################
      Process an object property
      ###########################################
  -->
  <xsl:template match="/ObjectProperty">

      <!-- Property name (localized) -->
      ==<xsl:apply-templates select="." mode="label" />==
      
      This is a property of type [[Has type::page]].
      
  </xsl:template>

</xsl:stylesheet>

