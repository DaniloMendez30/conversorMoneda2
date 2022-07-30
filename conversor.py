

menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""

opcion = int(input(menu))

if opcion == 1: 
	pesos = input('¿Cuántos pesos mexicanos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 21.5
elif opcion == 2: 
	pesos = input('¿Cuántos pesos colombianos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 3715.01
elif opcion == 3: 
	
	pesos = input('¿Cuántos pesos argentinos tienes?: ')
	pesos = float(pesos)
	tipo_de_cambio = 74.44
	print('Escribe una opción correcta: ')



dolares = pesos / tipo_de_cambio

dolares = round(dolares, 2)

dolares = str(dolares)


print('Tienes $' + dolares +' dólares')
