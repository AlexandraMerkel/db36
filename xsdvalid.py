#! /usr/bin/env python
import sys, libxml2


def schema_validate(xml_file, xsd_file):
    ctxt = libxml2.schemaNewParserCtxt(xsd_file)
    schema = ctxt.schemaParse()
    validationCtxt = schema.schemaNewValidCtxt()
    res = validationCtxt.schemaValidateFile(xml_file, 0)
    #doc = libxml2.parseFile(xml_file)
    #res = validationCtxt.schemaValidateDoc(doc)
    #doc.freeDoc()
    if res != 0:
        print "VALIDATION FAILED"
    else:
        print "VALIDATED"
    return res


    
def main(argv):
    if len(argv) != 3:
        sys.stderr.write("Usage : %s xml_file sxd_file" % (argv[0],))
    else:
        print  schema_validate(argv[1], argv[2])
        

if __name__ ==  '__main__':
    main(sys.argv)
    
