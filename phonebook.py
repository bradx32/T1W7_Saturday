# inbuilt python module to allow for nicer printing structure in vertical lines rather than long horizontal text.
from pprint import pprint

"""
[
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "1241",
            "mobile: "412 123 123"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Brisbane",
        "phone": {
            "home": "123123"
            "mobile: "438 123 123"
        }
    }
]
"""

phonebook = [
    {
        "name": "John Smith",
        "address": "Sydney",
        "phone": {
            "home": "1241",
            "mobile": "412 123 123"
        }
    },
    {
        "name": "Jane Doe",
        "address": "Brisbane",
        "phone": {
            "home": "123123",
            "mobile": "438 123 123"
        }
    }
]

pprint(phonebook)

name = input("Enter name: ")
address = input("Enter address: ")
home = input("Enter home:")
mobile = input("Enter mobile: ")

person_to_add = {
    "name": name,
    "address": address,
    "phone": {
        "home": home,
        "mobile": mobile
    }
}

phonebook.append(person_to_add)

pprint(phonebook)

number_to_find = input("Enter a number to find: ")

def find_number(number_to_find):
    for phone_entry in phonebook:
        for number_key in phone_entry["phone"]:
            if (number_to_find == phone_entry["phone"][number_key]):
                print("Number found")
                print(phone_entry["name"])
                return
    print("Number not found")

find_number(number_to_find)

