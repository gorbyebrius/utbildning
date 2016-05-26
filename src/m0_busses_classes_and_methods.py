import shutil
import os
import SimpleHTTPServer
import SocketServer
#import concurrent.futures


'''
Created on May 26, 2016

@author: gorbyebrius
'''

class Buss_Factory(object):
    def __init__(self):
        website_directory="/tmp/python_busses"
        if not os.path.exists(website_directory):
            os.makedirs(website_directory)
        
        
        
        
    
    #def build(self):
        


class Buss(object):
    '''
    classdocs
    '''

    def __init__(self, color):
        '''
        Constructor
        '''
        website_directory="/tmp/python_busses"
            
        
        self.color = color
        filename_source = "/home/gorbyebrius/git/utbildning/resources/buss-" + color + ".png"
        filename_destination = website_directory + "/buss-" + color + ".png"
        shutil.copy(filename_source, filename_destination)

#buss_factory = Buss_Factory
#buss_factory.
executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 8000), Handler)
httpd.serve_forever()
print "hello"    