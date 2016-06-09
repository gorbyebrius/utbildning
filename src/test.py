import time, threading
#from multiprocessing import Process

#import threading
#from threading import Thread
#import subprocess
#import os
#import threading
#from threading import Thread

class Hello_world(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.time = 0
        
    def run(self):
        while True:
            #print "one thread"
            time.sleep(1)
            self.time += 1
            
    def get_time(self):
        return self.time
    
#class Foo_bar:
#    def __init__(self):
#        print "Foo bar"
    
#    def foo_bar(self):
#        while True:
#            print "two thread"
#            time.sleep(1)
        


print "Start"
#p = multiprocessing.Process(target=time.sleep, args=(1000,))

a = Hello_world()
#a.daemon(True)
a.start()
print "Middle"
print a , a.is_alive()
time.sleep(5)
print a.get_time()
time.sleep(1)
print a.get_time()
time.sleep(3)
print a.get_time()
print "end"








