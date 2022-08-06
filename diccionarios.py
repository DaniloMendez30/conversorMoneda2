def run():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }

    print(mi_diccionario['llave1'])

    poblacion_pais = {
        'argentina': 44943321,
        'Brasil':12123123123123,
        'Colombia': 3324234
    }

    for llave in mi_diccionario.keys():
        print(llave)   #imprime argentina, brasil, colombia

    for valores in mi_diccionario.values():
        print(valores) #imprime 4444443,121212123243,3324
    
    for pais, poblacion in mi_diccionario.items():
        print("La llave: '" + pais + "' contiene el item: " + str(poblacion)))

if __name__ == '__main__':
    run()