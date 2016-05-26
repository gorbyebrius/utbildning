'''
Created on May 25, 2016

@author: gorbyebrius
'''

import datetime

class Naive_fibonacci(object):
    def __init__(self, stop_at):
        self.stop_at = stop_at
        
    def calculate(self):
        x=0
        y=1
        # print str(x) + "  " + str(y) + " ",
        # for i in range(1, self.stop_at):
        while True:
            res = x + y
            if res > self.stop_at:
                return res 
                break
            #print str(res) + " ",
            x = y
            y = res

class Recursive_fibonacci(object):
    def __init__(self, stop_at):
        self.stop_at = stop_at
        
    def calculate(self, x, y):
        #print str(x) + " ",
        res = x + y
        if y < self.stop_at:
            result = self.calculate(y, res)
            return result
        else:
            return x
        
class Recursive_fibonacci_2(object):
    def __init__(self, stop_at):
        self.stop_at = stop_at
#         
    def calculate_helper(self, n):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        #summ = 
        
        #print n
        
        #print summ
        
        return self.calculate_helper( n - 1 ) + self.calculate_helper( n - 2 )
#     
    #def calculate(self):
        #for i in range(self.stop_at):
        #    print str(self.calculate_helper(i))
    #    reurn self.calculate_helper(self.stop_at)    


naive_fibonacci = Naive_fibonacci(200)
print ""
print "Naive Output:"     
a = datetime.datetime.now()
result = naive_fibonacci.calculate()
b = datetime.datetime.now()
print "Result: " + str(result)
print "Time: " + str(b-a)

recursive_fibonacci = Recursive_fibonacci(300)
print ""
print "Recursive Output:"
a = datetime.datetime.now()
result = recursive_fibonacci.calculate(0, 1)
b = datetime.datetime.now()
print "Result: " + str(result)
print "Time: " + str(b-a)

recursive_fibonacci_2 = Recursive_fibonacci_2(13)   
print ""
print "Recursive 2 Output:"
a = datetime.datetime.now()
result = recursive_fibonacci_2.calculate_helper(13)
b = datetime.datetime.now()
print "Result: " + str(result)
print "Time: " + str(b-a)
