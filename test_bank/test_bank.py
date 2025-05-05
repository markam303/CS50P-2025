import pytest
from bank import value


def test_hello():
    assert value("hello") == 0
    

def test_different():
    assert value("what's up") == 100


def test_first():
    assert value("hey") == 20
    assert value("hiho") == 20