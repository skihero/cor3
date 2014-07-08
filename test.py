#!/usr/bin/env python 

from PIL import Image 
from pytesseract import image_to_string

import sys 

print image_to_string(Image.open(sys.argv[1]))


