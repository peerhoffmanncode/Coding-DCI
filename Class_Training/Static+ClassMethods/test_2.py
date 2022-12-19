from stuff import add, mul
import pytest


@pytest.fixture()
def something():
    return 5


def test_1(something):
    assert add(1, 1), 2


def test_2():
    assert mul(1, 1), 1
