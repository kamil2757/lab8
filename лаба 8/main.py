# main.py
import functions as fn

while True:
    print("\n--- МЕНЮ ---")
    print("1. Простое число")
    print("2. Факториал (рекурсия/цикл)")
    print("3. НОД и НОК")
    print("4. Совершенное число")
    print("5. Сумма цифр")
    print("6. Перевернуть строку")
    print("7. Палиндром")
    print("8. Бинарный поиск")
    print("9. Возведение в степень")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == '1':
        n = int(input("Число: "))
        print("Простое?", fn.is_prime(n))

    elif choice == '2':
        n = int(input("Число: "))
        print(f"Рекурсия: {fn.factorial(n)}, Цикл: {fn.factorial_iter(n)}")

    elif choice == '3':
        a, b = map(int, input("Два числа через пробел: ").split())
        print(f"НОД: {fn.gcd(a, b)}, НОК: {fn.lcm(a, b)}")

    elif choice == '4':
        n = int(input("Число: "))
        print("Совершенное?", fn.is_perfect(n))

    elif choice == '5':
        n = int(input("Число: "))
        print("Сумма цифр:", fn.sum_digits(n))

    elif choice == '6':
        s = input("Строка: ")
        print("Результат:", fn.reverse_string(s))

    elif choice == '7':
        s = input("Строка: ")
        print("Палиндром?", fn.is_palindrome(s))

    elif choice == '8':
        arr = list(map(int, input("Массив через пробел: ").split()))
        target = int(input("Искомое число: "))
        print("Индекс:", fn.binary_search(arr, target))

    elif choice == '9':
        a, b = map(int, input("База и степень через пробел: ").split())
        print("Результат:", fn.power(a, b))

    elif choice == '0':
        print("Выход...")
        break
    else:
        print("Нет такого пункта!")