import pytest
from py_ds.data import fun

def test_hello():
    c = fun(1, 2)
    assert 4==c