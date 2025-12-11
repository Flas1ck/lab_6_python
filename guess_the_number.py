import random


def guess_the_number():
    print("Гра Вгадай число")
    print("Я загадав число від 1 до 100.")
    print("У тебе є 7 спроб, щоб його відгадати.")
    secret_number = random.randint(1, 100)
    attempts = 7
    for i in range(1, attempts + 1):
        print(f"\nСпроба №{i}")
        try:
            user_guess = int(input("Введи своє число: "))
        except ValueError:
            print("Це не число! Спроба втрачена.")
            continue
        if user_guess == secret_number:
            print(f" Вітаю! Ти вгадав число {secret_number} за {i} спроб(и)!")
            break
        elif user_guess < secret_number:
            print("Моє число БІЛЬШЕ.")
        else:
            print("Моє число МЕНШЕ.")
    else:
        print(f"\nТи програв! Спроби закінчилися. Було загадано число: {secret_number}")
if __name__ == "__main__":
    guess_the_number()
