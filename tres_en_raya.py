import random 


def dibujarTablero(tablero):
    print('')
    print(' |   |')
    print(' ' + tablero [7] + '| ' + tablero[8] + '  |' + tablero[9])
    print(' |   |')
    print('--------')
    print(' |   |')
    print(' ' + tablero [4] + '| ' + tablero[5] + '  |' + tablero[6])
    print(' |   |')
    print('--------')
    print(' |   |')
    print(' ' + tablero [1] + '| ' + tablero[2] + '  |' + tablero[3])
    print(' |   |')
    print('')


def ingresaLetraJugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def quienComienza():
    if random.randint(0, 1) == 0:
        return 'La Computadora'
    else:
        return 'El Jugador'


def jugarDeNuevo():
    print('¿Deseas Volver A Jugar? (si/no)')
    return input(). lower(). startswith('s')


def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra


def esGanador(ta, le):
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or 
    (ta[4] == le and ta[5] == le and ta[6] == le) or 
    (ta[1] == le and ta[2] == le and ta[3] == le) or 
    (ta[7] == le and ta[4] == le and ta[1] == le) or 
    (ta[8] == le and ta[5] == le and ta[2] == le) or 
    (ta[9] == le and ta[6] == le and ta[3] == le) or 
    (ta[7] == le and ta[5] == le and ta[3] == le) or 
    (ta[9] == le and ta[5] == le and ta[1] == le))


def obtenerDuplicadoTablero(tablero):
    dupTablero = []
    for i in tablero:
        dupTablero.append(i)
    return dupTablero


def hayEspacioLibre(tablero, jugada):
    return tablero[jugada] == ''

def obtenerJugadaJugador(tablero):
    jugada = ''
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('')
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)


def elegirAzarDeLista(tablero, listaJugada):
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)
    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None


def obtenerJugadaComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    if hayEspacioLibre(tablero, 5):
        return 5
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])


def tableroCompleto(tablero):
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True


print('')
print('Bienvenido a tres en raya')


while True:
    elTablero = [''] * 10 
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print('')
    print(turno + ' irá primero.')
    juegoEnCurso = True 
    while juegoEnCurso:
        if turno == 'El jugador':
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades, has ganado')
                juegoEnCurso = False 
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'La Computadora'
        else:
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)
            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La computadora te ha vencido, has perdido')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'El jugador'
                
    if not jugarDeNuevo():
        break