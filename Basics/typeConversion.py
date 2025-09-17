import math
from typing import Final

x = input("x : ")
# input comes from user is always string
# y = x + 1  TypeError: can only concatenate str

# if you want to know the type of an variable
print(type(x))

# to resove this we need to use typeconversion
# for int int(x), float float(x), boolean bool(x), string str(x)
print(f"after type casting {type(int(x))}")

y = int(x) + 1
print(f"value of y is {y}")

# Falsy values are
#       ""
#       0
#       None

# What are all the primitive data types in python?
#   -> numbers  -> strings  -> boolean


marks = 25
# int to string
marks = str(marks)
# string to int
marks = int(marks)

float_values = 3.765
#   float to int    DATA LOSS WILL BE HAPPEN HERE WE WILL LOOSE 765 after decimal values
float_to_int = int(float_values)

#   int to float we dont loss any data
float_values = float(float_to_int)



