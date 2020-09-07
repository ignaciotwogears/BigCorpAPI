import json


def testSingleEmployee(app, client):
    res = client.get('/employees/16')
    assert res.status_code == 200
    data = json.loads(res.get_data())
    assert isinstance(data,list)
    for item in data:
        assert isinstance(item,dict)
        assert isinstance(item["first"],str)
        assert isinstance(item["last"],str)
        assert isinstance(item["id"],int)
        assert isinstance(item["manager"],int)


def testSingleEmployeeExpanded(app, client):
    res = client.get('/employees/16?expand=manager.manager.office&expand=department.superdepartment')
    assert res.status_code == 200
    data = json.loads(res.get_data())
    assert isinstance(data,list)
    depth = 2
    for item in data:
        assert isinstance(item,dict)
        assert isinstance(item["first"],str)
        assert isinstance(item["last"],str)
        assert isinstance(item["id"],int)
        assert isinstance(item["office"],int)
        
        if item["manager"] is not None:
            assert isinstance(item["manager"],dict)
            for d in range(depth):
                manager = item["manager"].get("manager")
                if manager is not None:
                    assert isinstance(manager,dict)

