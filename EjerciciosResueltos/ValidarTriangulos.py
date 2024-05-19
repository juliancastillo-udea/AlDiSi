#Solución
def ValidadorTipoTriangulo(a1, a2, a3, l1, l2, l3):
#Triangulo Equilatero, Acutangulo, Oblicuangulo
    if a1 == a2 and a2 == a3:
        if l1 == l2 and l2 == l3:
            return 'Equilatero, Acutangulo, Oblicuangulo'
#Triangulo 'Isoceles, Acutangulo, Oblicuangulo'
    if a1 == a2 or a1 == a3 or a2 == a3:
        if a1<90 and a2<90 and a3<90:
            if l1 == l2 or l1 == l3 or l2 == l3:
                return 'Isoceles, Acutangulo, Oblicuangulo'
#Triangulo 'Escaleno, Acutangulo, Oblicuangulo'
    if a1 != a2 and a1 != a3 and a2 != a3:
        if a1<90 and a2<90 and a3<90:
            if l1 != l2 and l1 != l3 and l2 != l3:
                return 'Escaleno, Acutangulo, Oblicuangulo'
#Triangulo 'Isoceles, Rectangulo'
    if a1 == a2 or a1 == a3 or a2 == a3:
        if a1==90 or a2==90 or a3==90:
            if l1 == l2 or l1 == l3 or l2 == l3:
                return 'Isoceles, Rectangulo'
#Triangulo 'Escaleno, Rectangulo'
    if a1 != a2 and a1 != a3 and a2 != a3:
        if a1==90 or a2==90 or a3==90:
            if l1 != l2 and l1 != l3 and l2 != l3:
                return 'Escaleno, Rectangulo'
#Triangulo 'Isoceles, Obtusangulo, Oblicuangulo'
    if a1 == a2 or a1 == a3 or a2 == a3:
        if a1>90 or a2>90 or a3>90:
            if l1 == l2 or l1 == l3 or l2 == l3:
                return 'Isoceles, Obtusangulo, Oblicuangulo'
#Triangulo 'Escaleno, Obtusangulo, Oblicuangulo'
    if a1 != a2 and a1 != a3 and a2 != a3:
        if a1>90 or a2>90 or a3>90:
            if l1 != l2 and l1 != l3 and l2 != l3:
                return 'Escaleno, Obtusangulo, Oblicuangulo'
    return 'Las condiciones no se cumplen para una validacion de un triangulo.'