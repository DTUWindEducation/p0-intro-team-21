"""Check some of the functions in arithmetic.
"""
import numpy as np
import pytest

from test_arithmetic_extras import square

def test_square_integer():
    """Test that the square function returns the correct value for an
    integer input."""
    # given
    x = 3.4
    y_theo = 4
    # when
    y = square(x)
    # then
    assert y == y_theo


# code to execute only if Python is executed directly on this module,
# NOT on import
if __name__ == '__main__':
    test_square_integer()

