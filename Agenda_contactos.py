from colorama import Fore, Style, init

init(autoreset=True)

def menu():
    print(Fore.GREEN + Style.BRIGHT + "\n==== AGENDA DE CONTACTOS ====")
    print(Fore.YELLOW + Style.BRIGHT + "1: Agragar contacto")
    print(Fore.YELLOW + Style.BRIGHT + "2: Ver todos los contactos")
    print(Fore.YELLOW + Style.BRIGHT + "3: Buscar contactos")
    print(Fore.YELLOW + Style.BRIGHT + "4: Eliminar contacto")
    print(Fore.YELLOW + Style.BRIGHT + "5: Salir")
    return int(input(Fore.BLUE + Style.BRIGHT + "\nElige una opcion: "))

contactos = {}

while True:
    try:
        opcion = menu()
        if opcion == 1:
            clave = input(f"{Fore.GREEN}\nIngrese el nombre: ").title()
            valor = int(input(f"{Fore.GREEN}\nIngresa el numero: "))
            if clave in contactos:
                print(f"{Fore.BLUE}{Style.BRIGHT}\nEl contacto ya existe")
            else:
                contactos.update({clave: valor})
                print(f"{Fore.BLUE}{Style.BRIGHT}\nCONTACTO AGREGADO CORRECTAMENTE")
            continue
        elif opcion == 2:
            if not contactos:
                print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nLISTA DE CONTACTOS VACIA")
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nTUS CONTACTOS:\n")
                for clave, valor in contactos.items():
                    print(f"{Fore.BLUE}{Style.BRIGHT}{clave}= {Fore.GREEN}{Style.BRIGHT}{valor}")
        elif opcion == 3:
            clave_a_buscar = input("\nIgresa el nombre del contacto: ").title()
            valor = contactos.get(clave_a_buscar)
            if valor is not None:
                print(f"\n{Fore.BLUE}{Style.BRIGHT}{clave_a_buscar}: {Fore.GREEN}{Style.BRIGHT}{valor}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}El contacto no existe")
        elif opcion == 4:
            clave_a_eliminar = input(f"{Fore.RED}{Style.BRIGHT}\nIngrea el nombre que deseas eliminar: ").title()
            if clave_a_eliminar in contactos:
                del contactos[clave_a_eliminar]
                print(f"{Fore.BLUE}{Style.BRIGHT}\n{clave_a_eliminar} a sido eliminado")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\nEl contacto no existe")
        elif opcion == 5:
            salir = input(Fore.RED + Style.BRIGHT + "\nEstas seguro que deseas salir? S/N: ").upper()
            if salir == "N":
                continue
            elif salir == "S":
                 print(f"{Fore.YELLOW}{Style.BRIGHT}\nHASTA LA PROXIMA")
                 break
            else:
                print(Fore.RED + Style.BRIGHT + "\nOpcion invalida")
        elif opcion < 1 or opcion > 5:
            print(f"{Fore.WHITE}{Style.BRIGHT}\nOPCION NO EXISTE")

    except ValueError :
        print(Fore.RED + Style.BRIGHT +"\nValor invalido")
        