import json

expected_single = {
    "id": 4,
    "city": "Chicago",
    "country": "United States",
    "address": "233 S Wacker Dr"
}

expected_listed = [
    {
        "id": 3,
        "city": "London",
        "country": "United Kingdom",
        "address": "32 London Bridge St"
    },
    {
        "id": 4,
        "city": "Chicago",
        "country": "United States",
        "address": "233 S Wacker Dr"
    }
]


def testSingleOffices(app, client):
    res = client.get('/offices/4')
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert isinstance(data,dict)
    assert data == expected_single


def testListedOffices(app, client):
    res = client.get('/offices?offset=2&limit=2')
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert isinstance(data,list)
    assert data == expected_listed