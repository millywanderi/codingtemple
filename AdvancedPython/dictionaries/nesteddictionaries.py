#!/usr/bin/env python3

# Create a dictionary that contain three dictionaries
myfamily = {
    "child1": {
        "name": "Steve",
        "year": 2005
    },
    "child2": {
        "name":"Kylie",
        "year": 2015
    },
    "child3": {
        "name": "Lyle",
        "year": 2019
    }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will 
#contain the other three dictionaries
child1 = {
    "name": "Steve",
    "year": 2005
}
child2 = {
    "name": "Kylie",
    "year": 2015
}
child3 = {
    "name": "Lyle",
    "year": 2019
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# Print the name of child 2
myfamily = {
    "child1": {
    "name": "Steve",
    "year": 2005
    },
    "child2": {
        "name": "Kylie",
        "year": 2015
    },
    "child3": {
        "name": "Lyle",
        "year": 2019
    }
}
print(myfamily["child2"]["name"])
