from palabras import lista_palabras #importamos tanto la lista de palabras como el mognote
from monigote import etapas
import random
#Seleccionamos una palabra al azar de nuestra lista importada
palabra_oculta = random.choice(lista_palabras)

palabra_mostrada = []
for i in range(len(palabra_oculta)):
    palabra_mostrada.append("_")
# Definimos las vidas iniciales y una lista vacia para registrar las letras ya usadas
vidas = 6
letras_usadas = []

# Ciclo principal del juego que se ejecuta mientras queden vidas
while vidas > 0:
    print("-----------------------------------")
# Construimos la palabra actual con espacios para mostrarla en pantalla   
    palabra_actual = ""
    for l in palabra_mostrada:
        palabra_actual = palabra_actual + l + " "
    print("Palabra:", palabra_actual)
    print("Vidas restantes:", vidas)
    
    letra = input("Ingrese una letra: ")
# Validamos que la entrada sea  un solo caracter alfabetico y que tambien sea una letra 
    if len(letra) == 1 and letra.isalpha():# Convertimos la letra a mayuscula
        letra = letra.upper()
    
        # Verificar si ya se uso cpn un ciclo tradicional)
        ya_usada = False
        for pasada in letras_usadas:
            if pasada == letra:
                ya_usada = True
        # Si la letra no ha sido usada previamente y entonces la registramos
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

    # Verificar si ya completo la palabra osea si no faltan guiones
    le_faltan_guiones = False
    for l in palabra_mostrada:
        if l == "_":
            le_faltan_guiones = True
    # Si la palabra esta completa rompemos el ciclo while condición de victoria        
    if le_faltan_guiones == False:
        break

# Mensaje final para saber si ganaste o perdiste
gano = True
for l in palabra_mostrada:
    if l == "_":
        gano = False

if gano == True:
    print("¡FELICIDADES! ¡HAS GANADO EL JUEGO!")
    print("La palabra era:", palabra_oculta)
else:
    print("¡HAS PERDIDO! Te has quedado sin vidas.")
    print(etapas[6]) # Muestra el monigote final completo
    print("La solucion era:", palabra_oculta)