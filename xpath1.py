#! /usr/bin/env python
# coding: utf-8 
import sys, libxml2


def open(xml_file):
  doc = libxml2.parseFile(xml_file)
  ctxt = doc.xpathNewContext ()
  #students = ctxt.xpathEval("//student") # все студенты
  #students = ctxt.xpathEval("//department[@number='36']/group/student") # все студенты 36-й кафедры
  #students = ctxt.xpathEval("//faculty[@shortname='Cyb']//student") # все студенты факультета КиБ
  #for st in students: # цикл для предыдущих запросов
   # print st.prop("lastname")
  #print students
  groups = ctxt.xpathEval("//student[@lastname='Меркель']/..")
  print groups[0].prop("grnumber")
  print groups[0].xpathEval("child::*") # все дети
  print groups[0].xpathEval("attribute::*") # все аттрибуты
  ctxt.xpathFreeContext ()
  doc.freeDoc ()


def main(argv):
  if len(argv) != 2:
    sys.stderr.write("Usage : %s xml_file" % (argv[0],))
  else:
    open(argv[1])

if __name__ == '__main__':
  main(sys.argv)  
