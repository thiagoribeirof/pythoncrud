import mysql.connector

PASSWORD = 'root'
DATABASE = 'PythonCRUD'

def create_connection():
    cnx = mysql.connector.connect(user='root', password=PASSWORD,
                              host='127.0.0.1',
                              database=DATABASE)
    return cnx



def insert_employee(employee_name, employee_function):
    cnx = create_connection()
    cursor = cnx.cursor()
    add_query = "INSERT INTO employees(employee_name, employee_function) VALUES(%s, %s)"
    values = (employee_name, employee_function)
    try:
        cursor.execute(add_query, values)
        cnx.commit()
    except Exception as exc:
        print(exc)
    
    cursor.close()
    cnx.close()


class Employee:
    def __init__(self, name, function, id):
        self.name = name
        self.function = function
        self.id = id

def read_employees():
    cnx = create_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM employees"
    cursor.execute(query)
    results = cursor.fetchall()
    all_employees = []
    for employee in results:
        id = employee[0]
        name = employee[1]
        function = employee[2]
        newEmployee = Employee(id=id, name=name, function=function)
        all_employees.append(newEmployee)
    cursor.close()
    cnx.close()
    return all_employees


