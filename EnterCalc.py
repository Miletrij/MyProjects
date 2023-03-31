import random
from colorama import init
from colorama import Fore
init()

a = random.randint(2, 9)
b = random.randint(2, 9)
c = a * b

print(f"Решите пример: {a} x {b}")

print(Fore.CYAN)

while input("Введите правильный ответ: ") != str(c):

    print(Fore.RED + f"Ой! Вы уверены? :( Попробуйте еще раз!")
    print(Fore.CYAN)

else:
    print(Fore.GREEN + "Поздравляем! Вы Гений!!!")
    print(Fore.RESET)

input("Нажмите Enter для выхода")