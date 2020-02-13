import math;
def suma(A,A2):
    r=[-1,-1];
    r[0]= A[0]+A2[0];
    r[1]= A[1]+A2[1];
    return r;
def resta(A,A2):
    r=[0,0];
    r[0]= A[0]-A2[0];
    r[1]= A[1]-A2[1];
    return r;
def multiplicacion(a,b):
    uno = a[0] * b[0];
    dos = a[0] * b[1];
    tres = a[1] * b[0];
    cuatro = a[1] * b[1];
    parte_entera = uno-cuatro;
    imaginaria = dos+tres;
    r=[parte_entera,imaginaria];
    return r;
def conjugado(A):
    r = [A[0],A[1]*-1];
    return r;
def division(a,b):
    numerador = multiplicacion(a,conjugado(b));
    denominador = (b[0]**2)+(b[1]**2);
    entera = numerador[0]/denominador;
    imaginaria = numerador[1]/denominador;
    r = [entera,imaginaria];
    return r
def modulo(A):
    r1 = ((A[0]**2)+(A[1]**2))**0.5;
    r = round(r1,2)
    return r;

def fase(A):
    res = math.atan2(A[1],A[0]);
    r = round(math.degrees(res),2);    
    return r;
def polar(A):
    mod = modulo(A);
    fas = fase (A);
    r = [round(mod,2),round(fas,2)];
    return r;
def cartesiano(A):
    x = (A[0]*math.cos(math.radians(A[1]))*1000)/(1000);
    angulo = ((1000*A[0]*math.sin(math.radians(A[1])))/1000);
    r = [round(x,2),round(angulo,2)];
    return r;
def potencia(A,e):
    mod = modulo(A);
    arg = fase(A);

    mod = mod**e;
    arg = arg*e;
    r = cartesiano([mod,arg]);
    return r;
#lab2
def sumaVector(A,B):
    r=[];
    for i in range(len(A)):
        r.append(suma(A[i],B[i]))
    return r;
def inverso(A):
    r=[A[0]*-1, A[1]*-1];
    return r;
def inversoVector(A):
    r=[];
    for i in range(len(A)):
        r.append(inverso(A[i]));
    return r;
def multiplicacionDeVectores(A,a):
    r=[];
    for i in range(len(A)):
        r.append(multiplicacion(A[i],a));
    return r;
def sumaMatrices(A,B):
    r=[];
    for i in range(len(A)):
        r1=[];
        for j in range(len(A)):
            r1.append(suma(A[i][j],B[i][j]));
        r.append(r1);
    return r;
def inversoMatriz(A):
    r=[];
    for i in range(len(A)):
        r.append(inversoVector(A[i]))
    return r;
def multiplicacionPorUnEscalarYMatriz(c1,A):
    r=[]
    for col in range(0,len(A)):
        
        v=[]
        for row in range(0,len(A[0])):
            v.append(multiplicacion(A[col][row],c1))
        r.append(v)
    return r
def transpuestaMatriz(A):
    r=[];
    for i in range(len(A[0])):
        col = [T[i] for T in A]
        r.append(col)
    return r;
def conjugadaMatriz(A):
    r=[];
    for i in range(len(A)):
        r1=[];
        for j in range(len(A[0])):
            r1.append(conjugado(A[i][j]));
        r.append(r1);
    return r;
def adjuntaMatriz(A):
    r=transpuestaMatriz(A);r=conjugadaMatriz(r);
    return r; 
def productoDeDosMatrices(A,B):
    r = [[0] * len(B[0]) for j in range(len(A))];
    for i in range(len(A)):
        for j in range(len(B[0])):
            r1 = [r2[j] for r2 in B];
            r[i][j] = multiplicacionDeVectores(A[i],r1);
    return r;
def AccionMatrizSobreVector(A,a):
    r = [];
    for i in range(len(A)):
        r.append(multiplicacionDeVectores(a,A[i]));
    return r;
def productoInterno(a,b):
    r = [0,0]
    for i in range(len(a)):
        c = conjugado(a[0]);
        s = multiplicacion(c,b[i]);
        r = suma(r,s)
    return r;
def normaVector(a):
    r = 0;
    for i in range(len(a)):
        for j in range(len(a[0])):
            r += (a[i][j])**2
    r = r**0.5
    return r;
def distanciaEntreDosVectores(a,b):
    r = 0;
    for i in range(len(a)):
        for j in range(len(b[0])):
            resta = b[i][j]-a[i][j];
            s+= resta**2;
    r = r**0.5;
    return r;
def unitariaMatriz(A):
    M=[[(1,0) if j==1 else (0,0) for j in range(len(A))]for i in range(len(A))]
    deberiaSerUnitaria = True;
    for i in range(len(A)):
        if (len(A)!=len(A[i])):
            return "ERROR, las dimensiones deben ser n*n, no n*m, revise"
    if (productoDeDosMatrices(A, adjuntaMatriz(A)==M)): return deberiaSerUnitaria;
    else:
        return False;
def hermitianaMatriz(A):
    h = adjuntaMatriz(A);
    if h == A:
        return True;
    return False;
def productoTensorial(A,B):
    return None;
    




print(productoDeDosMatrices([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,9]],[[5,8],[-6,8],[6,9]]],[[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,9]],[[5,8],[-6,8],[6,9]]]))

















