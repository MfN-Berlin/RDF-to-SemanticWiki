<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <!-- Output is MediaWiki markup-->
  <xsl:output method="text" encoding="UTF-8" />
  
  <!--
      #########################
      Process a localized label
      #########################
  -->
  <xsl:template match="SemanticClass|DatatypeProperty|ObjectProperty" mode="label">
    <xsl:choose>
      <xsl:when test="labels/label[@lang=$lang]">
	<xsl:value-of select="labels/label[@lang=$lang]" />
      </xsl:when>
      <xsl:otherwise>
	<xsl:value-of select="@name" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!--
      ###########################
      Process a localized comment
      ###########################
  -->
  <xsl:template match="SemanticClass|DatatypeProperty|ObjectProperty" mode="comment">
      <xsl:if test="comments/comment[@lang=$lang]">
	&lt;div class="tip"&gt;<xsl:value-of select="comments/comment[@lang=$lang]" />&lt;/div&gt;
	
      </xsl:if>    
  </xsl:template>
  
</xsl:stylesheet>
