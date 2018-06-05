import random
"""Guessing game again."""
number = random.randint(1, 20)
guessNum = 0
print("I'm thinking of a number between 1 and 20.")
for tries in range(1, 6):
    try:
        guess = int(input("Take a guess."))
        guessNum += 1
    
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            break
    except ValueError:
        print("Please enter a number")
if guess == number:
    print("Good job! You guessed my number in " + str(guessNum) + " tries.")
else:
    print("Try again")
-----------------------------------------------
def collatz(number):
    try:
        number = int(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
    except ValueError:
        print("Please enter a number")

    return number
    
number = input("Enter number: ")
collatz(number)

---------------------------------------------
def f(x):
    result = ''
    for item in x[:-1]:
        result += (item + ', ')
    result += ('and ' + x[-1])
    
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(f(spam))
------------------------------------------------
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid)):
    for y in range(len(grid)):
        if x < 6 and y < 9:
            
            print(grid[y][x], end='')
    print()
        

        

