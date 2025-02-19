#Fibonacci_test

import numpy as np
import pytest
from functions import fibonacci_stop


#test with a standar integer
def test_fibonacci():
      fibonacci_numbers = [1,1,2,3,5,8,13,21]
      
      assert fibonacci_stop(30) == fibonacci_numbers

if __name__ == '__main__':
    test_fibonacci()