from flask import request
from flask_restful import abort

def checkLimit(limit):
    if limit is None:
        limit = 100
    else:
        limit = int(limit)
    
    return limit

def checkOffset(offset):
    if offset is None:
        offset = 0
    else:
        offset = int(offset)
    return offset

def checkExpanders():
    
    allowedExpanders = ("manager","office","department","superdepartment")
    expanderList = request.args.getlist("expand")
    
    if len(expanderList) > 0:
        for e in expanderList:
            expander = e.split(".")
            if not all(i in allowedExpanders for i in expander):                        
                abort(400, message=f" invalid expander : {e}")


# Format the item to a corresct dict format
def formatedItem(item):
    ret = {}
    for i in item:   
        key = None

        for values in item[i]:
            key = values
            break
        
        value = item[i].get(key)
        if i == "department" or i == "office" or i == "manager":
            try:
                value = int(value)
            except Exception:
                value = None
        
        ret[i] = value
    return ret

# return the array without nulls
def formatLS(ls):
    cp = []
    for l in ls:
        try:
            cp.append(int(l))
        except Exception:
            pass
    return cp