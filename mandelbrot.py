import imaginarios as p
def mandelbrot(z,c):
    resultados=[0 for i in range (30)];

    resultados[0] = p.suma(p.potencia(z,2),c);
    
    for i in range (1,len(resultados)):
        
        resultados[i] = p.suma(p.potencia(resultados[i-1],2),c);
        
        if p.modulo(resultados[i])>2:
            
            return False                                                                                                               ;


    return True;

def funcion_f(z,c):
    return p.suma(p.potencia(z,2),c)
def esta_en_mandelbrot(c):
    z=[0,0];
    contador=0;
    for i in range(30):
        contador=contador+1
        z = funcion_f(z,c)
        if p.modulo(z)>2.0:
            return False, contador

    return True,0

#print(esta_en_mandelbrot([0,1])


print(esta_en_mandelbrot([-3,0]))
