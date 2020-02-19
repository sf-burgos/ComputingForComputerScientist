import libreria as c
import numpy as np;
import matplotlib.pyplot as plt;

def main():
    v=[ [[0.45,0]],[[0.05,0]],[[0.3,0]],[[0.3,0]],[[0.2,0]] ]
    clicks=10;
    labels=['Pto. 0','Pto. 1','Pto. 2','Pto. 3']
    estado= [v[0][0][0],v[1][0][0],v[2][0][0],v[3][0][0]]
  
    index = np.arange(len(labels))
    print(index)
    plt.bar(index,estado)
    plt.xlabel('ESTADO')
    plt.ylabel('VALOR')
    plt.xticks(index, labels, rotation=0)
    plt.title('Evolucion dinamica del sistema '+str(clicks)+' clicks de tiempo')
    plt.show()
main()
def matrizDinamicaConAccion(v,col):
   # un click    
    print("matriz v");
    for i in range(len(v)):
        print(*v[i]);
    r = c.AccionMatrizSobreVector(v,col);

    print("vector col");
    print(col);

    print("matriz c accion v");
    print(r);
    
v = [[(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(1,0)],[(0,0),(1,0),(1,0),(0,0)],[(1,0),(0,0),(0,0),(0,0)]];
col = [(0,0),(0,0),(0,0),(1,0)];
clicks = 100
##matrizDinamicaConAccion(v,col);

def matrizDinamicaConAccionClicks(v,col, clicks):
    if clicks==1:
        matrizDinamicaConAccion(v,col);
    else:
        for i in range(clicks-1):
            v = c.productoMatricesImaginarias(v,v)
            print(v)
        
    
    print(c.AccionMatrizSobreVector(v,col))

matrizDinamicaConAccionClicks(v,col, clicks-1);
