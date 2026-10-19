def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

<<<<<<< HEAD
    print("Сумма:", add(a, b))
=======
    print("Сумма чисел:", add(a, b))
>>>>>>> 66a9300f98127ec3185cfbac074f3d2536d32580
    print("Разность:", subtract(a, b))
    print("Произведение:", multiply(a, b))


if __name__ == "__main__":
    main()


