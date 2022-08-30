from os import system, name

banner = "--------Bienvenido al juego--------"
banner2 = "Seleccione una opcion"
options = """1-Jugar\n
            0-Salir"""

# constantes
piedra = 1
papel = 2
tijeras = 3
jugar = 1
salir = 0

def main_menu():
    clear()
    print(banner)
    print("-"*(len(banner) - len(banner2))/2)
    print(banner2)
    print("-"*(len(banner) - len(banner2))/2)
    print(options)

def options_game(win_bot, win_client, bot_option):
    clear()
    print("="*20)
    print("Victorias Bot: "+ str(win_bot))
    print("Victorias Cliente: "+ str(win_client))
    print()
    if bot_option == piedra:
        print("El Bot escogio Piedra")
    elif bot_option == papel:
        print("El Bot escogio Papel")
    elif bot_option == tijeras:
        print("El Bot escogio Piedra")

    print("Elija una opcion")
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijeras")
    print("="*20)

def end_menu(result):
    clear()
    if result == "win":
        center = len(banner)/2 - len("Ganaste")
        print(" "*center +"-"*(len("Ganaste")+2)+ " "*center)
        print("-"*center + "|Ganaste|" + "-"*center)
        print(" "*center +"-"*(len("Ganaste")+2)+ " "*center)
    else:
        center = len(banner)/2 - len("Perdiste")
        print(" "*center +"-"*(len("Perdiste")+2)+ " "*center)
        print("-"*center + "|Perdiste|" + "-"*center)
        print(" "*center +"-"*(len("Perdiste")+2)+ " "*center)

    print("-"*(len(banner) - len(banner2))/2)
    print("Jugar de nuevo?")
    print(banner2)
    print("-"*(len(banner) - len(banner2))/2)
    print(options)

# Funcion que limpia la pantalla 
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
