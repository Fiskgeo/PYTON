from errno import EILSEQ


def fizz_buzz(x):
    for x in range(1, x + 1):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
                print("Fizz")
        elif x % 5 == 0:
                        print("Buzz")
        else:
           print(x)

num=int(input("Введите число: "))
fizz_buzz(num)