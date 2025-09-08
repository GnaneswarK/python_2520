import math

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
# after decimal greather than 50 then it will take next number
print(round(10.51))
print(round(10.33))
# if positive number or negative numbers it always displays postive number
print(abs(-4.96))


# math module methods

###############        Number-theoretic functions    ######################

# for combinations NCK OR NCN-K  N!/(K!*(N-K)!) : N must be equal or greather than k N>=K
# Example we have 3 numbers(a,b,c) pick any 2 here N is 3 K is 2
# we can pick ab ac bc combinations ans is 3 and formula for combination is NCK 3C2 or NCN-K 3C3-2 3C1
# note NCN or NC0 = 1 OR NC1 = 1

number_of_combinations = math.comb(3, 2)
print(f"number of combinations => {number_of_combinations}")

# for permutation NPK => N!/(N-K)!
# Example we have 3 numbers(a,b,c) pick any 2 here N is 3 K is 2
# ab ac ba bc ca cb
number_of_permutations = math.perm(3, 2)
print(f"number of permutations => {number_of_permutations}")

# N! = N*(N-1)*(N-2)*.....1
# 5! = 5*4*3*2*1
# Note 1! and 0! is 1
factorial = math.factorial(5)
print(f"factorial => {factorial}")

# greatest common divisior
# lets find factors for 2 numbers 12 and 6
# 6 factors 1 2 3 6 : 12 factors 1 2 3 4 6 12
# ans 6 is greatest common factor for both 6 and 12  so greatest common divisor GCD of 12 and 6 is 6
gcd = math.gcd(6, 12)
print(f"greatest common divisior => {gcd}")

# least common multiple
# lets find the LCM for 12 and 6
#    2  | 6 , 8
#       | 3 , 4    remainders after divisible with 2
# no common factors for 1 and 4 multiply all (divident and quotient) 2 * 3 * 4 = 24
lcm = math.lcm(6, 8)
print(f"least common multiple => {lcm}")


# float square root
# sqrt of 10 is 3.16 floor value of 3.16 is 3
floor_square_root_value = math.isqrt(10)
# we can use like this also int(math.sqrt()) but it is slow when compared to this math.isqrt(10)
# because while using this math.isqrt(10)we are skipping floating-point math
print(f"floor square root value => {floor_square_root_value}")


################        Floating point arithmetic       ##########################

# ceiling of x return next integer 5.6 => 6 , 5.1 => 6, 5.0 => 5 5.01 => 6
ceiling = math.ceil(5.66)
print(ceiling)
print(math.ceil(5.0))  # 5
print(math.ceil(5.99))  # 6
print(math.ceil(5.01))  # 6

# fabs return absolute of an number +-x is equal to x
print(math.fabs(-5))
print(math.fabs(5))
print(math.fabs(5.66))

# floor rounds of if after decimal greather than 50 next integer else round of to current integer
print(math.floor(5.6))
print(math.floor(-5.6))
