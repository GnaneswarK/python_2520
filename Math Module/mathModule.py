import math
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
print(f"ceil of 5.66 is -> {ceiling}")
print(f"ceil of 5.0 is  -> {math.ceil(5.0)}")  # 5
print(f"ceil of 5.99 is -> {math.ceil(5.99)}")  # 6
print(f"ceil of 5.01 is -> {math.ceil(5.01)}")  # 6

# fabs return absolute of an number +-x is equal to x
print(f"abs value of -5 -> {math.fabs(-5)}")
print(f"abs value of 5  -> {math.fabs(5)}")
print(f"abs value of 5.66 -> {math.fabs(5.66)}")

# floor rounds of if after decimal greather than 50 next integer else round of to current integer
print(f"floor value of 5.6 is {math.floor(5.6)}")
print(f"floor value of 5.1 is {math.floor(5.1)}")
print(f"floor value of 5.50 is {math.floor(5.50)}")
print(f"floor value of -5.6 is {math.floor(-5.6)}")
print(f"floor value of -5.2 is {math.floor(-5.2)}")
print(f"floor value of -5.50 is {math.floor(-5.50)}")

# fused Multiply Add Allias fma formula math.fma(x,y,z)  => (x+y)+z where x and y !=0
# normaly in this expresiion what will happen (x*y)+z  after the result of x*y it will do floor then add z again floor
# by doing this we wont get exact value i avoid this we will use fma where after multiplying x*y the adding z next it will do floor to the value
print(math.fma(3.998, 4.997, 2.665))
print((3.998 * 4.997) + 2.665)
# with small values you wont find it but while dealing with large numbers you will find the difference
x = 1e308
y = 1e-308
z = -1.0
print((x * y) + z)
print(math.fma(x, y, z))

# mod -> modulus remainder
print(f"modulus remainder of an value 7%2 => {math.fmod(7, 2)}")

# modf if we pass value we will get an tuple which contains float value and integer
result = math.modf(4.397)
# if we want to access the float use result[0] and for the integer use result[1]
# using modf for More precise (avoids tiny floating-point subtraction errors).
# if you want only integer part better use math.floor(x) or int(x) if you want both float and int use math.modf(x)
print(f"modf decimal value 4.397 : {result[0]}")
print(f"modf integer value 4.397 : {result[1]}")


# remainder generally follws math.remainder(x,y)
# q = x/y nearest integer means next step math.floor(q) if 5.6 returns 6 : 5.2 returns 5
# reslut = x - q*y
# result range [-y/2 , +y/2]
# very helpfull when we are working with circles degrees trignometry
# small example
# 355 in cirlce we have 360 degress or 2 pie for 355 degrees we need to rotate 355 degrees positive or else 5 degrees negative
# range means here full circle is 360 means positive 180 and negative 180
# by using this math.remainder(355,360) we will get -5 which means negative rotation 5 digree this should be helpfull when we are working automation robots to rotate instead of 355 full rotate 5 degree oposite rotation both are same
print(f"remainder of 3,7 is ->  {math.remainder(3, 7)}")


# math.trunc(x) which removes decimal and print integer similar not same one as int(x)
print(f"trunc of 3.99 -> {math.trunc(3.99)}")
print(f"trunc of 3.01 -> {math.trunc(3.01)}")


#######################     Floating point manipulation functions       ########################
