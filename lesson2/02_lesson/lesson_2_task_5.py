def month_to_season(x):

        if x == 1 or x == 2:
            print("Зима")
        elif x >=3 and x <=5:
            print("Весна")
        elif x >=6 and x <= 8:
            print("Лето")
        elif x == 12:
            print("Зима")
        else:
            print("Неверное число")


month=int(input("Введите число: "))
month_to_season(month)
