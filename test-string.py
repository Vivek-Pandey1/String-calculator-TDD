import pytest

from String import string_cal

def test_empty_string():
    result= string_cal("")
    assert result==""

def test_number_string():
    result= string_cal("1")
    assert result=="1"
