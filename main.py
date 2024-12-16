import random
import string


def get_text():
    print("\nВведите текст")
    txt = str(input())
    return txt


def gen_text():
    print("\nВведите длинну текста")
    len_txt = int(input())
    all_symbols = string.ascii_uppercase + " "
    result = ''.join(random.choice(all_symbols) for _ in range(len_txt))
    return result


def palindrome(text):
    list_of_words = text.split()
    answer = []
    for word in list_of_words:
        if word == reversed(word):
            answer.append(word)
    return answer


def result(ans):
    if ans == []:
        print("Паллиндромов не обнаруженно")
    else:
        print(ans)


def text_writed():
    pass


def text_changed():
    pass



if __name__ == "__main__":
    text = ""
    ans = []
    while True:
        print("Выберете пункт меню\n1. Ввод исходных данных вручную\n2. Ввод исходных данных сгенерированных случайным образом\n3. Выполнение алгоритма по заданию\n4. Вывод резульата\n5. Завершение работы программы")
        x = int(input())
        if x == 1:
            text = get_text()
        elif x == 2:
            text = gen_text()
        elif x == 3:
            ans = palindrome(text)
        elif x == 4:
            result(ans)
        elif x == 5:
            exit()
        else:
            print("\nТакого пункта нету\n")
