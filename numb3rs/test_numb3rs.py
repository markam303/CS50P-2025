import pytest

from numb3rs import validate


def test_string():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
     
def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255") == False
    assert validate("256.4.5.2") == False