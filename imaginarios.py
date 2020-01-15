def main():
    print(suma([3,2],[7,5]));
    print(resta([3,2],[7,5]));
    print(productoPunto([3,2],[7,5]));

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
def productoPunto(A,A2):
    r=[0,0];
    r[0]= A[0]*A2[0];
    r[1]= A[1]*A2[1];
    return r[0]+r[1];
main()
