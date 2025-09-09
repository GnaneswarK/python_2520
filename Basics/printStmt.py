print("Hello World 🦁")
print("🦁" * 10)
lion = "🦁" + "10"
#concat_string_and_integer
print("Python" + " " + str(10))
#concat_string_and_integer_using_fstring
print(f"Python {10}")
print(f"{10+12} Python {24}")

#Variables 
student_id = 720
rating = 4.98
is_published = False
course_name = "Python"

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


#String methods
