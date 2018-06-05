#Jaka to liczba 2

import random

def ask_number(question, low, high):
    number = None
    while number not in range(low, high):
        number = int(input(question))
        return number
#Powitanie
print("\t\\ \\Witaj w Programie \'Jaka to liczba\'!\\ \\")
print("Mam na myśli liczbę z zakresu 1 - 100")
print("Czy jesteś w stanie ją odgadnąć mając do dyspozycji 10 prób?")
#Inicjalizacja zmiennych


#Gra
def main():
    tries = 0
    guess = random.randint(1, 100)
    low = 0
    high = 100
    number = ask_number("Podaj liczbę od 1 do 100: ", low, high)
    while tries < 10 and guess != number:
       print("Komputer mówi: ", guess)
       if guess < number:
          print("Za mała liczba")
       elif guess > number:
          print("Za duża liczba")
    
       tries += 1
       guess = random.randint(1, 100)

    if guess == number:
       print("Komputer mówi: ", guess)
       print("Zgadłeś!")
    else:
       print("Game over!")

    
#Wyjdź
main()
input("By zakończyć nacisnij Enter")
