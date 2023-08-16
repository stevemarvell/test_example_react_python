import os
import pytest

from infrastructure.repositories.greeting_repository_array import GreetingRepositoryArray


# uses test data file in _this_ local directory
@pytest.fixture
def repo():
    return GreetingRepositoryArray(f'{os.path.dirname(__file__)}/test_array_data.json')


def test_array_known_name(repo):
    assert repo.get_greeting_by_name("Fred") == "Hiya"


def test_array_case(repo):
    assert repo.get_greeting_by_name("fred") == "Hiya"


def test_array_unknown_name(repo):
    assert repo.get_greeting_by_name("alice") == "Hi ho"
