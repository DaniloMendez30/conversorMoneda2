import random # modulo o paquete de funciones que nos permiten trabajar con la aleatoridad.

def run():

    aleatorio = random.randint(1,100)
    numero = int(input("Ingresa un numero entre 1 y 100: "))
         
    while numero != aleatorio:
        if numero > aleatorio:
            print("el numero es mas pequeño")
                 
        else:
            print("el numero es mas grande")

        numero = int(input("elige otro numero: "))

    print("Ganaste parcero !!! 🥳")
        

if __name__ == '__main__':
    run()