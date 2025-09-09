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
