def is_phone_number(text):
    if len(text) != 12:
        return False

    for num in range(0,3):
        if not text[num].isdecimal():
            return False

    if text[3] != '-':
        return False

    for num in range(4,7):
        if not text[num].isdecimal():
            return False
        
    if text[7] != '-':
        return False
    
    for num in range(8,11):
        if not text[num].isdecimal():
            return False
    return True
