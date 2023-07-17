CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

#grabs all customers
def get_all_customers():
    #will return all objects in CUSTOMERS
    return CUSTOMERS


#grabs specific customer
def get_single_customer(id):
    #variable to later hold the returned customer
    requested_customer = None

    #iterates through CUSTOMERS list
    for customer in CUSTOMERS:
        #When a match is made requested_customer is set equal to match
        if customer[id] == id:
            requested_customer = customer
    #Returns requested_customer
    return requested_customer
