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
    {{#default_form:<xsl:value-of select="@name" />}}
    {{#forminput:form=<xsl:value-of select="@name" />|autocomplete on category=<xsl:value-of select="@name" />}}
  </xsl:template>
</xsl:stylesheet>
