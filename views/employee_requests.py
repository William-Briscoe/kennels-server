import sqlite3
import json
from .models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

#grabs all employees
def get_all_employees():
    #will return all objects in EMPLOYEES
    return EMPLOYEES


#grabs specific employee
def get_single_employee(id):
    #variable to later hold the returned employee
    requested_employee = None

    #iterates through EMPLOYEES list
    for employee in EMPLOYEES:
        #When a match is made requested_employee is set equal to match
        if employee[id] == id:
            requested_employee = employee
    #Returns requested_employee
    return requested_employee


def get_employee_by_location(location_id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #SQL query
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)
    
    return employees