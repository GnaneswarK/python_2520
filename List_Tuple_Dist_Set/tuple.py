#   tuple is immutale by nature one value assigned in the tupple you cant change it
#   if you want you can change the whole object of the tuple
#   generally if you want to declare an tuple then you need to use round brackets ()

x = 1
tuple = (1, "one", 1.25, True)
print(tuple)
print(type(tuple))
print(id(tuple))
print(f"display first element in the tuple {tuple[1]}")
print(id(x) == id(tuple[0]))  # as we know values share same memory
# tuple[0] = 25   #TypeError: 'tuple' object does not support item assignment
print(tuple)
tuple = (2, "two", 2.35, False)  # as we discussed we can change the object
print(tuple)


#   TUPLE -> tuple is an immutable data so we cannot modify add remove data
#   but we have some methods that we use like count number of occurence of an number
#   index   by using this we can get the index of an perticular value
#   and build in functions like len sum min max slicing(note it wont change data instead it will create new object) in not for conditional statements

tuple = (1, 5, 8, 5, 12, 5, 17)
#   tuple.count(5)
count = tuple.count(5)
print(
    f"we will get the occurence of 5 in the tuple {count} and tuple is {tuple}")

#   tuple.index(12) and using condition statement if for not getting valueError note if we have multipe values we will get first occurence one
print(f"index of value of {tuple.index(12)}") if 12 in tuple else print(
    "12 value is not present in the tuple")

#   NOTE :: min max sum will work only if we have same type of data for all elements present in the object and those data types are int float and
#   KEY NOTE :: min max will work for strings also it will use ascii values to check min and max
minimum = min(tuple)
maximum = max(tuple)
addition = sum(tuple)
length = len(tuple)
substring = tuple[0:3]
print(
    f"sum of values in the tuple {addition} \nmin value int the tuple is {minimum} \nmax value in the tuple is {maximum} \nlength of the tuple is {length} \nSsubstring from the startindex of 0 to end index of 3 in the tuple is {substring}")


#   we have an list we know inside list values doesnt want to modify or update
#   in this scenerio we want this list as tuple and if we try to add each element like in usage of loop it wont happen once tuple is created we cannot modify or update
#   so we have an inbuit data type tuple rigth with this we can convert list to tuple
#   we know tuple is immutable data but we can add list to it because
#   we can change list inside the list but cannot change the list
my_list = [1, 3, 7, (15, 19), 28, [29, 32]]
del tuple  # if you want to know why im using this go through list.py there i mention
my_tuple = tuple(my_list)
print(my_tuple)


#   suppose my tuple look like this
my_tuple = (720, "Gnaneswar", "BTech", "CSE")
#   we know its looks like id name highest graduation and course
#   if we want to select id we will do like this list[0] and we dont know what is meant by list[0]
#   so we will do like this id = list[0] suppose we have 3 or 4 records we can do it but if we have plenty of records then plenty of lines
#   instead we can do some shorter way like this
my_id, my_name, my_highest_graduation, my_course = my_tuple
#   like this we are assigning each fied to to an reference variable
print(f"my id is {my_id} \nmy name is {my_name}")
#   NOTE :: LHS == RHS number of elements in the tuple is equal to reference variable
#   if LHS != RHS we will get this Error
#   my_id, my_name = my_tuple   #   ValueError: too many values to unpack (expected 2)

#   in Python we have unpacking also called as starred expression generally noted as *
i1, i2, *i3 = my_tuple
#   here i1 holds roll number i2 holds gnaneswar
#   but when it comes to it we noted as * means its an collection which is list holds multiple data here i3 holds Btech cse
print(f"{i1}\n{i2}\n{i3}")
#   we can do like this also
i1, *i2, i3 = my_tuple
print(f"{i1}\n{i2}\n{i3}")
#   we cannot do like this
my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13)
# i1, *i2, i3, *i4 = my_tuple     # Only one unpack operation allowed in list
#   if we do we will get this error SyntaxError: multiple starred expressions in assignment
 
