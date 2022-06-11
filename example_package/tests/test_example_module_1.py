import numpy as np
import numpy.testing as npt
import pytest
from example_module_1 import example1 as ex11


def test_module_1_example_1_add_one():
    "Check the result"
    computed = ex11.add_one(4.2)
    reference = 5.2
    npt.assert_almost_equal(computed, reference, decimal=12)
