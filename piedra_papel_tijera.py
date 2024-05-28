import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
lagarto = 'lagarto'
posibilidades = [piedra, papel, tijera, lagarto]
listaGanadora = [[papel, piedra], [tijera, papel], [piedra, tijera], [lagarto, papel], [piedra, lagarto], [tijera, lagarto]]
listaPerdedora = [[piedra, papel], [papel, tijera], [tijera, piedra], [papel, lagarto], [lagarto,piedra], [lagarto,tijera]]


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
    contestacionUsuario = input("JUEGO : Piedra, papel, tijera y lagarto" + "\n" + "Quieres jugar? (s/n): ")
    if 's' in contestacionUsuario.lower():
        maquina = generarrandom()
        while True and 1 == 1:
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
                if jugar(jugador, maquina) == 1 and 1 == jugar(jugador, maquina):
                    print("Gana el usuario !!!")
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
