import math
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

### Falsy values are
#       ""
#       0
#       None

#What are all the primitive data types in python?
#   -> numbers  -> strings  -> boolean
