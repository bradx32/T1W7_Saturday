# Non-primitive Data Types

# List - collection of data - mutable (changeable) - indexed

numbers = [12, 32, 2, 4, 56, 78]
#          0    1  2  3  4   5 (these are their index numbers)

print(numbers)
print(numbers[4])

# add a number to end of list with append below
numbers.append(12)
print(numbers)

numbers[1] = 25
print(numbers)



# Tuples - collection of data or multiple pieces of information - immutable (unchangeable) - indexed
# for example: days, calandar, birthdays

days = ("Monday", "Tuesday", "Wednesday")
# index:   0         1            2

print(days)
print(days[1])

# days[2] = "Friday"   - Cannot do this
#  days.append("Friday")  - Cannot do this



# Sets - collection of data - mutable (changeable) - not indexed - no repeated items

names = {"John", "Jane", "Mike"}

print(names)

# cannot append as it is not indexed, so you add a name to the random 'set' list
names.add("Smith")
print(names)

names.remove("John")
print(names)

names.add("Jane")
print(names)

a = { 5, 3, 1, 2, 4} # { 1, 2, 3, 4, 5}
b = { 5, 7, 8, 4, 6} # { 4, 5, 6, 7, 8}


# below exercise is based off a venn-diagram made on draw.io
# combines the set a variable with b and doesn't give duplicates
u = a.union(b) # b.union(a)
print(u)

# gives result of a and b variables with the duplicate numbers
i = a.intersection(b) # b.intersection(a)
print(i)

# difference of a and b "dab" = a - b
dab = a.difference(b) # A - B
print(dab)

dba = b.difference(a) # B - A
print(dba)

# checks to see if 2 or 10 is 'in' the set variable a
print(2 in a)
print(10 in a)

for number in a:
    print(number)


# Dictionary - collection of data - mutable (changeable) - keyed - key value pair (meaning "GPU": "RTX3070")

person1 = {
    "name": "John",
    "surname": "Smith",
    "age": 32
}

print(person1)
print(person1["name"])
print(person1.get("name"))

# use .get method to see if "phone" is in the person1 dictionary without crashing the program like the below comment will 
# print(person1["phone"])
print(person1.get("phone", "No phone number provided")) # 2nd argument (no phone number provided) prints if the "phone" value does not exist

person1["address"] = "Melbourne"
print(person1)

person1["age"] = 33
print(person1)

# to remove any key value use .pop
person1.pop("surname")
print(person1)

print("Loop started here: \n")

# Loop to each key value pair
for key in person1:
    print(f"key: {key}") # prints the actual key names
    print(f"Value: {person1[key]}") # prints the key values

persons = [
    {
        "name": "Person1",
        "address": "Sydney",
        "phone": "[12412421, 124152123]"
    },
    {
    
        "name": "Person2",
        "address": "Perth",
        "phone": {
            "home": "12414",
            "mobile": "15412421"
        }
    },
    {
        "name": "Person3",
        "address": "Hobart"
    }
]

print(persons)
# you can also print certain areas as they are indexed
