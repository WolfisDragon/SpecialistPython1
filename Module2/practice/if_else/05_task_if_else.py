# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

m = int(input("Введите номер месяца: "))
if m==12 or m==1 or m==2:
    print("Зима")
elif m==3 or m==4 or m==5:
    print("Весна")
elif m==6 or m==7 or m==8:
    print("Лето")
else:
    print("Осень")
