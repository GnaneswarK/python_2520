# print whether an number is prime or not

number = int(input("num :"))
boolean = True
num = 2
for num in range(2, number//num+1, 1):
    if number % num == 0:
        boolean = False
        break
result = "prime" if boolean else "not Prime"
print(f"{number} is {result}")

# range(2, num//number+1, 1): this range end index one evealuate this num//number+1 for the first time then it wont so it not good practise in java every iterate it recalculate but in python only first time it will recalculate
# we will try to implement this in while loop

boolean = True
num = 2
while num <= number//num:
    if number % num == 0:
        boolean = False
        break
    num += 1
result = "prime" if boolean else "not Prime"
print("###########################")
print(f"{number} is {result}")


# now print prime numbers between 1 to 100
primes = []
# this primes are known as List in java
for value in range(2, 100):
    boolean = True
    index = 2
    while index <= value//index:
        if value % index == 0:
            boolean = False
            break
        index += 1
    if boolean:
        primes.append(value)
print(primes)


# print prime numbers between 1 to 100 using for else or while else

primes = []
for value in range(2, 100+1):
    divisor = 2
    while divisor <= value//divisor:
        if value % divisor == 0:
            break
        divisor += 1
    else:
        primes.append(value)
print(primes)

# printing prime numbers between 1 to 100 USING Pythonic version(all)
all_primes = [
    n
    for n in range(2, 101)
    if all(n % d != 0 for d in range(2, int(n**0.5)+1))
]
print(all_primes)
