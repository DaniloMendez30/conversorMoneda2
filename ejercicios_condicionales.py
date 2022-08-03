def run():

    tipo = """
Bienvenido a pizza danilo.
Elige una opción: 

1-Pizza vegetariana
2-Pizza no vegetariana

"""
    tipo_pizza = int(input(tipo))
    
    if tipo_pizza == 1:
        nombre_pizza = 'Pizza vegtariana'
        menu = """
        Elige un ingrediente: 
        1-Pimiento
        2-Tofu
        recuerda que las pizzas ya vienen con mozzarella y el tomate
        """
        ingrediente = int(input(menu))
        if ingrediente == 1:
            nombre_ingrediente = 'Pimiento'
            print(
            "Tu orden de una " + nombre_pizza + " con los ingredintes de: Mozzarela, Tomate y " + nombre_ingrediente)
        else:
            nombre_ingrediente = 'Tofu'
            print(
            "Tu orden de una " + nombre_pizza + " con los ingredintes de: Mozzarela, Tomate y " + nombre_ingrediente)

    else:
        nombre_pizza = 'Pizza no vegtariana'
        menu = """
        Elige un ingrediente: 
        1-Peperoni
        2-jamon
        3.Salmon
        recuerda que las pizzas ya vienen con mozzarella y el tomate
        """
        ingrediente = int(input(menu))
        if ingrediente == 1:
            nombre_ingrediente = 'Peperoni'
            print(
            "Tu orden de una " + nombre_pizza + " con los ingredintes de: Mozzarela, Tomate y " + nombre_ingrediente)
        elif ingrediente == 2:
            nombre_ingrediente = 'Jamon'
            print(
            "Tu orden de una " + nombre_pizza + " con los ingredintes de: Mozzarela, Tomate y " + nombre_ingrediente)
        else:
            nombre_ingrediente = 'Salmon'
            print(
            "Tu orden de una " + nombre_pizza + " con los ingredintes de: Mozzarela, Tomate y " + nombre_ingrediente)


if __name__ == '__main__':
    run()
