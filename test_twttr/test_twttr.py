from twttr import shorten
import pytest
    

def test_vowels():
    assert shorten("twitter") == "twttr"
    
    
def test_consonants_only():    
    assert shorten("CS50") == "CS50"
    
    
def test_omitting_punctuation():
    assert shorten("what's your name?") == "wht's yr nm?"


def test_omitting_numbers():
    ...


def test_all_uppercase():
    ...


def test_lowercase_vowels():
    ...


def test_capitalized_vowel():
    ...


def test_integers():
    with pytest.raises(AttributeError):
        shorten(1)
        shorten(0)
        shorten(-1)