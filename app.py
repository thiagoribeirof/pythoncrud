from flask import Flask, request,redirect, render_template
import sql

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method=='POST':
        print("post")
        employee_name = request.form.get("employee_name")
        employee_function = request.form.get("employee_function")
        print(employee_name, employee_function)
        sql.insert_employee(employee_name=employee_name, employee_function=employee_function)

    elif request.method=='GET':
        print('get')

    return render_template("index.html")

@app.route("/read.html", methods = ['POST', 'GET'])
def read():

    return render_template("read.html")