from colorama import init,Style,Fore

init(autoreset=True)

def menu_opciones():
    print(
    Fore.GREEN + Style.BRIGHT + "===CAJERO AUTOMATICO===", 
    Fore.YELLOW + Style.BRIGHT + "\nMENÚ: \n"
    "1: CONSULTAR SALDO\n"
    "2: DEPOSITAR DINERO\n"
    "3: RETIRAR DINERO\n"
    "4: SALIR"
    )
    return int(input(Fore.GREEN + Style.BRIGHT + "Elige la opcion: "))
      
#saldo inicial
saldo_usuario = 100

#menu
while True:
    try:
        opcion = menu_opciones()
        if opcion == 1:
            print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT} \nSu saldo es: ${saldo_usuario}\n")
            continue
        elif opcion == 2:
            deposito = int(input(Fore.BLUE + Style.BRIGHT + "\nCuanto deseas Depositar: "))
            if deposito > 0:
                saldo_usuario += deposito
                print(f"\nDeposito satisfactorio, Saldo actual: ${saldo_usuario}\n")
                continue
        elif opcion == 3:
            retiro = int(input(Fore.CYAN + Style.BRIGHT + "\nCuanto deseas Retirar: "))      
            if retiro <= saldo_usuario:
               saldo_usuario -= retiro
               print(f"\nRetiro satisfactorio, Saldo actual: ${saldo_usuario}\n")
            else:
                print(Fore.RED + Style.BRIGHT + "\nSALDO INSUFICIENTE\n")
        elif opcion == 4:
            print(Fore.CYAN + Style.BRIGHT + "\nHASTA PRONTO")
            break
        elif opcion < 1 or opcion > 4:
            print(Fore.CYAN + Style.BRIGHT + "\nOpcion no existe\n")
            continue
    except ValueError :
        print(Fore.RED + Style.BRIGHT + "\nVuelve a intentarlo\n")
        