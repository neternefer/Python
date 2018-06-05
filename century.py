def century(year):
    """Return century from year.
       (int) -> (int)
       century(1905)
       >>>20
       century(1900)
       >>>19
    """
    century = 0
    last_digit = year % 10
    if year >= 1 and last_digit == 0:
        century = year // 100 
    else:
        century = year // 100 + 1
    return century

def equation(inp):
    lst = []
    stn = ""
    inp1 = inp.strip()
    for i in inp1[1:]:
        for j in inp1[2:]:
            if i == '-':
                stn = stn + i
            if j in ("123456789") and int(j) % 2 == 0:
                stn = stn + j
                print(stn)
    print(stn)
