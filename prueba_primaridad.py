def run():
    def esPrimo(numero):
        contador = 0
        for i in range(1,numero+1):
            if i == 1 or i == numero: #un numero primo es todo alquel que se solo se puede dividir ente 1 o el mismo numero
                continue
            if numero % i == 0: # si el resto de la divicion es 0 es un numero primo
                contador += 1
        if contador == 0:
            return True
        else:
            return False


    numero = int(input("Escribe un numero: "))
    if esPrimo(numero):
        print("es primo parcero")
    else: 
        print(" no es primo hermano ")

if __name__ == '__main__':
    run()