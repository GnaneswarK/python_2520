#   Generally list are hetrogeneous(can hold all types of datatypes)
#   but in reality if you want deal with hetrogenous go with tutle
#   for homogeneous we will go with list
#   lists are muttable we can
#   if we want to assign to a new list we can do & we can change the individual data also
#   if you want to decale an list then use square brackets like this []


list = [10, 30, 50, 70, 100]
print(list)
print(f"displaying the first element in the list {list[0]}")
list[0] = input("Enter the value to update the first element > ")
print(f"updated first element in the list {list[0]}")
print(list)
print(f"before changing whole object memory address {id(list)}")
list = [2, 3, 4, 5]
print(f"change whole object of the list {list}")
print(f"after changing whole object memory address {id(list)}")


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

#   SET it is also an hetrogenous
#   note in set you cannot add list,map,set but you can add tuple because of hashing
#   set stores values by using hashvalues
#   if you modify any data present in the set automatically its hashvalue changes and you cannot access it so due to this they said in set you cannot add mutable data
#   in set we can add immutable data like int float bool string tuple
#   to decalre set we need to use flower brackets {}
set = {1, 1.56, "Hello", True}
# reslut {1, 1.56, 'Hello'} it wont print true because of duplicates
print(set)
# As all we know set doent allows duplicates boolean is subclass of int
print(isinstance(True, int))  # prints true
# so in set 1 and true holds same hashcode + bonus tip float value of 1.0 also holds same value as 1 and true
# set is MUTABLE BUT INSIDE THE SET VALUES ARE IMMUTABLE na we we add data delete data but cannot modify data
# set[0] = 25     #   TypeError: 'set' object does not support item assignment
print(set)
# as it is muttable we can reassign object
set = {2, 1.96, "Hello", True, (4, 6, 7)}
print(set)


#       NOW WE WILL DISCUSS ABOUT METHODS INSIDE THE LIST SET TUPLE DIRECTORY(MAP)  and BONUS FROZENSET ALSO

#   LIST

list_of_numbers = [5, 7, 3, 2, 2, 9, 1, 2]
print(f"print list before updation {list_of_numbers}")

# modify data in index of 2
list_of_numbers[2] = 27
print(f"print list after updating value at index at {list_of_numbers}")

# getting index number with correspoinding vaue
index = list_of_numbers.index(2)
print(
    f"index number for the value of 2 => {index} and list => {list_of_numbers}")

#
list_of_numbers.insert(2, 250)
print(f"adding 250 value at iindex 2 {list_of_numbers}")

# Adding value to the List at the End
list_of_numbers.append(12)
print(f"print list after adding value {list_of_numbers}")

# removes last index value return removed value
removed_value = list_of_numbers.pop()
print(
    f"Removed value {removed_value} list after removing last index {list_of_numbers}")
# if we want to remove at perticular index we can pass index value in the pop metho
removed_value = list_of_numbers.pop(3)
print(
    f"Removed value {removed_value}, with index of 3 list after removing last index {list_of_numbers}")
# we can acheive this list_of_numbers.pop(3) by using delete method also see here use this del one if you dont want which value you are removing
del list_of_numbers[5]
print(
    f"with index of 3 list after removing last index {list_of_numbers}")


# no return type if value present removes first occurence values else ValueError
list_of_numbers.remove(250)
print(
    f"removes values int list first occurence one after removing list {list_of_numbers}")

# sort in ascending order
list_of_numbers.sort()
print(f"list after ascending order {list_of_numbers}")

# shallow copy
shallow_copy_of_the_list = list_of_numbers.copy()
print(f"shadow copy of the list {shallow_copy_of_the_list}")
# to understand more about shallow copy in the list insted of immutable data we will add mutable data then we will see the difference
# shallow copy means creates a new container (new list object),but the elements inside are copied by reference, not duplicated.
list = [[1, 2, 3], [4, 5]]
#   here in list list[0] is an list which holds [1,2,3] which is an mutable list
#   shallow copy of the list
shallow_copy = list.copy()
#   now we are doing shallow copy for shallow copy it creates new list object which holds same data as list like this list = [[1,2,3],[4,5]]
#   but inside list list[0] and list[1] for these it wont create new list object instead it reference to same memory addres check this
print(
    f"memory address of list and shallow_copy both are different {id(list)} & {id(shallow_copy)} ")
print(
    f"memory address of list[0] and shallow_copy[0] both are same because both are sharing same reference {id(list[0])} & {id(shallow_copy[0])}")
#   if i try to update the list[0][1] then changes will reflect in shallow copy also because both are sharing same reference
print(f"{list} & {shallow_copy}")
list[0][1] = 250
print(f"{list} & {shallow_copy}")
#   and if try to update list[0] then it wont reflect on shallow copy because here are we are redirecting whole reference so in this scenerio no change
list[0] = 250
print(f"{list} & {shallow_copy}")
# if you want deep copy where reference also should create new object then import copy use this method inside the copy => copy.deepcopy(list) which retrun deepcopy list

#   count method returns the count of the value occurence
count = list_of_numbers.count(119)
print(count)

# Extend nothing like adding multiple values at time to the list or merging 2 list like if we have 2 arrays
# in which each array holds 10 values and we want to combine then then we will get an list which holds 20 values this concept similar to extend
list_of_numbers.extend([21, 22, 23, 24, 25, 26, 27])
print(list_of_numbers)

# se if we want to reverese an list means last elemnt first first elemnt last
# if they ask print numbers in descending order we can use this
# first sort function which prints in ascneding order then reverse we will get descending order
list_of_numbers.sort()
list_of_numbers.reverse()
print(list_of_numbers)
# for reverse list we can use like this also
print(f"reverse of an list {list_of_numbers[::-1]}")

