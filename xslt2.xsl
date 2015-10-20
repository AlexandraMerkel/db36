<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:output encoding="utf-8" method="html" />
     
      <xsl:template match="/" >
        <h1>КИБ</h1>
        <table>
          <tr>
            <td>№</td>
            <td>ФИО</td>
            <td>Группа</td>
          </tr> 
 
        <xsl:for-each select="//faculty[@shortname='Cyb']//student">
          <xsl:sort order="ascending" select="@lastname" />
          <tr> 
            <td><xsl:value-of select='position()' /></td>
            <td><xsl:value-of select='@lastname' /></td>
            <td><xsl:value-of select='../@grnumber' /></td>
          </tr>
          
        </xsl:for-each>
       </table>
      </xsl:template>
    </xsl:stylesheet>
