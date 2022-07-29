
moneda = input("Seleciona la moneda de tus pais 1 = Colombia ; 2 = México : ")
moneda = int(moneda)

if moneda == 1 :
    pesos = input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4402
    dolares = round(pesos / valor_dolar, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares" )

elif moneda == 2 :

    pesos_mexicanos = input("Cuantos pesos Mexicanos tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 0.049
    dolares = round(pesos_mexicanos / valor_dolar, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares" )

