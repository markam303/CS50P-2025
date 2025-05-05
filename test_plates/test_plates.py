import pytest
from plates import is_valid


def test_first_2_letters():
    assert is_valid("AA") == True
    assert is_valid("AAdid") == True
    assert is_valid("0Z0N") == False
    

def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABRACA") == True
    assert is_valid("ABRACAD") == False
    

def test_numbers():
    assert is_valid("AA007") == False
    assert is_valid("AA107") == True
    assert is_valid("AA1000") == False


def test_punctuations():
    assert is_valid("AA.!S") == False
    assert is_valid("AA 23") == False