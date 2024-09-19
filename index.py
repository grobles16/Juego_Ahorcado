from random import choice

lista = ['manzana', 'pera', 'mango']
vidas = 5

def escoger_palabra(lista):
    return choice(lista)

def solicitar_letra():
    abecedario = 'abcdefghijklmnñopqrstwxyz'
    bandera = False
    
    while not bandera:
        letra = input("Ingrese una letra para descubrir la palabra secreta: ")
        if letra in abecedario and len(letra) == 1:
            bandera = True
        else:
            print("- - - -  Ingrese una letra correcta - - - -")
    
    return letra


def validar_palabra(palabra_seleccionada, palabra_correcta):
    if palabra_seleccionada == palabra_correcta:
        return True
    return False

def descontar_vidas(vidas):
    
    if vidas == 0:
        print("*****************************************")
        print("*     F i n * D e l * J u e g o         *")
        print("*****************************************")
        
    else:
        vidas -= 1
        print("*****************************************")
        print(f"* Te quedan: {vidas} vida(s)")
        print("*****************************************")

    return vidas

def mostrar_palabra_guion(palabra):
    palabra_guiones = []
    for letras in palabra:
        palabra_guiones.append('_')
    return palabra_guiones

def intento(palabra_seleccionada, palabra_guion):

    index = 0
    bandera = False
    print(palabra_guion)
    opcion = solicitar_letra()

    while vidas >= 1:
        for letra in palabra_seleccionada:
            if letra == opcion:
                palabra_guion[index] = opcion
                bandera = True
            index += 1

        if validar_palabra(palabra_seleccionada, palabra_guion) == True:
            print("****** Ganaste ******")
            print("*   La palabra es   *")
            print(palabra_guion)
            return True
        
        if bandera == False:
            vidas = descontar_vidas(vidas)

        if vidas == 0:
            return descontar_vidas(vidas)
        
        index = 0
        bandera = False
        print(palabra_guion)
        opcion = solicitar_letra()
        print("\n")
        
palabra_seleccionada = list(escoger_palabra(lista))
palabra_guion = mostrar_palabra_guion(palabra_seleccionada)
intento(palabra_seleccionada, palabra_guion)