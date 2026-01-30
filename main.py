# step 1

def get_sum(a, b):
    return a + b

# step 2

def count_capital_letters(text):
    count = 0
    capital_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for char in text:
        if char in capital_letters:
            count += 1
    return count

# step 3



# step 4

def get_odd_count(num: str) -> int:
    count = 0
    for n in num:
        if int(n) % 2 == 0 and int(n) != 0:
            count += 1
    return count

# step 5

