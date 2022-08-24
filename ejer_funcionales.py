
def run():

    #--------------------------------- podemos usar un filter con un list comprenhension
    lista_nombres = ["danilo","camilo","andres","andrea","carlos"]
   
    # for i in lista_nombres:
    #      if i[0] == "a":
    #         lista_nueva.append(i)
    #      else:
    #          continue
    
    for i in lista_nombres:
         lista_nueva = list(filter(lambda i : i[0] == "a", lista_nombres))
    print("los nombres que comienzan con la letra " + " a " + " son " + str(lista_nueva))

    #------------------------------------------------------------------------------------
    # lista1 = [23, 45, 67, 20]
    # lista2 = [47, 67, 87, 20]
    # iguales = []

    # for i in lista1:
    #     for j in lista2:
    #         if i == j:
    #             iguales.append(i)
    #         else: continue

    # print("las listas coinciden en: " + str(iguales))

    #-------------------------------------------------------------------------------------
            

    # lista = [5,10,20,30]
    # cont = 0
    # multi = 1
    

    # for i in lista:
    #     cont = cont + i 
    #     multi = multi * i
    
    # print("la suma de la lista es " + str(cont))
    # print("la multipicacion de la lista es " + str(multi))

    #--------------------------------------------------------------------------------------
   
#    initial = 0

#    number1 = int(input("digita el primer numero: "))
#    initial = number1

#    number2 = int(input("digita el digita el segundo numero: "))
   

#    if initial > number2:
#        pass
#    else: 
#        initial = number2

#    number3 = int(input("digita el digita el tercer numero: "))
   

#    if initial > number3:
#         print("el numero mayor de los tres es " + str(initial))
#    else: 
#        initial = number3
#        print("el numero mayor de los tres es " + str(initial))


if __name__ == "__main__":
    run()