from palabras import lista_palabras
from monigote import etapas
import random

palabra_oculta = random.choice(lista_palabras)

palabra_mostrada = []
for i in range(len(palabra_oculta)):
    palabra_mostrada.append("_")

vidas = 6
letras_usadas = []


while vidas > 0:
    print("-----------------------------------")
    
    palabra_actual = ""
    for l in palabra_mostrada:
        palabra_actual = palabra_actual + l + " "
    print("Palabra:", palabra_actual)
    print("Vidas restantes:", vidas)
    
    letra = input("Ingrese una letra: ")

    if len(letra) == 1 and letra.isalpha():
        letra = letra.upper()
    
        # Verificar si ya se uso cpn un ciclo tradicional)
        ya_usada = False
        for pasada in letras_usadas:
            if pasada == letra:
                ya_usada = True
        
        if ya_usada == False:
            letras_usadas.append(letra)
            
            # ---  Verificar si la letra esta en la palabra oculta ---
            acerto = False
            for i in range(len(palabra_oculta)):
                if palabra_oculta[i] == letra:
                    palabra_mostrada[i] = letra
                    acerto = True
            
            if acerto == True:
                print("La letra esta en la palabra.")
            else:
                vidas -= 1
                print(" La letra no esta.")
                print(etapas[6 - vidas]) # Muestra el monigote segun los errores
        else:
            print("La letra ya se ha utilizado anteriormente.")
    else:
        print("Tiene que ser una sola letra y estar en el rango [A-Z].")

 