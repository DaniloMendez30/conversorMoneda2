def divisor(num):
    divisor = []

    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run(): #Es buan practica iniciar el codigo con un funcion y asi no va leer linia po linia
     
     
     try:
         num = int(input("Ingresa un numero: "))
         if num > 0:
              print(divisor(num)) 
              print("El programa termino. :) ")
         else: raise TypeError("No puedes ingresar un numero negativo")
         
     except ValueError as ve :
         print("No puedes ingresar texto")
     except TypeError  as ve2 :
         print(ve2)
     
    
if __name__ == "__main__":
    run()
