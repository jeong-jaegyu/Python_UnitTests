import pytest

from testdemo.testdemo import print_hi


def test_demo():
    print_hi("hi")


@pytest.mark.skip(reason='reason here')
def test_skip():
    pass


@pytest.mark.xfail
def test_failure():
    assert 1 == 2


# Fails if error not raised
def test_exp_err():
    with pytest.raises(TypeError):
        return "hello"/4
