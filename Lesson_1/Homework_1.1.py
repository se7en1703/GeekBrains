# Найдите сумму цифр трехзначного числа.
num = int(input("Введите любое трехзначное число: "))
last_digit = int(0)
sum = int(0)
for i in range(3):                   # Тело цикла
    last_digit = num % 10            # Нахождение последней цифры в числе
    sum = sum + last_digit           # Суммирование цифр
    num = num // 10                  # Удаление крайней цифры в числе
print(sum)