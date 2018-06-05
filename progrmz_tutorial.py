#Display powers of 2 using anonymous function
terms = int(input("Choose a larger number: "))
num = int(input("Choose number: "))
powers = list(map(lambda x: 2 ** x, range(terms)))
for i in range(terms):
    print("Power of 2 for " + str(i) + " is " + str(powers[i]))

#Find numbers divisible by another number

divisible = list(filter(lambda x: (x % num == 0), range(terms)))
print("Items divisible by " + str(num) + " are: " + str(divisible))

#Convert decimal to binary, octal and hexadecimal
num = int(input("Choose a number:"))
print("Binary form of {0} is {0:b}".format(num))
print("Octal form of " + str(num) + " is " + str(oct(num)))
print("Hex form of " + str(num) + " is " + str(hex(num)))

#Find ASCII value of character
print("ASCII value of A is " + str(ord("A")))

#Find Highest Common Factor
#1.Loops
def compute(x, y):
    for i in range(1, min([x, y]) + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

#2.Euclidean algorithm
def compute1(x, y):
    
    if x > y:
        smaller = y
        larger = x
    else:
        smaller = x
        larger = y
    mod = larger % smaller
    while mod > 0:
        if smaller % mod == 0:
            hcf = mod
            break
        else:
            mod = smaller % mod
    return hcf
--------------------------------
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#Find Least Common Multiple
def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm

#Print factors of number
def print_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

#Is it a number?
def is_it_num(x):
    if isinstance(x, (float, int)):
        return True
    if not isinstance(x, str):
        return False

def is_it_float(x):
    while True:
        try:
            return float(x)
        except ValueError:
            print("Give me a number")
weight = is_it_float(input("Your weight: "))
height = is_it_float(input("Your height: "))
bmi = str(round(weight /height**2), 2))
        

            
            
