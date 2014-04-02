from optparse import OptionParser
import sys
import os

parser = OptionParser()
parser.add_option("-m", action="store", dest="morph")
(opts, args) = parser.parse_args()
print opts.morph
