from random import randint as ri
ListaABC = [[ri(-100,100),ri(-100,100),ri(-100,100)] for i in range(100)]
for i,j in enumerate(ListaABC):
    a, b, c = j[0], j[1], j[2]
    discriminante = (b*b - 4*a*c)
    if discriminante == 0:
        solucion = -b/(2*a)
        ListaABC[i].append(solucion)
        #Tiene una unica solución
    elif discriminante > 0:
        x1 = (-b + (discriminante ** (1 / 2))) / (2 * a)
        x2 = (-b - (discriminante ** (1 / 2))) / (2 * a)
        ltemp = [x1, x2]
        ListaABC[i].append(ltemp)
        #Tiene dos soluciones
    else:
        ListaABC[i].append([])
        #No tiene solucion en los reales
    print(f'{str(i+1).zfill(3)}-->\t{j}')

