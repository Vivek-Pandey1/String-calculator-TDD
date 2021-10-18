import pytest

from String import string_cal

def test_empty_string():
    result= string_cal("")
    assert result=="0"

def test_number_string():
    result= string_cal("1")
    assert result== 1

def test_sum_of_numbers():
    result= string_cal("1/2\n3;3")
    assert result== 9

def test_negative_number():
    result=string_cal("-8")
    assert result=="negatives not allowed -8"