import pytest
pytestmark = pytest.mark.login

def add(a,b):
    return a+b

def test_m1():
    a=4
    b=3

    # assert a == b, "Test failed as a is not equal to b"
    r1=add(a,b)
    assert r1== 7, "Test failed as a is not equal to b"


def test_m2():
    a,b=5,5
    assert a == b


