import pytest

from seasons import get_date, convert_to_min, minute_speller


def test_convert():
    assert convert_to_min(60) == 1
    assert convert_to_min(120) == 2
    

def test_error_date():
    with pytest.raises(ValueError):
        get_date("cat")
        get_date("01-01-1992")
        
        
def test_get_date():
    assert get_date("2024-05-16") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_date("2023-05-16") == "One million, fifty-two thousand, six hundred forty minutes"