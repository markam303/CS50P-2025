import pytest
from fuel import convert, gauge


def test_convert():
    assert test_convert("1/4") == 25

def test_gauge():
    assert gauge(1) == "E"