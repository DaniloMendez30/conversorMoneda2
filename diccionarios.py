def run():
    persona = {}
    continuar = True
    while continuar:
        clave = input('¿Qué dato quieres introducir? ')
        valor = input(clave + ': ')
        persona[clave] = valor
        print(persona)
        continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

    #   moneda = {
    #     'euro':'€', 
    #     'dollar':'$', 
    #     'yen':'¥'}
    #   menu = """
    #   1-euro
    #   2-dollar
    #   3-yen
    #   Elige una opción: """

    #   moneda_usuario =  input(menu)
        
    #   for mon in moneda.keys():
    #       if mon == moneda_usuario:
    #           print("el signo de " + mon + " es " + moneda[mon])
    #           break
    #       elif mon != moneda_usuario:
    #           continue   
    #       else: 
    #           print("esa moneda no existe")


if __name__ == '__main__':
    run()