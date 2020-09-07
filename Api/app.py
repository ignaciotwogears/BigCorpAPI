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
        try:
            expanders = request.args.getlist('expand')
            dept = {}
            for d in settings.DEPARTAMETS:            
                if d["id"] == int(dept_id):
                    dept = d
            
            xp.startExpanders(expanders,dept,None)
            return dept
        except:
            abort(500, message= "Ups something went wrong!")

class ListDepartment(Resource):
    def get(self):
        
        tools.checkExpanders()
        try:            
            limit = tools.checkLimit(request.args.get('limit'))
            offset = tools.checkOffset(request.args.get('offset'))
            expanders = request.args.getlist('expand')
            depts = settings.DEPARTAMETS[offset : offset + limit]
            
            for d in depts:
                xp.startExpanders(expanders,d,None)
            
            return depts
        except:
            abort(500, message= "Ups something went wrong!")



class SingleOffice(Resource):
    def get(self, ofi_id):
        try:
            office = {}  
            for o in settings.OFFICES:            
                if o["id"] == int(ofi_id):
                    office = o
            return office
        except:
            abort(500, message= "Ups something went wrong!")


class ListOffice(Resource):
    def get(self):
        try:      
            limit = tools.checkLimit(request.args.get('limit'))
            offset = tools.checkOffset(request.args.get('offset'))
            offices = settings.OFFICES[offset : offset + limit]
            return offices
        except:
            abort(500, message= "Ups something went wrong!")


class SingleEmployee(Resource):
    # Return an employee detail
    def get(self, emp_id):
        # Makes sure that the expanders are correct                
        tools.checkExpanders()
        try:            
            expanders = request.args.getlist('expand')
            data = middleware.getEmployeesByIds([emp_id])
            
            if len(data) == 0:
                abort(500, message= " Employees Server Not available")

            # Turns the list of dicts to a pandas dataframe
            df = pandasTools.formatDataframe(data)
            
            # Launch the expander iteration
            xp.startExpanders(expanders,data,df)
            return data
        except:
            abort(500, message= "Ups something went wrong!")

        
class ListEmployees(Resource):
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
                abort(500, message= " Employees Server Not available")
             
            # Turns the list of dicts to a pandas dataframe
            df = pandasTools.formatDataframe(data)
            
            # Launch the expander iteration
            xp.startExpanders(expanders,data,df)    
            return data
        except:
            abort(500, message= "Ups something went wrong!")


api.add_resource(ListEmployees, '/employees')
api.add_resource(SingleEmployee, '/employees/<emp_id>')
api.add_resource(ListDepartment, '/departments')
api.add_resource(SingleDepartment, '/departments/<dept_id>')
api.add_resource(ListOffice, '/offices')
api.add_resource(SingleOffice, '/offices/<ofi_id>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
    