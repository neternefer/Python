#Słownie

#jedynki
def ones(number):
    part = number 
    if part == 1:
        return "jeden"
    elif part == 2:
        return "dwa"
    elif part == 3:
        return "trzy"
    elif part == 4:
        return "cztery"
    elif part == 5:
        return "pięć"
    elif part == 6:
        return "sześć"
    elif part == 7:
        return "siedem"
    elif part == 8:
        return "osiem"
    elif part == 9:
        return "dziewięć"
    
def elevens(number):
    part = number 
    if part == 11:
        return "jedenaście"
    elif part == 10:
        return "dziesięć"
    elif part == 12:
        return "dwanaście"
    elif part == 13:
        return "trzynaście"
    elif part == 14:
        return "czternaście"
    elif part == 15:
        return "piętnaście"
    elif part == 16:
        return "szesnaście"
    elif part == 17:
        return "siedemnaście"
    elif part == 18:
        return "osiemnaście"
    elif part == 19:
        return "dziewiętnaście"
    
def tens(number):
    part = number // 10
    mod = number % 10
    if mod == 0:
        return ten_one(part)
    else:
        return ten_one(part) + " " + ones(mod)

def ten_one(part):
    if part == 2:
        return "dwadzieścia"
    elif part == 3:
        return "trzydzieści"
    elif part == 4:
        return "czterdzieści"
    else:
        return ones(part) + "dziesiąt"
    
def hundreds(number):
    part = number // 100
    mod = number % 100
    if mod == 0:
        return hundred_one(part)
    else:
        if find_eleven(mod):
            return hundred_one(part) + " " + elevens(mod)
        elif mod < 10:
            return hundred_one(part) + " " + ones(mod)
        else:
            return hundred_one(part) + " " + tens(mod)

def hundred_one(part):
    if part == 1:
        return "sto"
    elif part == 2:
        return "dwieście"
    elif part == 3 or part == 4:
        return ones(part) + "sta"
    else:
        return ones(part) + "set"

def find_eleven(number):
    m = []
    for i in str(number):
        m.append(int(i))
    if m[0] == 1:
        return True
    
def thousands(number):
    part = number // 1000
    mod = number % 1000
    if mod == 0:
        return thousand_one(part)
    elif mod < 10:
        return thousand_one(part) + " " + ones(mod)
    elif mod >= 10 and mod < 20:
        return thousand_one(part) + " " + elevens(mod)
    elif mod >= 20 and mod < 100:
        return thousand_one(part) + " " + tens(mod)
    else:
        return thousand_one(part) + " " + hundreds(mod)
    
def find_e(number, index):
    m = []
    for i in str(number):
        m.append(int(i))
    if m[index] == 2 or m[index] == 3 or m[index] == 4:
        return True
    
def thousand_one(part):
    if part >= 10:
        if part < 20:
            return elevens(part) + " tysięcy "
        elif part < 100:
            return tens(part) + " tysięcy "
        else:
            if find_e(part, 2):
                return hundreds(part) + " tysięce "
            else:
                return hundreds(part) + " tysięcy "
    else:
        if part == 1:
            return "tysiąc"
        elif part == 2 or part == 3 or part == 4:
            return ones(part) + " tysiące"
        else:
            return ones(part) + " tysięcy"


def millions(number):
    part = number // 1000000
    mod = number % 1000000
    return million_one(part) + thousands(mod)
    
def million_one(part):
    if part < 10:
        if part == 1:
            return "milion " 
        elif part == 2 or part == 3 or part == 4:
            return ones(part) + " miliony " 
        else:
            return ones(part) + " milionów "
    elif part >= 10 and part < 20:
        return elevens(part) + " milionów "
    else:
        if find_e(part, 1):
            return tens(part) + " miliony "
        else:
            return tens(part) + " milionów "
        
            
def main(number):
    if number < 10:
        print(ones(number))
    elif number < 20 and number >= 10:
        print(elevens(number))
    elif number >= 20 and number < 100:
        print(tens(number))
    elif number >= 100 and number < 1000:
        print(hundreds(number))
    elif number >= 1000 and number < 1000000:
        print(thousands(number))
    else:
        print(millions(number))


main(75033007)
    
        
