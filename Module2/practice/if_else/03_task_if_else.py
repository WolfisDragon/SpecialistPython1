# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))
if a==b or c==b or a==c:
    print("YES")
else:
    print("NO")
