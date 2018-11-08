#!/usr/bin/python
import Cocoa
import sys
import os


# Check the amount of arguments
if len(sys.argv) != 3:
    sys.exit("Usage: {} /path/to/image /path/to/file".format(sys.argv[0]))


# Extract paths
file = sys.argv[1].decode("utf-8")
dir = sys.argv[2].decode("utf-8")


# Check if the image and the folder exist
if not os.path.isfile(file):
    sys.exit("\"{}\" does not exists/is not a file".format(file))

if not os.path.isdir(dir):
    sys.exit("\"{}\" does not exists/is not a directory".format(dir))


# Open image
try:
    image = Cocoa.NSImage.alloc().initWithContentsOfFile_(file)
except:
    sys.exit("Failed to open \"{}\" as image".format(file))


# Set image as icon
try:
    Cocoa.NSWorkspace.sharedWorkspace().setIcon_forFile_options_(image, dir, 0)
except:
    sys.exit("Failed to set \"{}\" as icon for \"{}\"".format(file, dir))
