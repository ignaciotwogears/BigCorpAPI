from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd
import requests
import json


app = Flask(__name__)
api = Api(app)


DEPARTAMETS = {}
OFFICES = {}

def readJson(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

def loadResources():
    global DEPARTAMETS
    global OFFICES

    DEPARTAMETS = readJson("./resources/departments.json")
    OFFICES = readJson("./resources/offices.json")


def getEmployees(limit,offset):
    r = requests.get(f'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit={limit}&offset={offset}')
    res = r.json()
    return res


def getPendingEmployees(ls):
    
    glue = "&id="
    ids = glue.join([str(i) for i in ls])
    req = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=" +ids
    print(req)
    r = requests.get(req)
    return r.json()
    
    
def addOffice(obj):
    for F in OFFICES:
        if obj['office'] == F['id']:
            obj['office'] = F

def addDepartment(obj,tile):
    for o in obj:        
        for D in DEPARTAMETS:                        
            if o['department'] == D['id']:
                o['department'] = D                
                if len(tile) > 0:
                    expand(tile,o['department'],None)


def addSuperDepartment(obj,tile):    
    for D in DEPARTAMETS:    
        if obj['superdepartment'] == D['id']:
            obj['superdepartment'] = D
            if len(tile) > 0:
                    expand(tile,obj['superdepartment'],None)


def addManager(obj,tile,actualKey,pdData):

    for o in obj:
        manager = o.get('manager')
        findedItem = pdData.query(f'id == {manager}')
        if not findedItem.empty:
            findedItem = findedItem.to_dict()
            o['manager']  = formatedItem(findedItem)
             
            if len(tile) > 0: 
                expand(tile,[o['manager']],pdData)
        

def expand(keys,obj,template):
    actualKey = keys[0]
    tile = keys[1:]

    if (actualKey == "manager"):
        addManager(obj,tile,actualKey,template)
    
    elif(actualKey == "department"):
        addDepartment(obj,tile)

    elif (actualKey == "superdepartment"):
        addSuperDepartment(obj,tile)
    
    elif (actualKey == "office"):
        addOffice(obj[0])


def startExpanders(expanders,response,pdData):
    for exp in expanders:
        expand(exp.split("."),response,pdData)



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

def getOrphanFrames(df):
    
    ids = df['id']
    orphans = df.query('manager not in @ids')['manager']
    ls = [p for p in orphans]
    formatLs = formatLS(ls)
    ls = list(dict.fromkeys(formatLs))
    return ls


def formatDataframe(df):
    ls = getOrphanFrames(df)
    while(len(ls) >0):
        pendingData = getPendingEmployees(ls)

        pdFrame = pd.DataFrame.from_dict(pendingData)
        frames = [df, pdFrame]
        df = pd.concat(frames)
        ls = getOrphanFrames(df)
    
    return df



class SingleEmployee(Resource):
    def get(self, emp_id):
        expanders = request.args.getlist('expand')
        rawData = getPendingEmployees([emp_id])
        pdData = pd.DataFrame.from_dict(rawData)
        pdData = formatDataframe(pdData)
        print(pdData)
        startExpanders(expanders,rawData,pdData)
        return rawData
        
class Employees(Resource):
    def get(self):
                
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        expanders = request.args.getlist('expand')
        rawData = getEmployees(limit,offset)
        
        pdData = pd.DataFrame.from_dict(rawData)
        pdData = formatDataframe(pdData)
        print(pdData)
        startExpanders(expanders,rawData,pdData)    
        return rawData


api.add_resource(Employees, '/employees')
api.add_resource(SingleEmployee, '/employees/<emp_id>')

if __name__ == '__main__':
    loadResources()
    app.run(debug=True)