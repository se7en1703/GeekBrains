# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Crane = int(input("Сколько журавликов сделали дети? "))
Petya_and_Serg = int(Crane / 3)
Petya = int(Petya_and_Serg / 2)
Kate = int(Petya_and_Serg * 2)
print(f"Петя сделал {Petya} журавликов, Сережа сделал {Petya} журавликов, а Катя сделала {Kate} журавликов")