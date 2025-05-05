import pytest
from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    

def test_different():
    assert value("what's up") == 100
    assert value("Great") == 100


def test_first():
    assert value("hey") == 20
    assert value("Hiho") == 20