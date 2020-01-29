import math
"""
La librería soporta las siguientes operaciones con complejos:

Suma
Producto
Resta
División
Módulo
Conjugado
Conversión entre representaciones polar y cartesiano
Retornar la fase de un número complejo.

"""
def suma(A,A2):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la suma real en n3 y la suma imaginaria en n4
    """
    r=[-1,-1];
    r[0]= A[0]+A2[0];
    r[1]= A[1]+A2[1];
    return r;


def resta(A,A2):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la resta real en n3 y la suma imaginaria en n4
    """
    r=[0,0];
    r[0]= A[0]-A2[0];
    r[1]= A[1]-A2[1];
    return r;


def multiplicacion(a,b):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la multiplicacion real en n3 y la suma imaginaria en n4
    """
    first = a[0] * b[0]
    second = a[0] * b[1]
    third = a[1] * b[0]
    fourth = a[1] * b[1]
    ent = first-fourth
    imag = second+third
    r=[ent,imag]
    return r;

def division(A,A2):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la division real en n3 y la suma imaginaria en n4
    """
    numerador = multiplicacion(A,conju(A2))
    denominador = (A2[0]**2)+(A2[1]**2)
    ent = numerador[0]/denominador
    imag = numerador[1]/denominador
    return [ent,imag]


def division2(a,b):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la division real en n3 y la suma imaginaria en n4
    """
    arriba = multiplicacion(a,conjugado(b))
    abajo = (b[0]**2)+(b[1]**2)
    ent = arriba[0]/abajo
    imag = arriba[1]/abajo
    return [ent,imag]


def conjugado(A):
    """
    PreCondicion: un arreglo de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara el conjugado real en n3 y la suma imaginaria en n4
    """
    res = (A[0],A[1]*-1)
    return res


def modulo(A):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara el modulo real en n3 y la suma imaginaria en n4
    """
    res=((A[0]**2)+(A[1]**2))**0.5
    return res


def fase(a):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la fase real en n3 y la suma imaginaria en n4
    """
    
    res = math.atan2(a[0],a[1])
    return round(math.degrees(res),2)


def polar(a):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la polar real en n3 y la suma imaginaria en n4
    """
    r = modulo(a)
    ang = fase(a)
    return [r,ang]


def cartesiano(a):
    """
    PreCondicion: dos arreglos de la forma A[n1,n2] donde n1 es la parte reales y n2 es la parte imaginaria
    Post: un arreglo forma R[n3,n4] donde estara la cartesiano real en n3 y la suma imaginaria en n4
    """
    r = a[0]
    ang = a[1]
    coseno = math.cos(math.radians(ang))
    seno = math.sin(math.radians(ang))
    first = round((r * coseno),2)
    second = round((r * seno),2)
    return [first,second]

def potencia(A,e):
    mod = modulo(A[0])
    arg = fase(A[1])

    mod = mod**e
    arg = arg*e

    return cartesiano([mod,arg])

print(suma(potencia([0,0],[0,1])))
