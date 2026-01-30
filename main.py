# step 1

def get_sum(a: int, b: int) -> int:
    return a + b

# step 2

def count_capital_letters(text: str) -> int:
    count = 0
    capital_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for char in text:
        if char in capital_letters:
            count += 1
    return count

# step 3

def decode_string(str):
    lower_str = str.lower()
    result = ''
    for char in str:
        if lower_str.count(char.lower()) == 1:
            result += '('
        else:
            result += ')'
    return result

# step 4

def get_odd_count(num: str) -> int:
    count = 0
    for n in num:
        if int(n) % 2 == 0 and int(n) != 0:
            count += 1
    return count

# step 5

def check_access(has_keycard: bool, has_fingerprint: bool, is_alarm: bool, is_daylight: bool) -> bool:
    if is_alarm == True:
        return False
    elif has_keycard == True and is_daylight == False:
        return False
    elif has_keycard == False and has_fingerprint == False:
        return False
    else:
        return True
