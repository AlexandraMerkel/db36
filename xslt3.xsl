<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:output encoding="utf-8" method="html" />
     
      <xsl:template match="/" >
        <h1>Статистика</h1>
        <table>
          <tr>
            <td>№</td>
            <td>Группа</td>
            <td>Количество студентов</td>
            <td>Факультет</td>
            <td>Курс</td>  
          </tr> 
 
        <xsl:for-each select="//group">
          <xsl:sort order="ascending" select="@course" />
          <xsl:sort order="ascending" select="@name" />
          <tr> 
            <td><xsl:value-of select='position()'/></td>
            <td><xsl:value-of select='@name'/></td>
            <td><xsl:value-of select='count(student)'/></td>
            <td><xsl:value-of select='../../@short_name'/></td>
            <td><xsl:value-of select='@course'/></td>
          </tr>
          
        </xsl:for-each>
       </table>
      </xsl:template>
    </xsl:stylesheet>
