# def is for defining functions
# there are 2 TYPES OF FUNCTIONS
#       PERFORM A TASK FUNCTION
#       RETURN A VALUE FUNCTION
# print natural numbers upto 100 without arguments
def print_natural_numbers():
    for val in range(1, 21):
        print(val, end=" ")
    print("")


# print natural numbers upto which value using arguments
def print_natural_numbers_with_args(number):
    for val in range(1, number+1):
        print(val, end=" ")
    print("")


# print first name and last name concat each other
def print_fullname_with_args(first_name, last_name):
    print(f"print fullname => {first_name} {last_name}")


def get_fullname_with_args(first_name, last_name):
    return f"{first_name} {last_name}"


print_natural_numbers()
print_natural_numbers_with_args(int(input("Enter an positive number : ")))
firstName = input("firstname : ")
lastName = input("lastname : ")
print_fullname_with_args(firstName, lastName)
fullName = get_fullname_with_args(firstName, lastName)
print(f"Full name is {fullName}")

# if we try to print the function which is having no return type then what we will get??
# so here it will says None and + its not performing the function also
print(print_natural_numbers())
# if you do like this in Java you will get compile time error


#   functions using unpacked

#   adding 2 numbers
def sum_of_numbers(num1, num2):
    return num1+num2

#   adding 3 numbers


def sum_of_numbers(num1, num2, num3):
    return num1+num2+num3

#   what of we have thousands of numbers??
#   so in this scenerio we will use unpacking   *
#   so whenever we using unpacked means its an list


def sum_of_numbers_using_unpacked(*nums):
    total = 0
    for num in nums:
        total += num
    return num

#   validation check for using * , KEYWORD ONLY , DEFAULT VALUES


def check1(*num):
    return 1  # valid


def check2(num, *num2):
    return 2            # valid

# Any parameter after * args becomes keyword-only


def check3(num, *num2, num3):
    return num+num3     # Valid but some precausions need to take here num3 is keyword we must pass it by keyword reference liek this num3=27


# Calling it like check3(1, 2, 5, 9) fails because num3 must be passed explicitly:
print(check3(1, 2, 5, 9, num3=27))

#   **kwargs (double-star) must be the last


def f(a, *b, **c):
    return 1    # valid

# def f(a, **b, *c):
#     return 1    # Invalid compile time  "c" is not accessed


#   in functions we can pass default values
def alpha(num1=2, num2=3):
    return True  # VALID


def alpha1(num1, num2=3):
    return True  # VALID

# def alpha2(num1=2, num2):
#     return True  # InVALID "num2" is not accessed
#   SyntaxError: non-default argument follows default argument Because num2 (non-default) comes after num1=2 (default).
#   Python doesn’t know how to call it unambiguously.


def alpha1(num1=27, *num2, num3=5, num4):
    return True  # VALID
#   after  unpacked args all are keywords only so it is not mandaotory to methion all for default values

# def alpha1(num1=27,num2, *num2, num3=5,num4):
#     return True  # InVALID
#   We can’t put a non-default param (num2) after a default (num1=27) → same SyntaxError we saw earlier.

# def alpha1(num1, *num2=3):
#     return True  # InVALID  "num2" is not accessed
#   SyntaxError: var-positional argument cannot have default value
