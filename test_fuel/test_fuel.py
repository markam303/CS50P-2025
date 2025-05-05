import pytest
from fuel import convert, gauge


def test_convert():
    ...

def test_gauge():
    assert gauge(25) == f"25%"