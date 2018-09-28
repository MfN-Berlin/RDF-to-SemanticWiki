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
    <xsl:call-template name="header"/>

    
    {{{for template|<xsl:value-of select="@name" />}}}
    <xsl:apply-templates select="DatatypeProperty" mode="form"/>
    <xsl:apply-templates select="ObjectProperty" mode="form"/>
    {{{end template}}}

    <!-- Buttons -->
    <xsl:call-template name="buttons"/>

    <!-- Bottom of page -->
    <xsl:apply-templates select="." mode="footer"/>

  </xsl:template>

  <!-- FORM HEADER -->
  <xsl:template name="header">
    &lt;noinclude&gt;
    <!-- Form name (localized) -->
    {{DISPLAYTITLE:<xsl:apply-templates select="." mode="label"/>}}
    {{#forminput:form=<xsl:value-of select="@name" />}}
    &lt;/noinclude&gt;
    &lt;includeonly&gt;<xsl:apply-templates select="." mode="helpIcon"/>
    <!-- Class info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />    
  </xsl:template>
  
  <!-- FORM BUTTONS -->
  <xsl:template name="buttons">    
    {{{standard input|minor edit}}}{{{standard input|watch}}}

    {{{standard input|save}}}{{{standard input|changes}}}

    {{{standard input|cancel}}}
  </xsl:template>
  
  <!-- FORM FOOTER -->
  <xsl:template match="/SemanticClass" mode="footer">    
    <!--Suppress table-of-contents and paragraph edit links-->
    __NOTOC__
    __NOEDITSECTION__
  </xsl:template>

  <!--
      ###########################
      Process a datatype property
      ###########################
  -->
  <xsl:template match="DatatypeProperty" mode="form">
    <!-- Property name (localized) and help icon-->
    ==<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>==
    
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <!-- Form input fields -->
    <xsl:value-of select='/Enumeration'/>
    <xsl:choose>
      <xsl:when test="@cardinality='FunctionalProperty'">
	<xsl:choose>
	  <!--
	      Enumeration properties have the name of their enumeration class as range attribute,
	      and the allowed values are a child element. 
	  -->
	  <xsl:when test="allowedValues">
	    <!-- Property as a dropdown -->
	    {{{field|<xsl:value-of select="@name"/>
	    |property=<xsl:value-of select="@name"/>
	    |input type=dropdown
	    }}}
	  </xsl:when>
	  <xsl:when test="@range='Literal'">
	    {{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=textarea|editor=wikieditor|rows=10}}}
	  </xsl:when>
	  <xsl:when test="@range='boolean'">
	    {{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=radiobutton| mandatory|default=false}}}
	  </xsl:when>
	  <xsl:when test="@range='dateTime'">
	    {{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=date}}}
	  </xsl:when>
	  <xsl:when test="@range='int'">
	    {{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=text|size=10}}}
	  </xsl:when>
	  <xsl:otherwise>
	    {{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=text}}}
	  </xsl:otherwise>
	</xsl:choose>
      </xsl:when>
      <xsl:otherwise>
	<xsl:value-of select="$i18nTexts/multipleValues[@lang = $lang]"/>
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=text|list|delimiter=;}}}
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!--
      ##########################
      Process an object property
      ##########################
  -->
  <xsl:template match="ObjectProperty" mode="form">
    <!-- Property name (localized) and help icon-->
    ==<xsl:apply-templates select="." mode="label" /> <xsl:apply-templates select="." mode="helpIcon"/>==
    
    <!-- Property info -->
    <xsl:apply-templates select="." mode="collapsibleInfo" />
    
    <xsl:choose>
      <xsl:when test="@cardinality='FunctionalProperty'">
	<!-- Object property as a dropdown -->
	{{{field|<xsl:value-of select="@name"/>
	|property=<xsl:value-of select="@name"/>
	| values from category=<xsl:value-of select="@range"/>
	|input type=dropdown
	}}}
      </xsl:when>
      <xsl:otherwise>
	<xsl:value-of select="$i18nTexts/multipleChoice[@lang = $lang]"/>&lt;br/&gt;
	<!-- Object properties as a listbox -->
	{{{field|<xsl:value-of select="@name"/>
	|property=<xsl:value-of select="@name"/>
	| values from category=<xsl:value-of select="@range"/>
	|input type=listbox
	|size=10
	|list
	|delimiter=@
	}}}
      </xsl:otherwise>
    </xsl:choose>

  </xsl:template>

</xsl:stylesheet>
