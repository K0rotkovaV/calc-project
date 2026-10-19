def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сумма чисел:", add(a, b))
    print("Разность:", subtract(a, b))
    print("Произведение:", multiply(a, b))


if __name__ == "__main__":
    main()


