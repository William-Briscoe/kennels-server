import sqlite3
import json
from .models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

#grabs all employees
def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name AS location_name,
            l.address AS location_address
        FROM Employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees

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