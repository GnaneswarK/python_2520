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
