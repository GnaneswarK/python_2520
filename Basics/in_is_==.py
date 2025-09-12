# "in" normally .conatins() method in java
# for substring check in the string we will use in
# Example

course = "python course"
print(f"checking course present in {course} => {"course" in course} ")
print(f"checking java present in {course} => {"java" in course} ")

# == it checks whether both lhs and rhs value are same or not
# == plays as .equals() in java

course1 = "python course"
course2 = "python course"
print(
    f"checking both {course1} and {course2} have same value or not => {course1 == course2}")

# "is" normally checks the both memory addres same or not means both are sharing same memory
print(
    f"checking both {course1} and {course2} have same value or not => {course1 is course2}")
# here you will see true for primitive data types like numbers and string
# if value is same phyton wont create new memory address for them instead it will assign the memory to the sahred one
# like you say an special concept in java like string pool
# but when it comes to complex datatypes its different example list tuples

nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 4]
# here we know nums1 and nums2 both are having identical list of values
# but when we see closely python will assign different loctions for each other
# and one more beauty of python is nums1[0] is 1 right and nums2[0] is 1 and both nums1[0] and nums2[0] are numbers int these values shares same memory address but their parent lists doesnt share same address

print(
    f"checking 2 different list sharing same address or not which are identical {nums1} and {nums2} => {nums1 is nums2}")
print(
    f"checking 2 different list inside the data sharing same address or not which are identical values int type {nums1[0]} and {nums2[0]} => {nums1[0] is nums2[0]}")
# for your conformation im printing there memory address numbers also
print(f"memory addres of {nums1} is {id(nums1)}")
print(f"memory address of {nums2} is {id(nums2)}")
print(
    f"inside the list fist value addres holding the value {nums1[0]} and its address is {id(nums1[0])}")
print(
    f"inside the list fist value addres holding the value {nums2[0]} and its address is {id(nums2[0])}")

# note point if you try to do in in int types you will get type error like this
print(10 in 25)  # TypeError: argument of type 'int' is not iterable
# because for checing substring we are using loops to iterate whether same charecter or word is present or not but for numbers there is no concept of iteration thats why we are getting TypeError
