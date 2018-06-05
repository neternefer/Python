#Count words in sentence
def count_words(sen):
    words = sen.split()
    return len(words)

#Count vowels
def count_vowels(sen):
    count = 0
    for item in sen.lower():
        if item in 'aeiouy':
            count += 1
    return count

#Return True if the number of Os and Xs in string is the same
def x_o(sen):
    x = 0
    o = 0
    for item in sen:
        if item == x:
            x += 1
        elif item == y:
            y += 1
    return x == y

#Change all numbers in sentence to '#'
def change_num(sen):
    new = ''
    for item in sen:
        if item.isnumeric():
            new += '#'
        else:
            new += item
    return new

#Find country with largest area
from countries import countries
largest = 0
for country in countries:
    if country["area"] > largest:
        largest = country["area"]


