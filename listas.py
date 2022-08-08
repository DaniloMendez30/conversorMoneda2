def run():
    #  asignatura = ( "Matemáticas ", "Física ", "Química ", "Historia " ,"Lengua ")
    #  nota = []
    
    #  for mat in asignatura:
    #     nota_materia = input("que nota sacaste en " + mat)
    #     nota.append(nota_materia)
    #  for i in range(len(nota)):
    #      print("La nota de la materia " + asignatura[i] + " es " + nota[i] )

    #----------------------------
    # ganadores = []
    # for numero_ganadores in range(1,5):
    #     loteria = input("cual es el " + str(numero_ganadores)  + " numero ganador de la loteria: ")
    #     ganadores.append(loteria)
    #     ganadores.sort()

    # for i in range(len(ganadores)):
    #     print("el " + str(i) + " numero ganador es " + ganadores[i])
    #----------------------------

   word = input("Introduce una palabra: ")
   vocals = ['a', 'e', 'i', 'o', 'u']
   for vocal in vocals: 
       times = 0
       for letter in word: 
           if letter == vocal:
               times += 1
       print("La vocal " + vocal + " aparece " + str(times) + " veces")

if __name__ == '__main__':
    run() 

