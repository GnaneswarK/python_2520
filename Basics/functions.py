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
