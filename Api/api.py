from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd
import requests
import json
from expanders import *
import settings
import tools
import middleware
import pandasTools

app = Flask(__name__)
api = Api(app)


class SingleEmployee(Resource):
    def get(self, emp_id):
        expanders = request.args.getlist('expand')
        rawData = middleware.getPendingEmployees([emp_id])
        pdData = pandasTools.formatDataframe(rawData)
        print(pdData)
        startExpanders(expanders,rawData,pdData)
        return rawData
        
class Employees(Resource):
    def get(self):                
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        expanders = request.args.getlist('expand')
        rawData = middleware.getEmployees(limit,offset)
        pdData = pandasTools.formatDataframe(rawData)
        print(pdData)
        startExpanders(expanders,rawData,pdData)    
        return rawData


api.add_resource(Employees, '/employees')
api.add_resource(SingleEmployee, '/employees/<emp_id>')

if __name__ == '__main__':
    settings.init()
    app.run(debug=True)