LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

#grabs all locations
def get_all_locations():
    #will return all objects in LOCATIONS
    return LOCATIONS


#grabs specific location
def get_single_location(id):
    #variable to later hold the returned location
    requested_location = None

    #iterates through LOCATIONS list
    for location in LOCATIONS:
        #When a match is made requested_location is set equal to match
        if location[id] == id:
            requested_location = location
    #Returns requested_location
    return requested_location


def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location
