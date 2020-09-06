
import json

def readJson(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

def loadResources():
    global DEPARTAMETS
    global OFFICES

    DEPARTAMETS = readJson("./resources/departments.json")
    OFFICES = readJson("./resources/offices.json")


def init():
    global DEPARTAMETS
    global OFFICES
    DEPARTAMETS = {}
    OFFICES = {}
    loadResources()
