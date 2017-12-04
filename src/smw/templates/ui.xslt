<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:i18n="i18n" exclude-result-prefixes="i18n">
  
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

  <!--
      #####################################
      Localized texts used in the templates
      #####################################
  -->
  <i18n:messages>
    <i18n:msg key="None">
      <i18n:text lang="en">No results found.</i18n:text>
      <i18n:text lang="de">Keine Angabe.</i18n:text>
    </i18n:msg>
  </i18n:messages>
  
  <xsl:variable name="i18nTexts" select="document('')/*/i18n:messages"/>
  
  <xsl:template name="i18n">
    <xsl:param name="key"/>
    <xsl:param name="lang"/>
    <xsl:value-of select="$i18nTexts/i18n:msg[@key=$key]/i18n:text[@lang=$lang]"/>
  </xsl:template>

  <!--
      ########################
      Collapsible info element
      ########################
  -->
  <xsl:template match="SemanticClass|DatatypeProperty|ObjectProperty" mode="collapsibleInfo">    
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
  <xsl:template match="SemanticClass" mode="helpIcon">&lt;span class="mw-customtoggle mw-customtoggle-<xsl:value-of select="@name"/>" style="float: right;margin-top: -60px;"&gt;<xsl:value-of select="$helpIcon"/>&lt;/span&gt;</xsl:template>
  
</xsl:stylesheet>
