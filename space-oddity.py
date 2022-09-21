"""
    Space Oddity

    Created by Naim & Elkin for the Interactive Systems class at Javeriana Cali.
    All rights reserved.

    Date creation: Sep 19, 2022
    Last modified: Sep 21, 2022
    Current version: 1.0.1
"""
from openal import *
import os
import time

# Position of the listener
listenerPos = (0, 0, 0)
# Velocity of the listener
listenerVel = (0, 0, 0)
# Orientation of the listener (first 3 elements are "at", second 3 are "up")
listenerOri = (0, 0, -1, 0, -1, 0)

ZORK = """
          ██████  ██▓███   ▄▄▄       ▄████▄  ▓█████     ▒█████  ▓█████▄ ▓█████▄  ██▓▄▄▄█████▓▓██   ██▓
        ▒██    ▒ ▓██░  ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀    ▒██▒  ██▒▒██▀ ██▌▒██▀ ██▌▓██▒▓  ██▒ ▓▒ ▒██  ██▒
        ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▒███      ▒██░  ██▒░██   █▌░██   █▌▒██▒▒ ▓██░ ▒░  ▒██ ██░
          ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄    ▒██   ██░░▓█▄   ▌░▓█▄   ▌░██░░ ▓██▓ ░   ░ ▐██▓░
        ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒   ░ ████▓▒░░▒████▓ ░▒████▓ ░██░  ▒██▒ ░   ░ ██▒▓░
        ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░   ░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒▓  ▒ ░▓    ▒ ░░      ██▒▒▒ 
        ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░  ▒    ░ ░  ░     ░ ▒ ▒░  ░ ▒  ▒  ░ ▒  ▒  ▒ ░    ░     ▓██ ░▒░ 
        ░  ░  ░  ░░         ░   ▒   ░           ░      ░ ░ ░ ▒   ░ ░  ░  ░ ░  ░  ▒ ░  ░       ▒ ▒ ░░  
              ░                 ░  ░░ ░         ░  ░       ░ ░     ░       ░     ░            ░ ░     
                                    ░                            ░       ░                    ░ ░     
"""

THANKS = """
                    ░▀█▀░█░█░█▀█░█▀█░█░█░█▀▀░░░█▀▀░█▀█░█▀▄░░░█▀█░█░░░█▀█░█░█░▀█▀░█▀█░█▀▀
                    ░░█░░█▀█░█▀█░█░█░█▀▄░▀▀█░░░█▀▀░█░█░█▀▄░░░█▀▀░█░░░█▀█░░█░░░█░░█░█░█░█
                    ░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░░░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀
"""


class State:
    def __init__(self, text="", options="", isTerminal=False, sourcesInBackground=False):
        self.text = text
        self.options = options
        self.sources = []
        self.children = []
        self.isTerminal = isTerminal
        self.sourcesInBackground = sourcesInBackground

    def playSources(self):
        if (self.sourcesInBackground):
            for source in self.sources:
                source.play()
        else:
            for source in self.sources:
                source.play()
                while source.get_state() == AL_PLAYING:
                    time.sleep(1)

    def stopSources(self):
        if (self.sourcesInBackground):
            for source in self.sources:
                source.stop()


A = State(
    text="""
    Se abren las puertas de tu cámara criogénica. Despertarse de este sueño usualmente toma unos minutos 
    antes de que tus músculos puedan responder. Pero estás consciente y puedes mover tu boca. Puedes
    escuchar alarmas.

    -- Comandante Robinson, lo he despertado de su sueño criogénico ya que se empezó el protocolo de seguridad 
       R.0.J.0 el cual requiere que un miembro de la tripulación esté despierto. --
    """,
    options="""
    1) Salir del bloque
    2) Investigar el bloque de criogénesis
    """,
)

B = State(
    text="""
    Caminas un poco por el pasillo y miras alrededor. Puedes ver las cápsulas del resto de la tripulación. 
    Hasta donde puedes ver parece que todos siguen en sueño criogénico. Pero el pasillo es largo y no puedes 
    ver hasta el final.
    """,
    options="""
    1) Salir del bloque
    2) Terminar de revisar el pasillo
    """,
)

