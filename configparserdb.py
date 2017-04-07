#!/bin/env python
#
# configparserdb.py
#
import ConfigParser
import sys, os
import getopt

def usage():
    print 'configparserdb.py -s <section> -e <element> [-d <db file>]'
    print '   where section - is the database key field'
    print '         element - is the field value being requested'
    print '         db file - is the database file (default is db.cfg)'

def read(dbfile, section, element):
    Config=ConfigParser.ConfigParser()
    Config.read(dbfile)
    if section in Config.sections():
        #print "%s found" % section
        if element in Config.options("%s" % section):
            #print "%s found" % element
            return Config.get('%s' % section, '%s' % element)
        else:
            print "Error: element %s not found. Choices are:" % element
            print Config.options(section)
            return '' 
    else:
	print "Error: section %s not found. Choices are:" % element
	print Config.sections()
        return ''


def main(argv):
    section = ''
    element = ''
    dbfile = 'db.cfg'
    try:
      opts, args = getopt.getopt(argv,"hs:e:d:",["section=","element=","db="])
    except getopt.GetoptError:
      usage()
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        usage()
        sys.exit(1)
      elif opt in ("-e", "--element"):
        element = arg
      elif opt in ("-s", "--section"):
        section = arg
      elif opt in ("-d", "--db"):
        dbfile = arg
    if os.path.isfile(dbfile) != True:
        print "Error: %s file not found." % dbfile
        usage()
        sys.exit(1)
    if section == '':
        print 'Error: -s <section> is mandatory'
        usage()
        sys.exit(1)
    if element == '':
        print 'Error: -e <element> is mandatory'
        usage()
        sys.exit(1)
    value=read(dbfile, section, element)
    if value == '':
        print "FAILED"
        sys.exit(1)
    else:
        print "%s" % value
        sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])

