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
