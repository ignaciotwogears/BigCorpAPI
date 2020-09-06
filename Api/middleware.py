import requests

def getEmployees(limit,offset):
    r = requests.get(f'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit={limit}&offset={offset}')
    res = r.json()
    return res


def getEmployeesByIds(ls):
    
    glue = "&id="
    ids = glue.join([str(i) for i in ls])
    req = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=" +ids
    print(req)
    r = requests.get(req)
    return r.json()
    
    