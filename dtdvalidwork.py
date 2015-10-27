#! /usr/bin/env python
import sys, libxml2


def validate(xml_file, dtd_file):
    doc = libxml2.parseFile(xml_file)
    dtd = libxml2.parseDTD(None, dtd_file)
    ctxt = libxml2.newValidCtxt()
    ret = doc.validateDtd(ctxt, dtd)
    dtd.freeDtd()
    doc.freeDoc()
    return ret
    
def main(argv):
    if len(argv) != 3:
        sys.stderr.write("Usage : %s xml_file dtd_file" % (argv[0],))
    else:
        print validate(argv[1], argv[2])
        

if __name__ ==  '__main__':
    main(sys.argv)
    
