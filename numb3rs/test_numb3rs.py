import pytest

from numb3rs import validate


def test_string():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
     
def test_boundaries():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("12.12.11.12") == True

def test_wrong():
    assert validate("255") == False
    assert validate("256.4.5.2") == False
    assert validate("-1") == False
    assert validate("300.300.300.300") == False
    assert validate("10.10.01.10") == False