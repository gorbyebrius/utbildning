'''
Created on May 25, 2016

@author: gorbyebrius
'''

class Calculator(object):
    '''
    This class
    '''

    def __init__(self, color):
        '''
        Constructor
        '''
        self.color = color
        
        
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

lefteris_calculator = Calculator( "green" )

print str( lefteris_calculator.addition(10, 20) )
print "done..."
