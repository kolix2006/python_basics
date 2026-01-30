from main import *

# 1 step check

print(get_sum(4, 7)) # 11

# 2 step check

print(count_capital_letters('Kim Phing Thao')) # 3

# 3 step check

print(decode_string('Success')) # )())())

# 4 step check

print(get_odd_count('24445')) # 4

# 5 step check

print("Тест 1 (Ключ, день, нет тревоги):", check_access(True, False, False, True))   # Тест 1 (Ключ, день, нет тревоги): True
print("Тест 2 (Ключ, ночь, нет тревоги):", check_access(True, False, False, False))  # Тест 2 (Ключ, ночь, нет тревоги): False
print("Тест 3 (Палец, ночь, нет тревоги):", check_access(False, True, False, False)) # Тест 3 (Палец, ночь, нет тревоги): True
print("Тест 4 (Палец, день, но ЕСТЬ тревога):", check_access(False, True, True, True)) # Тест 4 (Палец, день, но ЕСТЬ тревога): False
print("Тест 5 (Ключ И палец, день, нет тревоги):", check_access(True, True, False, True)) # Тест 5 (Ключ И палец, день, нет тревоги): True
print("Тест 6 (Ничего нет):", check_access(False, False, False, True))               # Тест 6 (Ничего нет): False
