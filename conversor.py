def conversor(tipo_pesos,valor_dolar):
    pesos = float(input('¿Cuántos pesos ' + tipo_pesos + ' tienes?: '))
    tipo_de_cambio = valor_dolar
    dolares = pesos / tipo_de_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares +' dólares')

menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos
4-Real Brasileño

Elige una opción: 

"""

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos",21.5)

elif opcion == 2:
    conversor("colombianos",3715.01)

elif opcion == 3:
    conversor("argentinos",74.44)

elif opcion == 4:
    conversor("Brasileño",0.19)

else :
    print('Escribe una opción correcta: ')
    