import pytest
import functions_pytest as fp

def test_season():
    assert fp.season('snow') == 'winter'
    assert fp.season('sun') == 'summer'
    assert fp.season('asdasdsa') is None

def test_range_list():
    assert 6 in fp.range_list(5, 10)
    assert 150 in fp.range_list(10, 200)
    assert 1500 in fp.range_list(10, 2000)

def division():
    assert fft.div(20, 5) == 4
    assert fft.div(100, 4) == 25
    assert fft.div(1000, 10) == 100