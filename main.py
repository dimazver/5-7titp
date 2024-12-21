import random
import string

def get_text():
    print("\nВведите текст")
    return str(input())

def gen_text():
    print("\nВведите длину текста")
    len_txt = int(input())
    all_symbols = string.ascii_uppercase + " "
    return ''.join(random.choice(all_symbols) for _ in range(len_txt))

def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    list_of_words = text.split()
    return [word for word in list_of_words if is_palindrome(word)]

def display_result(ans):
    (not ans and print("Палиндромов не обнаружено")) or print(ans)

def text_writed(txt):
    return txt != ""

def main():
    text = ""
    ans = []
    writed = False
    chandeg = False

    while True:
        print(
            "Выберите пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод результата\n5. Завершение работы программы")
        x = int(input())

        if x == 1:
            text = get_text()
            writed = text_writed(text)
            chandeg = False
        elif x == 2:
            text = gen_text()
            writed = text_writed(text)
            chandeg = False
        elif x == 3:
            if writed:
                ans = find_palindromes(text)
                chandeg = True
            else:
                print("Сначала введите текст")
        elif x == 4:
            if chandeg:
                display_result(ans)
            else:
                print("Сначала проверьте текст на палиндромы")
        elif x == 5:
            break
        else:
            print("\nТакого пункта нет\n")

if __name__ == "__main__":
    main()
