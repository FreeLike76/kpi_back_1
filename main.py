import matplotlib.pyplot as plt
import numpy as np
import math


def getparams():
    """Фукнція відповідає за введення памраметрів та обробку помилок введення"""
    while True:
        try:
            x_start = int(input("Від: "))
            x_end = int(input("До: "))
            x_step = float(input("Крок: "))

            if (x_end - x_start) > x_step > 0:
                return x_start, x_end, x_step
            else:
                raise ValueError

        except ValueError:
            print("Помилка типу або хибно задано проміжок!")


def table(x, y):
    print("Таблиця значень:")
    for i in range(0, len(x)):
        print("X =", x[i], "\tY =", y[i])

# Введення параметрів, приклад: від -5 до 5, крок 0.01
x_start, x_end, x_step = getparams()
# Створюємо масив значень Х в проміжку розміром в проміжок/крок + 1
x = np.linspace(x_start, x_end, int((x_end - x_start) / x_step) + 1)
# y = f(x) = x / tan(x)
y = []
# Масив точок де функція невизначена
x_undef = []

# Для кожного х рахуємо значення функції, зберігаємо Х для яких функція не визначена (ділення на 0)
for i in range(0, len(x)):
    try:
        y.append(float(x[i]) / float(math.tan(x[i])))
    except ZeroDivisionError:
        x_undef.append(x[i])
# Видаляємо значення Х з масиву для яких функція не визначена
# Для відповідності значень у-х на графіку
for undef in x_undef:
    x = x[x != undef]

# Вивід таблиці значень
table(x, y)
# Вивід особливих точок
print("Функція не визначена на Х =", x_undef)

# Будуємо графік
plt.plot(x, y, c="b")
# Обмеження координат за введеними межами по х
plt.xlim([x_start, x_end])
# Показати plot
plt.show()
