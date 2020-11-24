import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_number_between(self) :
        n=0
        for d in data : 
            if d>3 and d<7 : n = n + 1
        self.assertTrue( numberBetween( data, 3, 7)==n, "Your function for calculating the number between is not working" )
        n=0
        for d in data : 
            if d>2 and d<5 : n = n + 1
        self.assertTrue( numberBetween( data, 2, 5)==n, "Your function for calculating the number between is not working" )
        n=0
        for d in data : 
            if d>6 and d<9 : n = n + 1
        self.assertTrue( numberBetween( data, 6, 9)==n, "Your function for calculating the number between is not working" )
