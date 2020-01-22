import imaginarios as c
##https://www.wolframalpha.com/examples/mathematics/numbers/complex-numbers/
def test_suma():
    assert c.suma([-3,2],[4,1])==[1,3], "DeberiaSer 1+3i"

def test_resta():
    assert c.resta([3,2],[7,5])==[-4,-3], "DeberiaSer -4-3i"

def test_multiplicacion():
    assert c.multiplicacion([2,3],[7,5])==[13,13], "DeberiaSer 13+13i"

if __name__=='__main__':
    test_suma()
    test_resta()
    ##test_multiplicacion()
    print('prueba exitosa')
    



