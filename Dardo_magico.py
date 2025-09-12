import random
from colorama import Fore,Style,init
init(autoreset=True)

def numero_tablero():
    return random.randint(1,10)

print(
    Fore.BLUE + Style.BRIGHT + 
    "🎯 Debes ingresar un numero del 1 al 10 🎯\n🏆 Ganas al alcanzar 3 puntos 🏆 " 
    )
def juego():
    n = numero_tablero()
    score = 0
    score_max = 3
    intentos = 0
    intentos_max = 5
    while intentos < intentos_max:
        try:
            num_usuario = int(input(Fore.GREEN+ Style.BRIGHT + "🧐 Ingresa el numero: "  ))
            if num_usuario < 1 or num_usuario > 10:
                print(Fore.RED + Style.BRIGHT + "🤬 Valor fuera del rango 🤬") 
                continue
            intentos += 1
            print(f"{Fore.GREEN}{Style.BRIGHT}🥵 Llevas: {intentos} intentos 🥵")
            if num_usuario == n:
                score += 1
                print(f"{Fore.BLUE}{Style.BRIGHT}🎯 Acertaste, tu puntaje es: {score}🎯")
                numero_nuevo = n
                while numero_nuevo == n:
                    numero_nuevo = random.randint(1,10)
                n = numero_nuevo                
            else:
                print(f"{Fore.BLUE}{Style.BRIGHT}🎯 Tu puntaje es: {score}🎯")
            if score == score_max:
                print(f"{Fore.GREEN}{Style.BRIGHT} 🎉 Ganaste 🎉")
                break
        except ValueError as e:
            print(f"Valor invalido {e}")    
while True:
    juego()
    reinicio = input(Style.BRIGHT + Fore.BLUE + "😎 Desear volver a jugar 😎 S/N: ").upper()
    if reinicio != "S":
        print(Style.BRIGHT + Fore.BLUE + "\n😉 Nos vemos la proxima vez 😉")
        break
    