x = 1  # natural numbers
x = 1.23  # float numbers
x = 3 + 4j  # a + bi immaginary numbers(complex)

print(10 + 3)  # Addition
print(10 * 3)  # Multiplication
print(10 - 3)  # Subtraction
print(10 / 3)  # Division (double type)
print(10 // 3)  # Return natural number round of
print(10 % 3)  # returns remainder
print(10 ** 3)  # Exponential power 10^3 => 1000
print(10 != 10)  # if both are same return False
# after decimal greather than 50 then it will take next number
print(round(10.51))
print(round(10.33))
# if positive number or negative numbers it always displays postive number
print(abs(-4.96))


x = 12
y = 23
z = 13

print(x < y and y > z)  # T   AND     T   =   T
print(x < y and y < z)  # T   AND     F   =   F


print(x < y or y > z)  # T   OR     T   =   T
print(x < y or y < z)  # T   OR     F   =   T
print(x > y or y < z)  # F   OR     F   =   F


print(not x < y)  # T NOT = F
print(not x > y)  # F NOT = T

# for binary numbers &(and) |(or)
# in  &  1 and 1 is 1 => both sould be 1 then only one
# int |  1  or 0 = 1, 1 or 1 = 1 => any one should be 1 then it is one
# int |  1  or 0 = 1, 1 or 1 = 0, 0 or 0 = 0 => both are same return 0

a = 5  # 101
b = 6  # 011
c = a & b
d = a | b
e = a ^ b
#           a   =   101     a   =   101     a   =   101
#           b   =   110     b   =   110     b   =   110
#           &   =   100     |   =   111     ^   =   011     BINARY

#                    4               7               3      DECIMAL
print(f"value of {a} & {b}  is {c}")
print(f"value of {a} | {b}  is {d}")

# LETS DO ADDING OF 2 NUMBERS WITHOUT USING + SIGN USING BINALRY OPERATIONS & | <<(left shift carry)

value1 = 5
value2 = 7


def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


print(add(value1, value2))

# procedure
#   condition y ! = 0 => 7 != 0 true while loop enter
#   carry = x & y => 101 & 111 => 101 => 5
#   x = x ^ y =>     101 ^ 111 => 010 => 2
#   y = carry << 1 =>  101 << 1 => adding right side end 0 for one time 1010 => 10
#
#   2ND WHILE LOOP
#   y!=0 => true y is 10
#   carry = x & y => 2 & 10 => 2
#   x = x ^ y => 2 ^ 10 => 8
#   y = carry <<1 => 2 << 1 => 4
#
#   3ND WHILE LOOP
#   y!=0 => true y is 4
#   carry = x & y => 8 & 4 => 0
#   x = x ^ y => 2 ^ 10 => 12
#   y = carry <<1 => 2 << 1 => 0
#  loops end return x ans 5

# what left shift will do means 1 1 will return true in & but we need to carry 1 for left side so we are doing leftshift << 1
