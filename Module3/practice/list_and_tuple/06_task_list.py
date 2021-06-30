# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

num1 = int(input())  # Первое число
num2 = int(input())  # Второе число

# TODO: your code here
good_nums = []

for n in range(num1, num2):
    if n % 3 == 0:
        good_nums.append(n)
print(good_nums)
