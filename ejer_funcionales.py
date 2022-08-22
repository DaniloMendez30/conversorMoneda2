


def run():
   
   initial = 0

   number1 = int(input("digita el primer numero: "))
   initial = number1

   number2 = int(input("digita el digita el segundo numero: "))
   

   if initial > number2:
       pass
   else: 
       initial = number2

   number3 = int(input("digita el digita el tercer numero: "))
   

   if initial > number3:
        print("el numero mayor de los tres es " + str(initial))
   else: 
       initial = number3
       print("el numero mayor de los tres es " + str(initial))


    

if __name__ == "__main__":
    run()