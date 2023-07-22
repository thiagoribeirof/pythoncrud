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

def read_employees(id=None): #default value is None. If an ID is given, it searchs for the ID.
    cnx = create_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM employees"
    if(id): #if ID is given, it's True.
        query = query + " WHERE employee_id = "+str(id)+";"
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

def update_employee(id, name, function):
    cnx = create_connection()
    cursor = cnx.cursor()
    values = (name, function, id)
    query = "UPDATE employees SET employee_name = %s, employee_function = %s WHERE employee_id = %s"
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()

def delete_employee(id):
    cnx = create_connection()
    cursor = cnx.cursor()
    query = "DELETE FROM employees WHERE employee_id = '%d'" % (int(id))
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()