import random
class piedrapapeltijeralagarto:

    """
    .. include:: README.md
    """


piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
lagarto = 'lagarto'
posibilidades = [piedra, papel, tijera, lagarto]
listaGanadora = [[papel, piedra], [tijera, papel], [piedra, tijera], [lagarto, papel], [piedra, lagarto], [tijera, lagarto]]
listaPerdedora = [[piedra, papel], [papel, tijera], [tijera, piedra], [papel, lagarto], [lagarto,piedra], [lagarto,tijera]]


def generarrandom():
    """
    Esta funcion/metodo sirve para darme un random
    :return: str
    """
    eleccion = random.choice(posibilidades)
    return eleccion


def jugar(jugador, maquina):
    """
    Funcion para jugar
    :param jugador: str
    :param maquina: str
    :return: int
    """
    if [jugador, maquina] in listaGanadora:
        return 1
    elif [jugador, maquina] in listaPerdedora:
        return -1
    return 0
def main():
    contadorusuario = 0
    contadormaquina = 0
    intentos = int(input("Dime un numero de intentos, quien gane más en esos intentos es el vencedor: "))
    nombre = str(input("Dime tu nombre: "))
    contestacionUsuario = input("JUEGO : Piedra, papel, tijera y lagarto" + "\n" + "Quieres jugar? (s/n): ")
    while intentos != 0:

        if 's' in contestacionUsuario.lower():
            intentos -= 1
            maquina = generarrandom()
            while True:
                movimiento = input(
                    "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / 'l' para lagarto)"
                    " o eres un fucking cagado y te tienes que ir? Usa TERMINAR: ").lower()
                if movimiento.upper() == "TERMINAR":
                    print("Tienes miedo nena?")
                    quit()

                print(f"Elección del ordenador: {maquina}")
                if 'p' in movimiento or 'a' in movimiento or 't' in movimiento or 'l' in movimiento:
                    if 'p' in movimiento:
                        jugador = piedra
                    elif 'a' in movimiento:
                        jugador = papel
                    elif 't' in movimiento:
                        jugador = tijera
                    elif 'l' in movimiento:
                        jugador = lagarto
                    print(f"Elección del usuario: {jugador}")
                    if jugar(jugador, maquina) == 1:
                        print(f"Gana {nombre} !!! \n Te quedan {intentos} intentos")
                        contadorusuario +=1
                    elif jugar(jugador, maquina) == -1:
                        print(f"Gana el ordenador !!! \n Te quedan {intentos} intentos")
                        contadormaquina +=1
                    elif jugar(jugador, maquina) == 0:
                        print(f"Empate !!! \n Te quedan {intentos} intentos")
                    break
                else:
                    print("Entrada incorrecta. Vuelve a intentar.")
        elif 'n' in contestacionUsuario.lower():
            break
        else:
            print('Entrada incorrecta. Vuelve a intentar.' + "\n")

    if contadorusuario>contadormaquina:
        print(f"Ha ganado el usuario {nombre} con {contadorusuario}")
    elif contadorusuario<contadormaquina:
        print(f"Ha ganado la maquina con {contadormaquina}")
    else:
        print("Empate de Manual!!!!!")

if __name__ == '__main__':
    main()