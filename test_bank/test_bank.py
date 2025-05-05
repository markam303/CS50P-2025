import pytest
from bank import value


def test_hello():
    assert value("hello") == 0

    

def test_different():
    assert("what's up") == 100


def test_first():
    assert("hey") == 20
    assert("hiho") == 20