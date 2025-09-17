# DICTIONARY -> SIMILAR CONCEPT TO MAP IN JAVA
#   Where it holds 2 parametrs one is key another one is value
#   keys are stored using hashing, so No duplicate keys allowed you can assume ike key is an data type of SET
#   Keys must be immutable types (e.g., int, str, tuple).
#   list or dict cannot be used as keys  :: NOTE SET ALSO CANNOT BE ADDED AS KEY
#   Values → can be any object (mutable or immutable).
#   You can update/overwrite values using the key, Multiple keys can point to the same value.

#   EXAMPLE OF AN DICT (Dictionary can be called as Dict)
#   HERE WE ARE TAKING ALL KEY VALUES ARE STRING DATATYPE
student_details = {
    "id": 720,
    "name": "Gnaneswar",
    "marks": [96, 55, 37, 99],
    "fullName":  {
        "firstName": "Gnaneswar",
        "lastName": "Korakuti"
    },
    "marks_immutable": (97, 99, 98, 95)
}

# print whole student_details DICT
print(student_details)

#   print an value of where key is holding ID
print(student_details["id"])

#   update the value where key is holding ID and print
#   here key is unique right because of these behaviour it is replaicing 720 with 916
#   and if we dont have the key and we try to update then it will create and key and store corresponding value
student_details["id"] = 916
student_details["id's"] = 420
print(student_details["id"])
print(student_details["id's"])
print(student_details)

#   if value is muttable data we can modify corespoinding value using key
#   here we have marks are muttable data list to add data in the list we know append() and to remove data we know remove() or pop method
student_details["marks"].append(92)
student_details["marks"].remove(37)
student_details["marks"].pop()
student_details["marks"].pop(0)
print(student_details["marks"])


#   if we want all keys use keys() method
print(student_details.keys())

#   if we want all values use values() method
print(student_details.values())

#   if you want all keys and values use items() method
# this returns an list of tuples where tuples hold key and value
print(student_details.items())
print(student_details)
# dict.items() → iterable view object, behaves like a list of (key, value) tuples.
# dict itself → prints in dictionary literal format (Python syntax).

# to get value we normally use like this
value_of_id = student_details["id"]
#   if id is not present boom we will get Error
# value_of_id = student_details["idsdf"]      #   KeyError: 'idsdf'
#   to avoid this we have an method called get where we pass id and pass an defalt value or else skip the 2nd paramer in dict if id is not present it print default value and doesnt add key to the dict
# if key is not present prints 0
value_of_id = student_details.get("idsdf", 0)
value_of_id_with_one_parameter = student_details.get(
    "idsdf")   # if key is not present prints none
print(value_of_id)
print(value_of_id_with_one_parameter)
print(student_details.items())

#   To remove key from the dict we have pop(key) method
student_details.pop("id's")
print(student_details.get("id's", 0))


#   to update normally we use like this
student_details["name"] = "Prabhu"
print(student_details.get("name"), "")
#   but this have one big disadvantage if key is not present it will create new key and store this value to avoid this
#   we need to use conditional statements in
if "name" in student_details:
    student_details["name"] = "Prabhu"
    print(student_details.get("name"))
#   or if you want to print else part also use ternary operation
student_details["name"] = "Ravi kanth" if "name" in student_details else print(
    "name key is not present please check")
print(student_details.get("name"))

#   suppose we have another dict we want to add those 2nd dict to first one no need to do manullay with iteration we can use update method

#   here in 2nd dict im using all different types of data for key
#   here im using INT, FLOAT, STRING, TUPLE, FROZENSET(same as set but immutable set), NONE
#   here i didnt add list,set,dict because those are muttable data if we add we will get error
second_dict = {
    1: 999,
    3.14: [1, 2, 3],
    'name': {'first': 'Alice'},
    (1, 2, 3): 'tuple as key',
    frozenset({10, 20}): 'frozen key',
    None: 'null-like key'
}
student_details.update(second_dict)
print(student_details.items())

# what type of error we will get if we use LIST SET DICT
# second_dict = {
#     [5,6,7] : [567,932]     #   TypeError: unhashable type: 'list'
# }

# second_dict = {
#     {5,6,7} : [567,932]     #   TypeError: unhashable type: 'set'
# }

# second_dict = {
#     {
#        1: 999,
#        3.14: [1, 2, 3]
#     }   :  [21,35,99]         # TypeError: unhashable type: 'dict'
# }

# second_dict = {
#     [5,6,7] : [567,932],        # at first line we will get TypeError and execution stop
#     {5,6,7} : [567,932],
#     {
#        1: 999,
#        3.14: [1, 2, 3]
#     } :   [21,35,99]
# }

# to clear all keys and values we will use clear() method
student_details.clear()
print(student_details.items())


my_dict = {"clgid":720,"fname":"Gnaneswar","lname":"Korakuti","fullname":"Gnaneswar Korakuti","mobileno":9876543210,}

#   getting items form dict using various ways from for loop
for key in my_dict:
    print(key,end=" ")
print("")

for key in my_dict.keys():
    print(key,end=" ")
print("")

for value in my_dict.values():
    print(value,end=" ")
print("")

for key,value in my_dict.items():
    print(f"{key} : {value}, ",end=" ")
print("")