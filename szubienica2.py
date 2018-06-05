#Szubienica
import random

#Zmienne
WORDS = ["MONTY", "PYTHON", "LAMA", "CAMELOT"]
word = random.choice(WORDS)
MAX_MISTAKES = len(word)
mistakes = 0
used = []
puzzle = " _ " * len(word)

#Powitanie
print("""Witaj w grze. Twoim zadaniem jest odgadnięcie słowa o jakim myślę.
         Masz do wykorzystania 7 szans.
      """)
print("Słowo o jakim myślę to", puzzle)


#Gra
while mistakes < 7 and puzzle != word:
    guess = input("Jaką literę wybierasz? ")
    guess = guess.upper()
    while guess in used:
        print("Już podałeś tą literę. Spóbuj ponownie")
        guess = input("Jaką literę wybierasz? ")
        guess = guess.upper()
    used += guess
    if guess in word:
        print("Zgadłeś!")
        new_puzzle = ""
        for i in range(len(word)):
            if guess == word[i]:
                new_puzzle += guess
            else:
                new_puzzle += puzzle[i]
        puzzle = new_puzzle
        
    
        
    else:
        print("Nie zgadłeś")
        mistakes += 1

if puzzle == word:
    print("Gratulacje. Słowo to:", word)
else:
    print("Przegrałeś. Słowo to:", word)

input("Naciśnij Enter by zakończyć")
                
