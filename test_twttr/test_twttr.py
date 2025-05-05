from twttr import shorten
import pytest
    

def test_vowels():
    assert shorten("twitter") == "twttr"
    
    
def test_consonants_only():    
    assert shorten("CSS") == "CSS"
    
    
def test_omitting_punctuation():
    assert shorten("what's your name?") == "wht's yr nm?"
    assert shorten("hello, my name is Charlie.") == "hello, my name is Charlie."


def test_omitting_numbers():
    assert shorten("CS50") == "CS50"


def test_all_uppercase():
    assert shorten("DDDDDD") == "DDDDDD"


def test_lowercase_vowels():
    assert shorten("AssemblE") == "AssemblE"


def test_capitalized_vowel():
    ...


def test_integers():
    with pytest.raises(AttributeError):
        shorten(1)
        shorten(0)
        shorten(-1)