def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else: 
        return False

def run(): #Es buan practica iniciar el codigo con un funcion y asi no va leer linia po linia
    palabra = input("Escribe una palabla: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else: 
        print("No es palindromo") 
    
if __name__ == "__main__":
    run()
