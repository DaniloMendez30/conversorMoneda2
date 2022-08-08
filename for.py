#def run():
#    for numero in range(10):
#        print(12 * numero)

#if __name__ == '__main__':
#    run()


#Recorer una cadena de caractereres

def run():
    # for i in range(10000):
    #    print(i)
    #    if i == 5678:
    #        break

    #for contador in range(1000):
    #    if contador % 2 != 0:
    #        continue
    #    print(contador)

    palabra = input("Escribe una palabra: ")
    letra = input("Escribe una letra: ")
    cont = 0
    
    for i in palabra:
        if i == letra:
            cont += 1
        else:
            continue
    print("la palabra " + palabra + " tiene " + str(cont) + " veces la letra " + letra )


if __name__ == '__main__':
    run()

