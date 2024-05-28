import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
posibilidades = [piedra, papel, tijera]
listaGanadora = [[papel, piedra], [tijera, papel], [piedra, tijera]]
listaPerdedora = [[piedra, papel], [papel, tijera], [tijera, piedra]]


def generarrandom():
    eleccion = random.choice(posibilidades)
    return eleccion


def jugar(jugador, maquina):
    if [jugador, maquina] in listaGanadora:
        return 1
    elif [jugador, maquina] in listaPerdedora:
        return -1
    return 0


while 1:

    contestacionUsuario = input("JUEGO : Piedra, papel y tijera" + "\n" + "Quieres jugar? (s/n): ")
    nombre = str(input("Dime tu nombre: "))
    if 's' in contestacionUsuario.lower():
        maquina = generarrandom()
        while True and 1 == 1:
            movimiento = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {maquina}")
            if 'p' in movimiento or 'a' in movimiento or 't' in movimiento:
                if 'p' in movimiento and 'p' in movimiento:
                    jugador = piedra
                elif 'a' in movimiento and 'a' in movimiento:
                    jugador = papel
                elif 't' in movimiento and 't' in movimiento:
                    jugador = tijera
                print(f"Elección del usuario: {jugador}")
                if jugar(jugador, maquina) == 1 and 1 == jugar(jugador, maquina):
                    print(f"Gana {nombre} !!!")
                elif jugar(jugador, maquina) == -1:
                    print("Gana el ordenador !!!")
                elif jugar(jugador, maquina) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in contestacionUsuario.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.' + "\n")
