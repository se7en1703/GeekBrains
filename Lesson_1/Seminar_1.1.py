n = int(input("Сколько км проезжает за день Ваш автомобиль? "))
m = int(input("Сколько Вам нужно проехать? "))
x = m // n + (m % n > 0)
print(f"Ваш автомобиль проедет {m} км за {x} дней")
