
class Job(object):
    def __init__(self, priority, description, url):
        self.priority = priority
	self.description = description
        self.url = url
        print 'New job:', url
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)