C = State(
    text="""
    Caminas hacia el final del pasillo y puedes ver que en una de las últimas filas hay otra cápsula que está abierta. 
    A diferencia de la tuya, esta parece haber sido abierta hace mucho ya que no esta empañada y rodeada de vapor.
    """,
    options="""
    1) Examinar cápsula
    2) "Hay alguien ahí?"
    3) Salir del bloque
    """,
)

D = State(
    text="""
    Escuchas tu voz resonar en el pasillo y esperas unos segundos, pero no hay respuesta.
    """,
    options="""
    1) Examinar cápsula
    2) Salir del bloque
    """,
)

E = State(
    text="""
    La cápsula está vacía, y en la puerta puedes ver el nombre del tripulante: Srgto. Ryans. Te acuerdas haberlo 
    visto antes de abordar, era un hombre maciso y sombrio con canas a los lados y un corte militar. Él estaba 
    encargado de la seguridad de la tripulación.
    """,
    options="""
    1) Salir del bloque
    """,
)

F = State(
    text="""
    Entras al hub principal de la nave y puedes ver la luz de las alarmas circular alrededor de las paredes.
    """,
    options="""
    1) Ir a bloque de criogénesis
    2) Ir al centro de comando
    3) Ir al puerto
    4) Ir a la bodega
    """,
    sourcesInBackground=True,
)

G = State(
    text="""
    El centro de comando tiene la terminal principal de la nave y los controles para navegar la nave. Mirando por 
    la ventana puedes ver que la nave está dirigida hacia unos asteroides.
    """,
    options="""
    1) Usar terminal
    2) Pilotear la nave
    3) Volver al hub
    """,
    sourcesInBackground=True,
)

H = State(
    text="""
    No sabes mucho de piloteo, pero sabes lo suficiente para activar los propulsores para cambiar el rumbo de la nave 
    y evadir los asteroides.
    """,
    options="""
    1) Volver al centro de comando
    """,
)

I = State(
    text="""
    El puerto es un pasillo con varias puertas que llevan a las cápsulas de escape. Cerca de una de las puertas 
    puedes ver al androide en el suelo, botando chispas por su pecho. Ademas, puedes ver que una nave se ha acoplado 
    al puerto.
    """,
    options="""
    1) Inspeccionar androide
    2) Inspeccionar puerta
    """,
    sourcesInBackground=True,
)

J = State(
    text="""
    El androide tiene rasguños en su pecho de donde emanan las chispas. Tiene sus brazos frente a él como si estuviera 
    tratando de taparse la cara.
    """,
    options="""
    1) Volver
    """,
    sourcesInBackground=True,
)

K = State(
    text="""
    Te acercas a la terminal y activas los comandos de voz.

    -- Hola Comandante Robinson, ¿En qué te puedo ayudar hoy? --
    """,
    options="""
    1) Hacer un reporte de la situación actual
    2) Enviar un comunicado de ayuda
    3) Volver
    """,
)

L = State(
    text="""
    -- Una nave sobrepasó nuestro sistema de seguridad y logró parquear su nave en nuestro puerto. 
       Perdí comunicación con el androide CG42 hace 5 horas. Durante ese tiempo activé el protocolo R0J0, 
       parando el vuelo de hiperespacio y el estado criogénico del comandante para investigar. --
      """,
    options="""
    1) Volver
    """,
)

M = State(
    text="""
    -- En esta zona solo hay naves volando en hiperespacio y por tanto también debe estar dormida su tripulación. --
    """,
    options="1) Volver",
)

N = State(
    text="""
    Al entrar el la bodega puedes observar que varias de las cajas han sido movidas y escuchas una respiración
    a la distancia.
    """,
    options="""
    1) Volver
    2) Ir hacia la respiración
    """,
)

