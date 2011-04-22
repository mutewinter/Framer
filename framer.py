# framer.py

# Author: Jeremy Mack
# Code Website: TODO
# Company: Pile of Turtles, LLC
# Company Website: http://pileofturtles.com

# Wrapper for framer.jstalk to call it for a set of image files in a given
# directory.

import glob
import os
import lib.argparse as argparse
from subprocess import call

jstalk = "jstalk"
framerJS = "framer.jstalk"
outputFolderName = "framed"
script_folder = os.path.dirname(os.path.abspath(__file__))
resources_directory = os.path.join(script_folder, "resources/")

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
  

def process_directory(directory):
  if directory:
    print "Getting my frame on."

    outputFolder = os.path.join(directory, outputFolderName) 
    if not os.path.exists(outputFolder):
      print "framed folder created"
      os.makedirs(outputFolder)
    

    pngFiles = glob.glob(directory + '*.png')

    for pngFile in pngFiles:
      call([jstalk, framerJS, pngFile, resources_directory])

    print "Framed %d images!" % len(pngFiles)

if __name__ == '__main__':
  args = parse_commandline_arguments()
  process_directory(args.directory[0])
