from flask import Flask, request,redirect, render_template, url_for
import sql

app = Flask(__name__) #intializin Flask
app.secret_key = 'fwkf434526@g'

@app.route("/", methods = ['POST', 'GET'])
def index():

    return render_template("index.html")


@app.route("/insert", methods = ['POST', 'GET'])
def insert():
    if request.method=='POST':
        print("post")
        try:
            employee_name = request.form.get("employee_name") #getting employee info from the form
            employee_function = request.form.get("employee_function")
            print(employee_name, employee_function)
            sql.insert_employee(employee_name=employee_name, employee_function=employee_function) #calls the insert_employee function

        except Exception as  exc:
            print(exc)
        else:
            return redirect(url_for('success'))

    elif request.method=='GET':
        print('get')
    return redirect(url_for('index'))

    
@app.route("/read", methods = ['POST', 'GET'])
def read():
    all_employees = sql.read_employees() #call to read_employees function
    return render_template("read.html", all_employees = all_employees)

@app.route('/success')
def success():

    return render_template('success.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    print(request.method)
    if request.method=="POST":
        employee_id = int(request.form.get("hidden_id"))
        employeeObj = sql.read_employees(employee_id)[0]
    return render_template('edit.html', employeeObj=employeeObj)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=="POST":
        employee_name = request.form.get("new_name")
        employee_function = request.form.get("new_function")
        employee_id = request.form.get("hidden_id")
        try:
            sql.update_employee(employee_id, employee_name, employee_function)
            template = 'success.html'
        except Exception as exc:
            print(exc)
            template = 'fail.html'

    return render_template(template)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method=="POST":
        id = request.form.get("hidden_id_del")
        try:
            sql.delete_employee(id)
            template = 'success.html'
        except Exception as exc:
            print(exc)
            template = 'fail.html'
        
    return render_template(template)