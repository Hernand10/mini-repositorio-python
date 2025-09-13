from colorama import Fore,init,Style
init(autoreset=True)

def listado():
    for j in compras:
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}- "
        f"{Fore.BLUE}{Style.BRIGHT}{j}")

print(
    f"{Fore.GREEN}{Style.BRIGHT}Bienvenido esta es tu lista del mercado\nEscribe el nombre de un producto o 'fin' para terminar"
    )

compras = []

while True:
    productos = input(f"{Fore.BLUE}{Style.BRIGHT}Producto: ")
    compras.append(productos)

    if productos == "fin".lower():
        compras.pop()
        if not compras:
            print(f"{Fore.RED}{Style.BRIGHT}La lista esta vacia")
            continue
        print(f"{Fore.RED}{Style.BRIGHT}Tu lista de compras es:")
        listado()
        while True:
            eliminar_producto = input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Deseas eliminar algun producto S/N: ").strip().lower()
            if eliminar_producto == "s":
                eliminar = input(f"{Fore.BLUE}{Style.BRIGHT}Que deseas eliminar: ")
                if eliminar in compras:
                    compras.remove(eliminar)
                    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista actualizada")
                    listado()
                    continue
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}El producto no esta en la lista")
                    continue
            elif eliminar_producto == "n":
                print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista actualizada")
                listado()
                break
            else:
                print("intenta de nuevo")
                continue
        break