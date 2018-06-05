#Wymieszane litery
import random
#Losowanie słowa z listy
WORDS = (["czerwony", "czeryonw"], ["zielony", "zienoyl"],
         ["żółty", "żóytł"], ["niebieski", "nieesibk"], ["czarny", "cznyra"])
random_choice = random.choice(WORDS)
random_word = random_choice[0]
clue = random_choice[1]
                                                            
#Wymieszanie liter
anagram = ""
word = random_word

for letter in range(len(word)):
    index = random.randrange(len(word))
    anagram += word[index]
    word = word[:index] + word[index + 1:]
    
#Powitanie i pobranie informacji
print("Welcome to the game. Your aim is to recognize the word.")
print("\nYour anagram is: " + anagram)
user_guess = input("Enter your guess: ")
          
#Gra
points = 10
tries = 0

while user_guess != random_word:
    tries += 1
    print("\nWrong! Try again")
    if tries >= 2 and points > 0:
       user_clue = input("Do you need a clue? Y/N: ")
       if user_clue == "Y":
          print(clue)
          points -= 2
          user_guess = input("Enter your guess: ")
       else:
          user_guess = input("Enter your guess: ")
    else:
        user_guess = input("Enter your guess: ")
    
    
if user_guess == random_word:
    print("\nYou win! You get " + str(points) + " points!")     


#Koniec
print("Press Enter to exit")
    
                             
