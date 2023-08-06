import json

json_string = '''{
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": false,
    "hobbies": null
}'''

json_object = json.loads(json_string)

print(json_object)
print(type(json_string))
print(type(json_object))

assert json_object["admin"] == False
assert json_object["address"]["city"] == "Gwenborough"

json_object_2nd = {
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": False,
    "hobbies": None
}

json_string_2nd = json.dumps(json_object_2nd, indent=2)
# print(json_string_2nd)
print(type(json_string_2nd))