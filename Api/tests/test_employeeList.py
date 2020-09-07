import json

def testSimpleListedEmployee(app, client):
    res = client.get('/employees?limit=10&offset=26')
    assert res.status_code == 200
    data = json.loads(res.get_data())
    assert isinstance(data,list)
    assert len(data) == 10

    for item in data:
        assert isinstance(item,dict)
        assert isinstance(item["first"],str)
        assert isinstance(item["last"],str)
        assert isinstance(item["id"],int)

        if not item.get("manager") is  None:
            assert isinstance(item.get("manager"),int)


def testExpandedListedEmployee(app, client):
    res = client.get('employees?limit=10&offset=26&expand=department.superdepartment&expand=manager.manager.manager.manager')
    assert res.status_code == 200
    data = json.loads(res.get_data())
    assert isinstance(data,list)
    assert len(data) == 10

    depth = 4
    for item in data:
        assert isinstance(item,dict)
        assert isinstance(item["first"],str)
        assert isinstance(item["last"],str)
        assert isinstance(item["id"],int)
        
        if not item.get("office") is None:
            assert isinstance(item["office"],int)
        
        if not item.get("manager") is None:
            assert isinstance(item["manager"],dict)
            
            manager = item.get("manager")
            if not manager is None:
                assert isinstance(manager,dict)
                for d in range(depth):
                    manager = item["manager"].get("manager")
                    if not manager is  None:
                        assert isinstance(manager,dict)