#!/usr/bin/env python 

from PIL import Image 
from pytesseract import image_to_string

import sys 


print "sys.argv[]"
print  sys.argv
print image_to_string(Image.open(sys.argv[1]))

#print image_to_string(Image.open('test-european.jpg'), lang='fra')

