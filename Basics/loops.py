# For Loop
# in Java
#   for( int i = 0; i < 5; i++ ){System.out.println("Hello")}
#   similary in java if we are starting with 0 no need to metion start index and increment is by one then no need to mention increment value

# same for loop start with 0 end with 4 increment by 1 can be done in 3 ways by python

for num in range(3):
    print("Hello")
#   here num is "i" in java as i said if we are starting with 0 ne need to methion & for increment also if we want we can do it

for num in range(0, 3):
    print("world")
#   here num start with 0 as we mentined in range
#   and num is less than 3 as mentioned in range
#   at the same time we didnt mention increment so by default increment is 1

for num in range(0, 3, 1):
    print("this is python")
#   here num start with 0 as we mentined in range
#   and num is less than 3 as mentioned in range
#   at the same time increment by 1 as mentioned in range

# Advanced For Loop OR Enhanced For Loop in java
# int array[] = {12,13,15,17,21}
# for (int num : array){System.out.print(num+" ")}
# similary in python
array = [10, 20, 30, 40, 50]
for num in array:
    print(num, end=" ")
print()

# Range is an iterable so we are using in for loop for assinging values
# similary strings also interable so we can use for loops also
for char in "python":
    print(char, end=" ")
print()

# Nested for loop to showcase 2D array
for x in range(5):
    for y in range(5):
        print(f"{x},{y}", end=" ")
    print("")