O = State(
    text="""
    Sigues derecho, moviendote hacia donde viene el sonido. Detras de una caja puedes ver una figura arrodillada 
    encima del cuerpo de un miembro de la tripulación. Puedes ver como está escarvando dentro de sus entrañas
    como si estuviera buscando algo! Se voltea lentamente para mirarte...
    """,
    options="",
)

T = State(isTerminal=True)

states = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]

soundTracks = [['A1.wav', 'A2.wav'], ['B1.wav'], ['C1.wav'], ['D1.wav'], ['E1.wav'], ['F1.wav'], ['G1.wav'], [
    'H1.wav', 'H2.wav'], ['I1.wav'], ['J1.wav'], ['K1.wav'], ['L1.wav'], ['M1.wav'], ['N1.wav', 'N2.wav'], ['O1.wav']]

for i in range(len(states)):
    for file in soundTracks[i]:
        states[i].sources.append(oalOpen("sounds/{0}".format(file)))

I.sources[0].set_looping(True)
F.sources[0].set_looping(True)
G.sources[0].set_looping(True)
J.sources[0].set_looping(True)

A.sources[0].set_position((10, 5, 5))
A.sources[1].set_position((0, 5, 5))
B.sources[0].set_position((0, 0, 1))
C.sources[0].set_position((0, 0, 3))
F.sources[0].set_position((0, 5, 1))
F.sources[0].set_gain(0.2)
G.sources[0].set_position((5, 1, 6))
G.sources[0].set_gain(0.4)
H.sources[0].set_position((0, -1, 1))
H.sources[1].set_position((0, 0, 0))
I.sources[0].set_position((0, 0, 10))
I.sources[0].set_gain(0.2)
J.sources[0].set_position((0, 0, 1))
J.sources[0].set_gain(0.7)
K.sources[0].set_position((5, 5, 5))
L.sources[0].set_position((0, 5, 1))
M.sources[0].set_position((0, 5, 1))
N.sources[0].set_gain(0.5)
N.sources[0].set_position((1, 1, 1))
N.sources[1].set_position((5, 0, 15))
O.sources[0].set_position((5, -1, 5))


A.children = [F, B]
B.children = [F, C]
C.children = [E, D, F]
D.children = [E, F]
E.children = [F]
F.children = [B, G, I, N]
G.children = [K, H, F]  # Cambiar G
H.children = [G]
I.children = [J, F]
J.children = [I]
K.children = [L, M, G]
L.children = [K]
M.children = [K]
N.children = [F, O]
O.children = [T]


def clear():
    if (os.name == 'posix'):
        return os.system('clear')


def startGame():
    trials = 0
    avoid_asteroid = False
    source = oalOpen(
        "sounds/initial-state.wav")
    source.set_gain(0.1)
    source.set_looping(True)
    source.play()
    print(ZORK)
    print("""
    ----------------------------------------------------------------------------------------------------
    |    Estás abordo del SS Olivo, una nave transportadora de cargamento de minerales recolectados    |
    |    en asteroides. Tu misión era la de recoger el cargamento en la galaxia de Miphokos y llevarlo |
    |    de vuelta a la tierra. Este viaje usualmente toma 20 años viajando a la velocidad de la luz.  |
    |    Para esto la tripulación debe estar bajo un sueño criogénico, ya que viajar a esta velocidad  |
    |    despierto usualmente termina en efectos detrimentales a la salud mental de la tripulación.    |
    ----------------------------------------------------------------------------------------------------
    """)
    time.sleep(5)
    input("Presione Enter para continuar...")
    current_state = A
    while (not current_state.isTerminal):
        clear()
        print(ZORK)
        if (not avoid_asteroid and trials >= 15):
            print("""
                    La nave ha colisionado con un asteroide y has muerto.
                """)
            time.sleep(5)
            break
        print(current_state.text)
        current_state.playSources()
        if (current_state.options == ""):
            print("""
    Esta criatura te ha devorado vivo.
                """)
            print()
            input("Presione Enter para finalizar el juego.")
            break
        print(current_state.options)
        if (current_state == H):
            G.children = [K, F]
            G.text = """
    El centro de comando tiene la terminal principal de la nave y los controles para navegar la nave.
            """
            G.options = """
    1) Usar terminal
    2) Volver al hub
            """
            avoid_asteroid = True
        valid = False
        while (not valid):
            option = input("Your option: ")
            try:
                option = int(option) - 1
                if (option < 0 or option >= len(current_state.children)):
                    print('Por favor ingrese una opción correcta.')
                else:
                    current_state.stopSources()
                    current_state = current_state.children[option]
                    valid = True
            except:
                print('Por favor ingrese una opción correcta.')
        trials += 1


