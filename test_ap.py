def test_ab():
    assert 5==7
    # def test_ab():
#     assert 5==7

import pytest_
@pytest.fixtures
def sample():
    return[2,3,5]
def test_s(sample):
    assert sum(sample)==10