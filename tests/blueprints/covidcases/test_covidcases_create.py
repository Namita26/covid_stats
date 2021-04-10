from app.blueprints.covid_cases.models.case import Case
from app.utils.file_utils import read_json


def teardown_module():
    Case.objects().delete()


def test_create(client):
    data = read_json("tests/seed_data/cases.json")[0]
    response = client.post("/v1/covid_cases", json=data)
    assert response.json.get("_id", None) is not None
    assert response.json.get("found_active_on", None) is not None
    assert response.json.get("location", None) is not None
    assert response.status_code == 201


def test_create_invalid_user_id(client):
    data = {
        "user_id": "Namita"  # user_id should be Int, no string.
    }
    response = client.post("/v1/covid_cases", json=data)
    assert response.status_code == 400


def test_it_should_return_400_and_created_object_if_extra_keys_provided(client):
    data = read_json("tests/seed_data/cases.json")[0]
    data["some_extra_filed"] = "Hi"
    response = client.post("/v1/covid_cases", json=data)
    assert response.status_code == 400


def test_duplicate_case_registration(client):
    data = read_json("tests/seed_data/cases.json")[0]
    response = client.post("/v1/covid_cases", json=data)
    assert response.status_code == 400
