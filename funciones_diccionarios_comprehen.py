import math

def lista(entero, funci):

    if funci == 1:
        resultado =  {  i : math.sin(i)  for i in range(1,entero + 1) }
    elif funci == 2:
        resultado =  {  i : math.con(i)  for i in range(1,entero + 1) }
    else:
        resultado =  {  i : math.tan(i)  for i in range(1,entero + 1) }
    

    return resultado



def run():

    msg = """ 
    Ahora elige que funcion quieres ejecutar:
    1. Seno
    2. Coseno
    3. Tangente
    
    """


    entero = int(input("Digite un numero entero: "))
    funci = int(input(msg))
    
    
    print(lista(entero, funci))


    

if __name__ == "__main__":
    run()
