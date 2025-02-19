#2 If/else statement

import numpy as np
import pytest
from functions import goldilocks

def test_goldilocks(capsys):
       BedSize = 135 
       #call the function
       goldilocks(BedSize)
       captured = capsys.readroutter()
       expected_output = "Too small!\n"
       assert captured.out == expected_output



