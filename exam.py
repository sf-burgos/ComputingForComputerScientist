import libreria as c
import numpy as np;
import matplotlib.pyplot as plt;
import copy
from math import *;

def main():
    v=[[[0.45,0]],[[0.05,0]],[[0.3,0]],[[0.3,0]],[[0.2,0]] ]
    clicks=10;
    labels=['Pto. 0','Pto. 1','Pto. 2','Pto. 3']
    estado= [v[0][0][0],v[1][0][0],v[2][0][0],v[3][0][0]]
  
    index = np.arange(len(labels))
    #print(index)
    plt.bar(index,estado)
    plt.xlabel('ESTADO')
    plt.ylabel('VALOR')
    plt.xticks(index, labels, rotation=0)
    plt.title('Evolucion dinamica del sistema '+str(clicks)+' clicks de tiempo')
    plt.show()
##main()
def imprimirLosResultados(V,clicks):
    cadena = "Pto. ";
    labels = [];
    estado = [];
    for i in range(len(V)):
        labels.append(cadena+str(i+1))
        #print(V[i][0])
        estado.append(V[i])
        
    index = np.arange(len(labels))
    plt.bar(index,estado)
    plt.xlabel('ESTADO')
    plt.ylabel('VALOR')
    plt.xticks(index, labels, rotation=90)
    plt.title('Evolucion dinamica del sistema '+str(clicks)+' clicks de tiempo')
    plt.show() 

def potenciaDeMatrices(M,n):
    for i in range(len(M)):
        for j in range (len(M[0])):
            
            M[i][j]= c.potencia(M[i][j],n)
            
    return M;


def sistemasProbabilisticosDinamicos(ensamblado, ens, clicks):
    if clicks==0:
        bandera = ens;
        for i in range(len(bandera)):
            for j in range(len(bandera[0])):
                bandera[i][j]=c.modulo(bandera[i][j])**2
        print(bandera[0])   
        imprimirLosResultados(bandera[0], clicks)
        
    else:
        bandera = ens;
        for i in range(clicks):
            bandera = c.AccionMatrizSobreVector(ensamblado,ens[0])
        
        print(bandera)
        print(len(bandera))
    
        for i in range(len(bandera)):
            bandera[i]=c.modulo(bandera[i])**2
        print(bandera)   
        imprimirLosResultados(bandera, clicks)



    
