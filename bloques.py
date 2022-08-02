def run():
    contador = 0
    LIMITE = 1000 # cuando tu colocar en mayusculas una variable es se convierte de tipoo constante es decir que no va cambiar
    potencia = 2**contador

    while potencia < LIMITE :
        print("2 elevado a " + str(contador) + " es igual a " + str(potencia) )
        contador = contador + 1
        potencia = 2**contador

if __name__ == '__main__':
    run()

