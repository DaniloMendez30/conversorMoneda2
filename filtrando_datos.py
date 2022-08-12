DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # traer solo el nombre de solo los que saben python con list comprenhesion
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    #traer solo el nombre de solo los que saben python con map & filters
    all_python_devs_fil = list(filter(lambda worker : worker["language"] == "python" , DATA))
    all_python_devs_map = list(map(lambda worker : worker["name"]  , all_python_devs_fil))

    #______________________________________________________________________

    # traer solo los que trabajan en platzy  con list comprenhesion
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    # traer solo los que trabajan en platzy  con map y filter
    all_Platzi_workers_fil =  list(filter(lambda worker : worker["organization"] == "Platzi", DATA))
    all_Platzi_workers_map =  list(map(lambda worker : worker["name"] , all_Platzi_workers_fil ))
 
    #_______________________________________________________________________
     
     # traer solo los mayores de edad  list comprenhesion
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]

    adults_fil =  list(filter(lambda worker :  worker["age"] > 18, DATA))
    adults_map =  list(map(lambda worker : worker["name"] ,  adults_fil ))

    # traer solo los mayores de edad  list comprenhesion

     #_______________________________________________________________________

    #traer todos los diccionarios y a cada uno agregarle el key ols y el valor true o false si es mayor a 70 años con map 
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #traer todos los diccionarios y a cada uno agregarle el key ols y el valor true o false si es mayor a 70 años con list comprehe
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]



    for worker in  old_people:
        print(worker)


if __name__ == '__main__':
    run()