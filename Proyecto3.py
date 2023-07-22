import os
import readchar

def clear_terminal_and_print(number):
    # Borra la terminal y muestra el nuevo número
    os.system('cls' if os.name == 'nt' else 'clear')
    print("nuevo numero", number)

def main():
    ingreso_mumero = 0

    while ingreso_mumero <= 50:
        # Esperar a que se presione la tecla 'n' en el teclado
        print("Presiona la tecla 'n'para continuar...")
        tecla = readchar.readkey()
        if tecla == 'n':
            # Borrar la terminal y mostrar el nuevo número
            clear_terminal_and_print(ingreso_mumero)

            # Incrementar el número en 1
            ingreso_mumero += 1

if __name__ == "__main__":
    main()