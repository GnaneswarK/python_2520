# intendation
# instead of open and close paranthasis in c java js like this {} in python we use intendation like this (tab space or space) to define code blocks

x = 25
if x < 20:
    print("x is less than 20")
elif x > 20:
    print("x is grather than 20")
else:
    print("x is equal to 20")

print("done with if loop")

#   TERNARY OPERATOR

age = 22
# normal if else statement
# NOTE
# Python scopes are mainly function, class, or module-level.
# Variables declared inside an if/else block are still part of the same function or global scope.
# Python does not create a new block scope for if, for, while, etc.
# Blocks like if, for, while do not introduce a new scope.
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# this 5 lines of code can acheive in one line by using ternary operations
# Java TERNARY OPERATION SYNTAX     condition   ?   true_value  :   false_value
# Python TERNARY OPERATION SYNTAX   true_value  if  condition  else false_value
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

#   LOGICAL OPERATOR
#   AND OR NOT
high_income = True
good_credit_score = False
student = False
# implementing and or not
if (high_income or good_credit_score) and not student:
    print("Eligible for car loan")
else:
    print("Not Eligible for car loan")
# similary in Java
# if (high_income || good_credit_score) && !student{
#       System.out.println("Eligible for car loan");
# }else {
#       System.out.println("Not Eligible for car loan");
# }


#       CHAINING COMPARITION OPERATORS
#   if we say for Age eligibily for voting is greather than 18 and lessthan 65
#   then in mathamatical expression we say   18<= age < 65
#   you know what that mathamatical expression is valid in Python
#   instead of age >= 18 and age < 65 we can say like this 18<= age < 65
#   18<= age < 65 This way of writting logic is known as chaining comparition
if 18 <= age < 65:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")