#   to find the legth of an list
print(f" length of an list {len(list_of_numbers)}")

# if we have only numbers in the list we can use some build in classes or methods to do min max sum
print(f"min value in the list {min(list_of_numbers)}")
print(f"max value in the list {max(list_of_numbers)}")
print(f"sum of value in the list {sum(list_of_numbers)}")

# for substring means sublist in the list we want we can use like this
# this concept is known as slicing
print(
    f"sublist in the list starts with 1 ends with 5 means holds and stubstring from index 1 to 4 4 values {list_of_numbers[1:5]}")

#   Membership test using in not in checking whether number is present ot not
# see we are using remove method and passing value if value present no problem if not then we will get ValueError
# to avoid we use memebership test using in
if 27 in list_of_numbers:
    print(f"before removing 27 from the list {list_of_numbers}")
    list_of_numbers.remove(27)
    # first it will check in list we ave 27 or not if yes the if loop enters
    # next it will remove 27 which is first occurence
    print(f"after removing 27 from the list {list_of_numbers}")

# clears all data from the list
list_of_numbers.clear()
print(list_of_numbers)
# for deleting all values we are using clear() instead of clear() method we can use del also
list_of_numbers.extend([1, 5, 7, 8, 9, 2])
del list_of_numbers[:]
print(list_of_numbers)


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


#   SET ->  SET Is muttable and elments added in the sets are not index based system
#   set uses the pattern like hashcode where objects or data types like int float tuple are added by hashvalue
#   so set use hashvalue right so it wont allow duplicates hashvalue of 1 and 1 is same right so it will take one time only
#   we cannot add mutable data like set list to the set because if these mutable data's are present in the set they can easity modify the data
#   and haschcode of the object also changes by the we are unable to access the object data with the reference so to aviod these
#   they are restricted the adding mutable data
#   if you want to know what will happen it an mutable data present in the set which is added values by using hashcode they try it on java you know the differece
#   Set<Set<Integers>> but try this for only testing process never ever dare try to change the data if you try you will lost addres to track it

set = {1, 3, "str", (5, 7, 8), ("len1", '12', 17), 3.65}  # valid
# set = {1, 3, "str", (5, 7, 8), ["len1", '12', 17], 3.65}  # in valid    TypeError: unhashable type: 'list'
print(set)

# addition = sum(set)   # invalid different data tupes used
# print(addition)

#   add to set  it value present doent effect the set if not added by using hashvalue
set.add(35)

# set.remove("str")   # if value is not present we will get keyError so better use condition check
print(f"remove the string which is 'str'{set.remove("str")}") if "str" in set else print(
    "Value didnt present in the set")
print(set)

# and you think like if i dont have keyError there's no need to write condition check to remove right boom you have an method where if elemnt didnt find it wont give any error

# closely observe we dont have this it check if dont have it wont give any error
set.discard("jhgdhjkgfjdbwvgefrnjbh")
print(set)

# we have pop() method also but be caution's dont use this pop() method and dont send index in the pop because set is not index based system
#   if we are using pop() to remove it will remove first element in the set, see as i said it removes first elemnt not in the set we sent it removes first element based on the value hashvalue it stored in this first value it will remove
set.pop()
print(set)

# it clears whole data in the set
set.clear()
print(set)


# IN SET WE HAVE LOT MORE LIKE SET OPERATIONS WHERE WE WILL DEAL WITH UNION, UNION ALL, INTERSECTION......

set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}

#   union will create new set which is combined of set1 and set2
union_set = set1.union(set2)
print(union_set)

#   if you dont want new set and if you want add 2nd set elemnts to the 1st set then upo can use update
set1.update(set2)
print(set1)

#   if you want only common elements in the both set A intersection B then go with intersection and it retruns new set which holds common data
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}
intersection_set = set1.intersection(set2)
print(intersection_set)
#   if you dont want to create new set you want to update the set which only contains common data then use intersection_update()
set1.intersection_update(set2)
print(set1)

# difference it will remove common data from the first set which are present in the second one
# suppose set 1 contains {1,2,3} set2 contaions {3,4,5} by using difference it will ignore common data in the 2nd set result {1,2}
# difference also retuns new set
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}
difference_set = set1.difference(set2)
print(difference_set)
#   if you dont want to create new set you want to update the set which only contains not common data then use difference_update()
set1.difference_update(set2)
print(set1)

#   AND IF YOU WANT DIFFERENCE FROM 2 SETS THEN USE Symmetric_difference
#   it will remove common data from 2 sets and add all the values of set1 and set2 to new set
#   set1 contains {1,2,3} set2 contains {3,4,5} result set is {1,2,4,5}
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}
symmetric_different_set = set1.symmetric_difference(set2)
print(symmetric_different_set)
#   AND if you dont want new set use update one
set1.symmetric_difference_update(set2)
print(set1)


# COMPARITION issubset()  issuperset()    isdisjoin()\
set1 = {1, 2}
set2 = {1, 2, 3}
set3 = {4, 5}
# subset
# True what it tell what are all elements in the set1 must be present in set2 NOTE all set1 set elements present in the set2
print(set1.issubset(set2))
# FALSE becuse set2 contains {1, 2, 3} and set1 contains {1,2} in set1 we are lacing 3 so false
print(set2.issubset(set1))
# TRUE IT IS OPPISITE OT subset here we are saying what are all elemnts present in the set1 must be present in the set2
print(set2.issuperset(set1))
# FALSE because set1 contains {1,2} and set2 contains{1,2,3} where set1 is lacking of 3 so false
print(set1.issuperset(set2))
# FALSE because set1 and set2 contains common elements
print(set1.isdisjoint(set2))
# TRUE both set2 and set3 doesnt have common elements
print(set2.isdisjoint(set3))
