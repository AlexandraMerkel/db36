#! /usr/bin/env python
import sys, libxml2

def open(xml_file):
  doc = libxml2.parseFile(xml_file)
  root = doc.getRootElement()
#  print root.name
  fac = root.children #.next - go to first child
  while fac is not None:
    if fac.type == "element":
      dep=fac.children
      while dep is not None:
        if dep.type == "element":
          #print dep.prop("number")
          group=dep.children
	  while group is not None:
            if group.type == "element":
              #print group.prop("grnumber")
              student=group.children
              while student is not None:
                if student.type == "element":
                  print student.prop("lastname")
                  #print student.prop("firstname")
                student=student.next
            group=group.next
        dep=dep.next
    fac=fac.next
  doc.freeDoc()

def main(argv):
  if len(argv) != 2:
    sys.stderr.write("Usage : %s xml_file" % (argv[0],))
  else:
    open(argv[1])

if __name__ == '__main__':
  main(sys.argv)
