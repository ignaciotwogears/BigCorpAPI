from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd
import requests
import json
import expanders as xp
import settings
import tools
import middleware
import pandasTools

app = Flask(__name__)
api = Api(app)
settings.init()


class SingleEmployee(Resource):
    def get(self, emp_id):                
        tools.checkRequest(("expand",))
        try:            
            expanders = request.args.getlist('expand')
            data = middleware.getEmployeesByIds([emp_id])
            
            if len(data) == 0:
                abort(500, message= " can't connect to the Employees server")

            df = pandasTools.formatDataframe(data)
            print(df)
            xp.startExpanders(expanders,data,df)
            return data
        except:
            abort(500, message= "Ups something went wrong!")

        
class Employees(Resource):
    def get(self):
        tools.checkRequest(("limit","offset","expand"))
        try:            
            limit = int(request.args.get('limit'))
            offset = int(request.args.get('offset'))
            expanders = request.args.getlist('expand')
            data = middleware.getEmployees(limit,offset)

            if len(data) == 0:
                abort(500, message= " can't connect to the Employees server")

            df = pandasTools.formatDataframe(data)
            print(df)
            xp.startExpanders(expanders,data,df)    
            return data
        except:
            abort(500, message= "Ups something went wrong!")


api.add_resource(Employees, '/employees')
api.add_resource(SingleEmployee, '/employees/<emp_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=False)
    