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

    # Comprehensions solution
    # worker = cada uno de los diccionarios internos de DATA
    # name = voy a guardar solo la llave "name" de cada diccionario en DATA
    # if = (condicion) si el "language" es python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    # Comprehensions solution
    # worker = cada uno de los diccionarios internos de DATA
    # name = voy a guardar solo la llave "name" de cada diccionario en DATA
    # if = (condicion) si la "organization" es Platzi
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Solucion con filter (pero trae todas las llaves de los diccionarios)
    adults_filter = list(filter(lambda worker: worker["age"] > 18, DATA))

    # Solucion con map (trayendo solo la llave "name" de los diccionarios y usando el adults_filter)
    adults_map = list(map(lambda worker: worker["name"], adults_filter))

    # Comprehensions solution
    # worker = cada uno de los diccionarios internos de DATA
    # name = voy a guardar solo la llave "name" de cada diccionario en DATA
    # if = (condicion) si la "age" es mayor a 18
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    
    # Usamos map para crear una lista nueva de diccionarios
    # y agregamos una llave nueva llamada "old" con True a los mayores de 70 y False a los menores
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()