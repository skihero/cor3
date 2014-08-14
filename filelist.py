
# Simple data 

files=[ 
	['ll', 'image_sample', 'image_sample.jpg'], 
	['3', 'font_image' , 'test.png' ], 
	] 


class Job(object):
    def __init__(self, priority, desc, url):
        self.priority = priority
	self.desc = desc 
        self.url = url
        print 'New job:', url
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)


