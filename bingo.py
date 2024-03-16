import random

def generador_de_cartones():
    numeros_unicos = random.sample(range(1, 100), 15)
    carton = []
    for numero in numeros_unicos:
        carton.append(numero)
    return carton
def remover_numero_y_comprobar(tablero, numero):
    lista_vacia_index = -1
    for index, lista in enumerate(tablero):
        if numero in lista:
            lista.remove(numero)
            if not lista:  # Si la lista está vacía después de remover el número
                lista_vacia_index = index
                break
    return lista_vacia_index

numero_De_jugadores = int(input("cuantos jugadores son: "))
print("")
cartones = []
for i in range(numero_De_jugadores):
    input(f'Nombre del jugador {i+1}: ')
    print("")
    decision = input('1.Aleatorio   2.Elegir')
    if decision == '1':
        print(f'carton del jugador {i+1}')
        print("")
        carton = generador_de_cartones()
        carton.sort()
        cartones.append(carton)
        print(', '.join(map(str, carton)))
    else:
        carton = []
        for i in range(15 ):
            numero = int(input('numero: '))
            carton.append(numero)
        carton.sort()
        cartones.append(carton)
        print(', '.join(map(str, carton)))
            
    print("")

tablero = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99
]
input("Comenzar sorteo")
ganador = False

while tablero:
    
    
    elemento_azar = random.choice(tablero)
    print(f"Numero sorteado: {elemento_azar}")
    tablero.remove(elemento_azar)
    input('')
    
    for indice, sublista in enumerate(cartones):
        if elemento_azar in sublista:
            sublista.remove(elemento_azar)
            if not sublista:
                print(f"¡El jugador {indice + 1} ha ganado!")
                ganador = True
                break
    if not ganador:
        input('Presiona enter para continuar...')
        for indice, carton in enumerate(cartones):
            print(f"Jugador {indice + 1}")
            print(', '.join(map(str, carton)) or "Sin números")
            print("")
    else:
        break            
  
