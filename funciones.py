#def imprimir_mensajes():
#    print('Mensaje especial: ')
#    print('Estoy aprendiando a usar funciones')  

# imprimir_mensajes()



def imprimir_mensaje(mensaje):
    print("Hola")
    print("como estas")
    print(mensaje)

opcion = int(input("Elige una opcion (1,2,3): "))
if opcion ==  1 :
    imprimir_mensaje("Elegiste la opcion 1")

elif opcion ==  2 :
     imprimir_mensaje("Elegiste la opcion 2")

elif opcion ==  3 :
     imprimir_mensaje("Elegiste la opcion 3")