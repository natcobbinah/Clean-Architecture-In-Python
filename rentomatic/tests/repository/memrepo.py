import pytest

from rentomatic.domain.room import Room
from rentomatic.repository.memrepo import MemRepo


@pytest.fixture
def room_dicts():
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "size": 215,
            "price": 39,
            "longitude": -0.09998975,
            "latitude": 51.75436293,
        },
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "size": 405,
            "price": 66,
            "longitude": 0.18228006,
            "latitude": 51.74640997,
        },
        {
            "code": "913694c6-435a-4366-ba0d-da5334a611b2",
            "size": 56,
            "price": 60,
            "longitude": 0.27891577,
            "latitude": 51.45994069,
        },
        {
            "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "size": 93,
            "price": 48,
            "longitude": 0.33894476,
            "latitude": 51.39916678,
        },
    ]


def test_repository_list_without_parameters(room_dicts):
    repo = MemRepo(room_dicts)

    rooms = [Room.from_dict(i) for i in room_dicts]

    assert repo.list() == rooms


def test_repository_list_with_code_equal_filter(room_dicts):
    repo = MemRepo(room_dicts)

    rooms = repo.list(
        filters={
            "code__eq": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a"
        }
    )

    assert len(rooms) == 1
    assert rooms[0].code == "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a"

@pytest.mark.parametrize("price", [60, "60"])
def test_repository_list_with_price_equal_filter(room_dicts,price):
    repo = MemRepo(room_dicts)

    rooms = repo.list(filters={"price__eq": price})

    assert len(rooms) == 1
    assert rooms[0].code == "913694c6-435a-4366-ba0d-da5334a611b2"


def test_repository_list_with_price_less_than_filter(room_dicts, price):
    repo = MemRepo(room_dicts)

    rooms = repo.list(
        filters={
            "price__lt": price
        }
    )

    assert len(rooms) == 2 
    assert set([r.code for r in rooms]) == {
        "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "eed76e77-55c1-41ce-985d-ca49bf6c0585"
    }


def test_repository_list_with_price_between_filter(room_dicts):
    repo = MemRepo(room_dicts)

    rooms = repo.list(filters={
        "price__lt": 66, "price__gt": 48
    })

    assert len(rooms) == 1
    assert rooms[0].code == "913694c6-435a-4366-ba0d-da5334a611b2"