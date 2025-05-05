import pytest
from fuel import convert, gauge


def test_convert():
    assert test_convert("1/4") == 25
    assert test_convert("1/2") == 50

def test_gauge_boundaries():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(101) == "F"
    
def test_gauge():
    assert gauge(25) == f"25%"
    
def test_gauge_error():
    with pytest.raises(ValueError, ZeroDivisionError):
        gauge("cat/dog")
        gauge("1/0")
        gauge("catdog")
        