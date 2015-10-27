#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, libxml2

def open(xml_file):
    doc = libxml2.parseFile (xml_file)
    ctxt = doc.xpathNewContext()
    students = ctxt.xpathEval("//student")
    students = ctxt.xpathEval("//facultet[@short_name='КИБ']/department/group/student")
    year = 2015
    students = ctxt.xpathEval("//group[@course<=(1+2015-{0})]/student".format(year))
    for st in  students:
        print st.prop("fio")

    groups =  ctxt.xpathEval("//student[@fio='Железняк Сергей Владимирович']/..")
    for g in  groups:
        print g.prop("name")

    cnt  = ctxt.xpathEval("count(//group[@name='К02-361']/student)")
    print cnt
    
    facultet  = ctxt.xpathEval("//department[@numer='36']/..")
    print facultet[0].prop("name")
    
    print  facultet[0].xpathEval("child::*")
    print  facultet[0].xpathEval("attribute::*")


    ctxt.xpathFreeContext ()
    doc.freeDoc ()
    
def main(argv):
    if len(argv) != 2:
        sys.stderr.write("Usage : %s xml_file" % (argv[0],))
    else:
        open(argv[1])


if __name__ ==  '__main__':
    main(sys.argv)
