from flask import Flask, request,redirect, render_template, url_for
import sql

app = Flask(__name__)
app.secret_key = 'fwkf434526@g'

@app.route("/", methods = ['POST', 'GET'])
def index():

    return render_template("index.html")


@app.route("/insert", methods = ['POST', 'GET'])
def insert():
    if request.method=='POST':
        print("post")
        try:
            employee_name = request.form.get("employee_name")
            employee_function = request.form.get("employee_function")
            print(employee_name, employee_function)
            sql.insert_employee(employee_name=employee_name, employee_function=employee_function)

        except Exception as  exc:
            print(exc)
        else:
            return redirect(url_for('success'))

    elif request.method=='GET':
        print('get')
    return redirect(url_for('index'))

    
@app.route("/read", methods = ['POST', 'GET'])
def read():
    all_employees = sql.read_employees()
    return render_template("read.html", all_employees = all_employees)

@app.route('/success')
def success():

    return render_template('success.html')

