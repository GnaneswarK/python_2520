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


#   As we know in set we cannot add duplicates and also mutable data tupes like list set dict
#   in python we know we have an buid-in class called set
#   by using this we can convert list to set
#   here we are taking 2 scenerios of list in list1 we have all immutable data and no muttable data
#   where as in list 2 we have combination of mutable data and immutable data
list1 = [2, "str", 3.17, True, (5, 6, 7)]
list2 = [1, False, ("str", True, 5.69), list1, {29, 52}]
del set
# true it will create my_set because in list we have all are immutable data
my_set = set(list1)
# false it wont create an set and throws an error unhashable type: 'list' because of list is mutable data
# my_set = set(list2)
