import pytest
from working import convert


def test_fullinput():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_nominutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"