element = "Python Course"

length = len(element)
first_charector = element[0]
last_charector = element[-1]
sub_string = element[0:6]
# string pool type same memory address with difference references
dup_string = element[0:]
# new String like creating object in java with new keyword new String(element) or element[:] both are same
copy_string = element[:]

print(length)
print(first_charector)
print(last_charector)
print(sub_string)
print(dup_string)

sample_string = "Testing Same Object or Not"

# copy with out emitting both side like this [0:] , [:len(element)]
without_dual_omit = element[0:]
with_dual_omit = element[:]

# 'is' is like == in Java and '==' is like .equals in Java
print(element is element[0:len(element)])
print(element is element[:])


# String methods

element = "  python course  "

# TO UPPER CASE NOTE STRINGS ARE IMMUTABLE SAME AS LIKE IN JAVA
print(element.upper())
# to lower case
print(element.lower())
# Starting Charecter After Space Is Capital Letter
print(element.title())
# trim space from left
print(element.lstrip())
#   trim space from right
print(element.rstrip())
# trim space both left and right
print(element.strip())
# find the index where it matches from start if not returns -1
print(element.find("o"))
# replace all where ever it appears
print(element.replace("python", "java"))
# in indicates whether it is present or not in the string
print("course" in element)
# we have "not in" also where we are checking for absent
print("Java" not in element)
# like concat with each charecter space element space next charector in jion continue
print(element.join("12345"))
# starting index it will print where ever it find if not ValueError
print(element.index("o"))
# length of an string
print(len(element))
# count the occurence of the string
print(element.count("o"))     # 2
print(element.count("o", 0, 6))  # 1 (between index 0–6 only)
print(element.count("z"))     # 0 (not found)
# startswith    # returns boolean true or false
print(element.strip().startswith("python"))
# ends with     # returns boolean true or false
print(element.strip().endswith("course"))

#   STRING SLICING
name = "prabhu ghajula"
#   FOR SUBSTRING
first_name = name[0:6]   # starts with 0 & ends with 6(doesnt take index 6)
# this also same before colon if we didnt mention anything it starts from 0
dup_first_name = name[:6]
# starts with index 7 ends with index 14 doesnt take index 14
last_name = name[7:14]
# this also same if we dont mention anything after colon then its take len(name)
dup_last_name = name[7:]
full_name = name[0:14]  # stats with 0 ends with 14
dup_full_name = name[:]  # this starts from start index to end index
#   IF i WANT TO PRINT EVEN CHARECTERS FROM THE STRING THEN I WILL USE LIKE THI
#   start:stop:step
# here it is stats from zero index and ends with last index setp is 2 it prints like this pah hjl
even_index = name[0:14:2]
# see as i said before colom if i didnt mention then it starts from zero and after colon if i didnt mention its ends with len(name)
#   above line i can mention like this also
dup_even_index = name[::2]
# similary for odd index
# why starts with one beacuse odd number stats from 1 not zero
odd_index = name[1::2]
#   by default step is 1 so if you dont mention there nothing gonna happen so name[0:6] == name[0:6:1]
# for fullname like this also we can do
dup_full_name = name[::]  # this also starts from start index to end index
#   if sept is -1 means here increment is by negative 1 which follows reverse order
#   to print reverse of an string use like this [::-1] or [0:len(name):-1]
reverse = name[::-1]


#   PRINT STATEMNTS
print("Original name: ", name)

print("first_name:", first_name)
print("dup_first_name:", dup_first_name)

print("last_name:", last_name)
print("dup_last_name:", dup_last_name)

print("full_name:", full_name)
print("dup_full_name:", dup_full_name)

print("even_index:", even_index)
print("dup_even_index:", dup_even_index)

print("odd_index:", odd_index)

print("reverse:", reverse)

greeting = "Hello how are you?"
my_list = greeting.split(" ")
print(my_list)
#   list to string
# where in single code i use single space right that is delimeter to jion the list
greeting = ' '.join(my_list)
print(greeting)
