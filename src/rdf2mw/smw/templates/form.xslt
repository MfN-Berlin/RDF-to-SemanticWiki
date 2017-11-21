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
    &lt;noinclude&gt;{{#forminput:form=<xsl:value-of select="@name" />}}&lt;/noinclude&gt;

    &lt;includeonly&gt;    
    <xsl:apply-templates match="DatatypeProperty" />
    <xsl:apply-templates match="ObjectProperty" />
    
    {{{end template}}}

    <!--Buttons-->
    {{{standard input|minor edit}}}
    {{{standard input|watch}}}{{{standard input|save}}}
    {{{standard input|changes}}} {{{standard input|cancel}}}
    
    <!--Suppress table-of-contents and paragraph edit links-->
    __NOTOC__
    __NOEDITSECTION__
    &lt;/includeonly&gt;

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

    <!-- Form input fields -->
    <xsl:choose>
      <xsl:when test="@range=Literal">
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=textarea|editor=wikieditor|rows=10}}}
      </xsl:when>
      <xsl:when test="@range=boolean">
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=radiobutton| mandatory|default=false}}}
      </xsl:when>
      <xsl:when test="@range=dateTime">
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=date}}}
      </xsl:when>
      <xsl:when test="@range=int">
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=text|size=10}}}
      </xsl:when>
      <xsl:otherwise>
	{{{field|<xsl:value-of select="@name" />|property=<xsl:value-of select="@name" />|input type=text}}}
      </xsl:otherwise>
    </xsl:choose>

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
    
    <!-- Object properties as a listbox -->
    {{{field|<xsl:value-of select="@range" />
    |property=<xsl:value-of select="@range" />
    |input type=listbox
    | values from category=<xsl:value-of select="@range" />
    |size=10
    |list
    |delimiter=@
    }}}

    <!-- Add an object link -->
    <div class="wt_toolbar">[<xsl:value-of select="$baseUrl" />Category:<xsl:value-of select="@name" /><xsl:text> </xsl:text><xsl:apply-templates select="." mode="label" />]</div>

  </xsl:template>

</xsl:stylesheet>
