import string
digits = set(string.digits)
b_letters  = set(string.ascii_uppercase)
s_letters  = set(string.ascii_lowercase)



def checkio(data):
    """Checks user password"""
    if len(data) < 10:
        return False
    else:
        if not any(char in data for char in digits):
            return False
        if not any(char in data for char in b_letters):
            return False
        if not any(char in data for char in s_letters):
            return False
        
        return True
print(checkio.__doc__)
