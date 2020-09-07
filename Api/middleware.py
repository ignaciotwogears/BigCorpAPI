import requests

def getEmployees(limit,offset):
    try:
        r = requests.get(f'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit={limit}&offset={offset}')
        res = r.json()
        return res
    except:
        return []


def getEmployeesByIds(ls):
    try:
        glue = "&id="
        ids = glue.join([str(i) for i in ls])
        req = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=" +ids
        r = requests.get(req)
        return r.json()
    except:
        return []
    
    
    