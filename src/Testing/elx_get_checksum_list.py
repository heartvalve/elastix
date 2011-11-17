import sys
import os
import os.path
from optparse import OptionParser

#-------------------------------------------------------------------------------
# the main function
def main():
    # usage, parse parameters
    usage = "usage: %prog [options] arg"
    parser = OptionParser( usage )

    # option to debug and verbose
    parser.add_option( "-v", "--verbose",
        action="store_true", dest="verbose" )

    # options to control files
    parser.add_option( "-l", "--list", type="string", dest="directoryList", help="list of elastix output directories" )
    #parser.add_option( "-o", "--output", dest="output", help="output text file" )

    (options, args) = parser.parse_args()

    # Convert string -l to list
    dirList = options.directoryList.split( ' ' )
    # Add everything not processed
    dirList.extend( args );
    #print "dirList: %s" % dirList

    print "directory checksum"

    for directory in dirList:
      # Equivalent to: fileName = options.directory + "/" + "elastix.log"
      fileName = os.path.join( directory, "elastix.log" );

      # Read elastix.log and find last line with checksum
      try:
        f = open( fileName )
      except IOError as e:
        print "%s No elastix.log found" % directory
        continue

      checksumFound = False;
      for line in f:
        if "Registration result checksum:" in line:
          checksumline = line;
          checksumFound = True;

      # Extract checksum
      if checksumFound:
        checksum = checksumline.split(': ')[1].rstrip( "\n" );

        # Print result
        print "%s %s" % (directory, checksum)
      else:
        print "%s -" % directory

      f.close();

    return 0

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(main())
