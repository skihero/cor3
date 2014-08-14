#!/usr/bin/env python 

import sys 
from pytesseract import image_to_string
from PIL import Image
import Queue

# local import 
from filelist import Job
from filelist import files

q = Queue.PriorityQueue()

for fil in files: 
	q.put(Job(fil[0], fil[1], fil[2]))

while not q.empty():
    next_job = q.get()
    print next_job 
    print 'Processing job:', next_job.url
    print image_to_string(Image.open(next_job.url))


