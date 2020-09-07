from flask import request
from flask_restful import abort

def checkRequest(tags):
    
    allowedExpanders = ("manager","office","department","superdepartment")
    
    for t in tags:
        if t == "expand":
            expanderList = request.args.getlist(t)
            if len(expanderList) > 0:
                for e in expanderList:
                    expander = e.split(".")
                    if not all(i in allowedExpanders for i in expander):                        
                        abort(400, message=f" invalid expander : {e}")

        elif request.args.get(t) is None:
            print("abort : " , t)
            abort(400, message=f"{t} argument is needed")


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


def formatLS(ls):
    cp = []
    for l in ls:
        try:
            cp.append(int(l))
        except Exception:
            pass
    return cp