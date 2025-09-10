import random
from colorama import Fore,Style,init
init(autoreset=True)
def numsecreto():
    return random.randint(1, 20)
n = numsecreto()
def juego():
    intentos = 0
    max_intentos = 5
    while intentos < max_intentos:
        try:
            numusuario = int(input(Style.BRIGHT + Fore.MAGENTA + "🧐 Ingresa el número: \n"))
            if numusuario > 20 or numusuario < 1:
                print(Fore.RED + f"😏 Valor fuera del rango 😏, Intentos: {intentos}\n")
                continue
            intentos +=1
            if numusuario != n:
                if numusuario < n:
                    print(Fore.RED + f"😒 Demasiado bajo, sigue intentado 😒, intentos: {intentos}\n")
                elif numusuario > n:
                    print(Fore.RED + f"😒 Demasiado alto, Sigue intentado 😒, intentos: {intentos}\n")
            else:
                print(Style.BRIGHT + Fore.GREEN + "🥳 Adivinaste 🥳")
                break
        except ValueError as e:
            print(Fore.RED + f"💀 Valor invalido 💀, intentos: {intentos}{e}\n")
    else:
        print(Style.BRIGHT + Fore.RED + f"☠️ Game over ☠️\n☠️ El numero correcto era: {n} ☠️\n")
while True:
    print(
        Style.BRIGHT + Fore.MAGENTA + 
        "🤔 Debes adivinar el numero del 1 al 20 🤔\n🤩 Tienes 5 intentos 🤩"
        )
    juego()
    reinicio = input(Style.BRIGHT + Fore.BLUE + "😎 Desear iniciar a jugar 😎 S/N: ").upper()
    if reinicio != "S":
        print(Style.BRIGHT + Fore.BLUE + "\n😉 Nos vemos la proxima vez 😉")
        break
    