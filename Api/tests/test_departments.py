import json

expected_fixed = {
    "id": 9,
    "name": "Sales Development",
    "superdepartment": {
        "id": 6,
        "name": "Outbound Sales",
        "superdepartment": {
            "id": 1,
            "name": "Sales",
            "superdepartment": None
        }
    }
}

def testSingleDepartment(app, client):
    res = client.get('/departments/9?expand=superdepartment.superdepartment')
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert isinstance(data,dict)
    assert data == expected_fixed