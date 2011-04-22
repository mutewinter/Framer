# framer.py

# Author: Jeremy Mack
# Code Website: TODO
# Company: Pile of Turtles, LLC
# Company Website: http://pileofturtles.com

# Acorn script that opens a target screenshot and applies the iPad frame It
# accepts one argument, which is the location of the PNG file to which it is
# going to add the screenshot.

import glob
#import sys
import os
import lib.argparse as argparse
from subprocess import call


def parse_commandline_arguments():
  parser = argparse.ArgumentParser(description=
      """
      Wrapper for framer.jstalk to call it for a set of image files in a given
      directory.
      """
      )

  parser.add_argument('directory', metavar='DIRECTORY', type=str, nargs=1,
      help='The directory to process')



  return parser.parse_args()
  

jstalk = "jstalk"
framerJS = "framer.jstalk"
outputFolderName = "output"


def process_directory(directory):
  if directory:
    outputFolder = os.path.join(directory, outputFolderName) 
    if not os.path.exists(outputFolder):
      print "Created output directory"
      os.makedirs(outputFolder)
    

    print "Parsing images in " + directory

    for pngFile in glob.glob(directory + '*.png'):
      call([jstalk, framerJS, pngFile])

if __name__ == '__main__':
  args = parse_commandline_arguments()

  process_directory(args.directory[0])
