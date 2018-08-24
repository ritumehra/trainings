# https://dzone.com/articles/restful-web-services-with-python-flask
import json
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

empDB=[
    {
        'id': '101',
        'name': 'Saravanan S',
        'title': 'Technical Leader'
    },
    {
        'id': '201',
        'name': 'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
]


@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    return jsonify({'emp':usr})


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):

    print(request.json)
    print(request.headers)
    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})


@app.route('/empdb/employee',methods=['POST'])
def createEmp():

    print(type(request.json))
    dat = {
        'id':request.json['id'],
        'name':request.json['name'],
        'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)


@app.route('/emp/post',methods=['POST'])
def createEmp_new():

    request.get_data()
    data_dict = json.loads(request.data)
    print('Request Paylosd: {}'.format(data_dict))

    dat = {
        'id':data_dict['id'],
        'name':data_dict['name'],
        'title':data_dict['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        # abort(404)
        pass
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


@app.route('/',methods=['GET'])
def homepage():

    return jsonify({'response':'Welcome to the Training Service'})


if __name__ == '__main__':
    app.run()