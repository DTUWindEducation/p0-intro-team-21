#clean_pitch

import numpy as np
import pytest
from functions import clean_pitch


#Logical operators
def test_clean_pitch():
      pitch_angles = [-1,2,6,95]
      status_signals = [1,0,0,0]
      assert clean_pitch(pitch_angles,status_signals) == [-999,2,6,95]

if __name__ == '__main__':
    test_clean_pitch()