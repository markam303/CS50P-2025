from twttr import shorten
import pytest
    

def test_text():
    assert shorten("twitter") == "twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_number():
    with pytest.raises(AttributeError):
        shorten(1)
        shorten(0)
        shorten(-1)
