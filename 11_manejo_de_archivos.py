def read():
    numbers = []
    # r -> Solo lectura
    # w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
    # a -> Añadido (agregar contenido abajo). Crea el archivo si éste no existe  
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:  
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose", "Rocío"]
    # encoding => parametro con el que nos aseguramos que lo que leamos lo leamos bien sin caracteres especiales
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def overwrite():
    names = ["Ángel", "Nicolás", "Catita", "Lili", "Gonzo"]
    # encoding => parametro con el que nos aseguramos que lo que leamos lo leamos bien sin caracteres especiales
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    overwrite()


if __name__ == '__main__':
    run()