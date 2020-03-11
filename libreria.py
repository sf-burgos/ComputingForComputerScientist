import math;
def suma(A,A2):
    r=[0,0];
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
        r.append(multiplicacion(A[i],a))
    return r
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
def productoMatricesImaginarias(m1,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(m1[i],columna)
    return matriz
def productoVectoresImaginarios(c1,c2):
    ini = [0,0]
    for i in range(len(c1)):
        
        sumau = multiplicacion(c1[i],c2[i])
        #print(suma)
        ini = suma(ini,sumau)
    return ini
def AccionMatrizSobreVector(A,a):
    r = [];
    for i in range(len(A)):
        r.append(productoVectoresImaginarios(a,A[i]));
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
            r+= resta**2;
    r = r**0.5;
    return round(r,2);
def unitariaMatriz(A):
    M = [[(1,0) if j==1 else (0,0) for j in range(len(A))]for i in range(len(A))]
    deberiaSerUnitaria = True;
    for i in range(len(A)):
        if (len(A)!=len(A[i])):
            return "ERROR, las dimensiones deben ser n*n, no n*m, revise"
    if (productoMatricesImaginarias(A, adjuntaMatriz(A))==M): return deberiaSerUnitaria;
    else:
        deberiaSerUnitaria = False;
        return False;
def hermitianaMatriz(A):
    h = adjuntaMatriz(A);
    if h == A:
        return True;
    return False;

def productoTensorialImaginario(m1,m2):
    matriz = []
    for i in range(len(m1)):
        matM = [[]] *len(m2)
        for j in range(len(m1[i])):
            m3 = multiplicacionPorUnEscalarYMatriz(m1[i][j],m2)
            for k in range(len(m2)):
                
                matM[k] = matM[k] + m3[k]
        for k in range(len(m2)):
            matriz.append(matM[k])
    return matriz
##print(productoTensorialImaginario([[[1,1],[0,0]],[[1,0],[0,1]]],[[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]]))
##print(unitariaMatriz([[[1/math.sqrt(2),0]],[[0,1/math.sqrt(2)],[[0,1/math.sqrt(2)]],[[1/math.sqrt(2),0]]]))
##print(AccionMatrizSobreVector([[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],[[1,-3],[4,3],[-3,1]]))
##print(productoMatricesImaginarias([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]],[[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]))
#print(unitariaMatriz([[[1/1.41,0],[0,1/1.41]],[[0,1/1.41],[1/1.41,0]]]))
##print(hermitianaMatriz([[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]]))
##print(hermitianaMatriz([[[1,0],[3,-1]],[[3,1],[0,1]]]))




##print(AccionMatrizSobreVector([[[-1,5],[1,-7],[-6,3]],
##                             [[-3,-9],[2,-5],[-1,10]],
##                             [[-6,5],[6,-5],[3,-2]]],[[1,-3],[4,3],[-3,1]]))
#print(productoTensorialImaginario([[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],[[0.5,0],[0.09,0],[0.41,0]],[[0.5,0],[0.3,0],[0.2,0]]], [[[7/34,0],[14/34,0],[4/34,0],[9/34,0]],[[15/34,0],[6/34,0],[12/34,0],[1/34,0]],[[2/34,0],[3/34,0],[13/34,0],[16/34,0]],[[10/34,0],[11/34,0],[5/34,0],[8/34,0]]]))

#print(productoTensorialImaginario(    ))











