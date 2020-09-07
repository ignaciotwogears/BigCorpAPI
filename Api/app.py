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

class SingleDepartment(Resource):
    def get(self, dept_id):
        tools.checkExpanders()
        expanders = request.args.getlist('expand')
        dept = []
        for d in settings.DEPARTAMETS:            
            if d["id"] == int(dept_id):
                dept = d
        
        xp.startExpanders(expanders,dept,None)
        return dept

class SingleEmployee(Resource):
    # Return an employee detail
    def get(self, emp_id):
        # Makes sure that the expanders are correct                
        tools.checkExpanders()
        try:            
            expanders = request.args.getlist('expand')
            data = middleware.getEmployeesByIds([emp_id])
            
            if len(data) == 0:
                abort(500, message= " can't connect to the Employees server")

            # Turns the list of dicts to a pandas dataframe
            df = pandasTools.formatDataframe(data)
            
            # Launch the expander iteration
            xp.startExpanders(expanders,data,df)
            return data
        except:
            abort(500, message= "Ups something went wrong!")

        
class Employees(Resource):
    # Return an employees list
    def get(self):
        # Makes sure that the request are correct
        tools.checkExpanders()
        limit = tools.checkLimit(request.args.get('limit'))
        offset = tools.checkOffset(request.args.get('offset'))
        expanders = request.args.getlist('expand')
        
        try:                
            data = middleware.getEmployees(limit,offset)

            if len(data) == 0:
                abort(500, message= " can't connect to the Employees server")
             
            # Turns the list of dicts to a pandas dataframe
            df = pandasTools.formatDataframe(data)
            
            # Launch the expander iteration
            xp.startExpanders(expanders,data,df)    
            return data
        except:
            abort(500, message= "Ups something went wrong!")


api.add_resource(Employees, '/employees')
api.add_resource(SingleEmployee, '/employees/<emp_id>')
api.add_resource(SingleDepartment, '/departments/<dept_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
    