##print(ejercicio([[[0.0, 0.0], [0.12558823529411764, 0.0], [0.18529411764705883, 0.0], [0.0, 0.0], [0.2511764705882353, 0.0], [0.37058823529411766, 0.0], [0.0, 0.0], [0.07176470588235294, 0.0], [0.10588235294117647, 0.0], [0.0, 0.0], [0.16147058823529412, 0.0], [0.23823529411764707, 0.0]], [[0.10294117647058823, 0.0], [0.01852941176470588, 0.0], [0.08441176470588234, 0.0], [0.20588235294117646, 0.0], [0.03705882352941176, 0.0], [0.16882352941176468, 0.0], [0.058823529411764705, 0.0], [0.010588235294117647, 0.0], [0.04823529411764706, 0.0], [0.1323529411764706, 0.0], [0.023823529411764705, 0.0], [0.10852941176470587, 0.0]], [[0.10294117647058823, 0.0], [0.06176470588235294, 0.0], [0.041176470588235294, 0.0], [0.20588235294117646, 0.0], [0.12352941176470587, 0.0], [0.08235294117647059, 0.0], [0.058823529411764705, 0.0], [0.03529411764705882, 0.0], [0.023529411764705882, 0.0], [0.1323529411764706, 0.0], [0.07941176470588235, 0.0], [0.05294117647058824, 0.0]], [[0.0, 0.0], [0.2691176470588235, 0.0], [0.39705882352941174, 0.0], [0.0, 0.0], [0.10764705882352942, 0.0], [0.15882352941176472, 0.0], [0.0, 0.0], [0.21529411764705883, 0.0], [0.31764705882352945, 0.0], [0.0, 0.0], [0.017941176470588235, 0.0], [0.026470588235294117, 0.0]], [[0.22058823529411764, 0.0], [0.039705882352941174, 0.0], [0.18088235294117647, 0.0], [0.08823529411764706, 0.0], [0.015882352941176472, 0.0], [0.07235294117647059, 0.0], [0.17647058823529413, 0.0], [0.031764705882352945, 0.0], [0.14470588235294118, 0.0], [0.014705882352941176, 0.0], [0.0026470588235294116, 0.0], [0.012058823529411764, 0.0]], [[0.22058823529411764, 0.0], [0.1323529411764706, 0.0], [0.08823529411764706, 0.0], [0.08823529411764706, 0.0], [0.052941176470588235, 0.0], [0.03529411764705883, 0.0], [0.17647058823529413, 0.0], [0.10588235294117647, 0.0], [0.07058823529411766, 0.0], [0.014705882352941176, 0.0], [0.008823529411764706, 0.0], [0.0058823529411764705, 0.0]], [[0.0, 0.0], [0.03588235294117647, 0.0], [0.052941176470588235, 0.0], [0.0, 0.0], [0.05382352941176471, 0.0], [0.07941176470588236, 0.0], [0.0, 0.0], [0.23323529411764704, 0.0], [0.34411764705882353, 0.0], [0.0, 0.0], [0.28705882352941176, 0.0], [0.4235294117647059, 0.0]], [[0.029411764705882353, 0.0], [0.005294117647058823, 0.0], [0.02411764705882353, 0.0], [0.04411764705882353, 0.0], [0.007941176470588236, 0.0], [0.036176470588235296, 0.0], [0.19117647058823528, 0.0], [0.03441176470588235, 0.0], [0.15676470588235292, 0.0], [0.23529411764705882, 0.0], [0.042352941176470586, 0.0], [0.19294117647058823, 0.0]], [[0.029411764705882353, 0.0], [0.01764705882352941, 0.0], [0.011764705882352941, 0.0], [0.04411764705882353, 0.0], [0.026470588235294117, 0.0], [0.017647058823529415, 0.0], [0.19117647058823528, 0.0], [0.11470588235294116, 0.0], [0.07647058823529412, 0.0], [0.23529411764705882, 0.0], [0.1411764705882353, 0.0], [0.09411764705882353, 0.0]], [[0.0, 0.0], [0.17941176470588235, 0.0], [0.2647058823529412, 0.0], [0.0, 0.0], [0.1973529411764706, 0.0], [0.2911764705882353, 0.0], [0.0, 0.0], [0.08970588235294118, 0.0], [0.1323529411764706, 0.0], [0.0, 0.0], [0.14352941176470588, 0.0], [0.21176470588235294, 0.0]], [[0.14705882352941177, 0.0], [0.026470588235294117, 0.0], [0.12058823529411765, 0.0], [0.16176470588235295, 0.0], [0.02911764705882353, 0.0], [0.13264705882352942, 0.0], [0.07352941176470588, 0.0], [0.013235294117647059, 0.0], [0.060294117647058824, 0.0], [0.11764705882352941, 0.0], [0.021176470588235293, 0.0], [0.09647058823529411, 0.0]], [[0.14705882352941177, 0.0], [0.08823529411764706, 0.0], [0.05882352941176471, 0.0], [0.16176470588235295, 0.0], [0.09705882352941177, 0.0], [0.06470588235294118, 0.0], [0.07352941176470588, 0.0], [0.04411764705882353, 0.0], [0.029411764705882356, 0.0], [0.11764705882352941, 0.0], [0.07058823529411765, 0.0], [0.047058823529411764, 0.0]]],[[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]],3))
##N = [[[0,0],[0.61,0],[0.9,0]],[[0.5,0],[0.09,0],[0.41,0]],[[0.5,0],[0.3,0],[0.2,0]]];
##M = [[[7/34,0],[14/34,0],[4/34,0],[9/34,0]],[[15/34,0],[6/34,0],[12/34,0],[1/34,0]],[[2/34,0],[3/34,0],[13/34,0],[16/34,0]],[[10/34,0],[11/34,0],[5/34,0],[8/34,0]]];
##resultadoTensorialDeEnsamble=c.productoTensorialImaginario(M,N);
##vectorPosicionN = [[[0,0],[1,0],[0,0]]];vectorPosicionM = [[[0,0],[0,0],[1,0],[0,0]]]
##
##resultadoTensorialDePosicion = c.productoTensorialImaginario(vectorPosicionN,vectorPosicionM);
##clicks = 0;
##sistemasProbabilisticosDinamicos(resultadoTensorialDeEnsamble,resultadoTensorialDePosicion,clicks);
##print(M[3][2]);
##print(N[1][2]);
##
##
##for i in range(len(resultadoTensorialDeEnsamble)):
##    for j in range(len(resultadoTensorialDeEnsamble[0])):
##        if resultadoTensorialDeEnsamble[i][j][0]==0.1411764705882353:
##            print(i,j,"hola");
M = [[[0,0],[1/sqrt(2),0],[1/sqrt(2),0],[0,0]],[[1/sqrt(2),0],[0,0],[0,0],[-1/sqrt(2),0]],[[1/sqrt(2),0],[0,0],[0,0],[1/sqrt(2),0]],[[0,0],[-1/sqrt(2),0],[1/sqrt(2),0],[0,0]]];
V = [[[0,0],[0,1],[0,0],[0,0]]]


sistemasProbabilisticosDinamicos(M,V,2);