def gameOptions():
    pass


def mainMenu():
    source = oalOpen(
        "sounds/main-menu.wav")
    source.set_looping(True)
    source.set_position((0, -10, 0))
    source.play()
    print(ZORK)
    print("""
                                    ░▀█░░▀▄░░░░█▀█░█░░░█▀█░█░█
                                    ░░█░░░█░░░░█▀▀░█░░░█▀█░░█░
                                    ░▀▀▀░▀░░░░░▀░░░▀▀▀░▀░▀░░▀░
    """)

    print("""
                                    ░▀▀▄░▀▄░░░░█▀█░█▀█░▀█▀░▀█▀░█▀█░█▀█░█▀▀
                                    ░▄▀░░░█░░░░█░█░█▀▀░░█░░░█░░█░█░█░█░▀▀█
                                    ░▀▀▀░▀░░░░░▀▀▀░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀
    """)

    print("""
                                    ░▀▀█░▀▄░░░░█▀▀░█░█░▀█▀░▀█▀
                                    ░░▀▄░░█░░░░█▀▀░▄▀▄░░█░░░█░
                                    ░▀▀░░▀░░░░░▀▀▀░▀░▀░▀▀▀░░▀░
    """)

    valid = False
    while (not valid):
        option = input("Your option: ")
        if (option == '1'):
            clear()
            print(ZORK)
            print("""


                                ░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░▀█▀░█▀█░█▀▀
                                ░▀▀█░░█░░█▀█░█▀▄░░█░░░█░░█░█░█░█
                                ░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀
            """)
            time.sleep(1)
            clear()
            print(ZORK)
            print("""


                                ░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░▀█▀░█▀█░█▀▀░░░
                                ░▀▀█░░█░░█▀█░█▀▄░░█░░░█░░█░█░█░█░░░
                                ░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░
            """)
            time.sleep(1)
            clear()
            print(ZORK)
            print("""


                                ░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░▀█▀░█▀█░█▀▀░░░░░░
                                ░▀▀█░░█░░█▀█░█▀▄░░█░░░█░░█░█░█░█░░░░░░
                                ░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░░▀░
            """)
            time.sleep(1)
            clear()
            print(ZORK)
            print("""


                                ░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░▀█▀░█▀█░█▀▀░░░░░░░░░
                                ░▀▀█░░█░░█▀█░█▀▄░░█░░░█░░█░█░█░█░░░░░░░░░
                                ░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░░▀░░▀░
            """)
            time.sleep(1)
            clear()
            source.stop()
            startGame()
            clear()
            print(ZORK)
            print(THANKS)
            valid = True
        elif (option == '2'):
            gameOptions()
            clear()
            print(ZORK)
            print(THANKS)
            valid = True
        elif (option == '3'):
            clear()
            print(ZORK)
            print(THANKS)
            valid = True
        else:
            print("Invalid option. Try again.")


def main():
    oalInit()

    if (not oalGetInit()):
        print("PyOpenAL failed to be initialized")
        return -1

    device = oalGetDevice()
    if (not device):
        print("unable to get device")
        return -1

    context = oalGetContext()
    if (not context):
        print("unable to get context")
        return -1

    listener = oalGetListener()
    listener.set_position(listenerPos)
    listener.set_velocity(listenerVel)
    listener.set_orientation(listenerOri)

    clear()

    mainMenu()


if __name__ == '__main__':
    main()
