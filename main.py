def get_text():
    pass


def gen_text():
    pass


def palindrome():
    pass


def result():
    pass


if __name__ == "__main__":
    while True:
        print("Выберете пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод резульата\n5. Завершение работы программы")
        x = int(input())
        if x == 1:
            get_text()
        elif x == 2:
            gen_text()
        elif x == 3:
            palindrome()
        elif x == 4:
            result()
        elif x == 5:
            exit()
        else:
            print("\nТакого пункта нету\n")
