import pytest
from um import count


def test_single_um():
    assert count("um") == 1


def test_punctuation_um():
    assert count("um?") == 1
    

def test_uppercase_um():
    assert count("Um, thanks for the album.") == 1
    

def test_dotdotdot_um():
    assert count("Um, thanks, um...") == 2
    

def test_inside_um():
    assert count("yummy") == 0
    assert count("yum") == 0