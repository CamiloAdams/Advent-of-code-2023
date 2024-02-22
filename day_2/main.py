import sys
# sys.stdout = open('./input.txt', 'w')
# file = open('test.txt', 'r')
file = open('input.txt', 'r')
meals = file.readlines()

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

# crear donde guardar las variables
# dividir en :
# De la parte 1 tomar el id del juego
# De la parte 2 dividir en ;
# Recorrer el resultado
# Dividir en ,
# Recorrer resultados
# Dividir en " "
# Verificar si el valor consultado en parte 2 es mayor o igual que el guardado
# Si en alguna parte es mayor salir y no guardar
# Si es menor o igual, guardar el id del juego
ids = list()
#12 red cubes, 13 green cubes, and 14 blue cubes
bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for index, line in enumerate(meals):
    ilegal = False
    id, sets = line.split(":")
    sets = sets.split(";")
    for set in sets:
        set = set.split(',')
        for op in set:
            num, color = op.split()
            if int(num) > bag[color]:
                ilegal = True
                break
        if ilegal:
            break
    if not ilegal:
       ids.append(int(id.split()[1]))

print("Part 1:")
print(sum(ids))

sum = 0

for index, line in enumerate(meals):
    bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    ilegal = False
    id, sets = line.split(":")
    sets = sets.split(";")
    for set in sets:
        set = set.split(',')
        for op in set:
            num, color = op.split()
            if int(num) > bag[color]:
                bag[color] = int(num)
    mul = 1
    for value in bag.values():
        mul*=value
    sum += mul

print("Part 2:")
print(sum)
