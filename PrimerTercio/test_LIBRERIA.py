import libreria as c
##https://www.wolframalpha.com/examples/mathematics/numbers/complex-numbers/
def test_suma():
    assert c.suma([-3,2],[4,1])==[1,3], "DeberiaSer 1+3i"

def test_resta():
    assert c.resta([3,2],[7,5])==[-4,-3], "DeberiaSer -4-3i"

def test_multiplicacion():
    assert c.multiplicacion([3,5],[7,10])==[-29,65], "DeberiaSer -29+65i"
def test_division():
    assert c.division([3,5],[7,10])==[0.47651006711409394, 0.03355704697986577], "DeberiaSer 71/149+5/149i"
def test_modulo():
    assert c.modulo([3,5])==5.83, "DeberiaSer 5.83"
def test_conjugado():
    assert c.conjugado([3,5])==[3,-5], "DeberiaSer 3-5i"
def test_fase():
    assert c.fase([3,5])==59.04, "DeberiaSer 59.04"
def test_polar():
    assert c.polar([3,5])==[5.83,59.04], "DeberiaSer 5.83,59.04"
def test_cartesiano():
    assert c.cartesiano([5.83,59.03])==[3.0,5.0], "DeberiaSer 3+5i"
def test_potencia():
    assert c.potencia([2,2],2)==[0.0, 8.01], "DeberiaSer 0,8.01"

#TESTLABORATORIO2#
def test_sumaVector():
    assert c.sumaVector([[8,3],[-1,-4],[0,-9]],[[8,3],[2,5],[3,0]])==[[16, 6], [1, 1], [3, -9]], "DeberiaSer [[16, 6], [1, 1], [3, -9]]"
def test_inversoVector():
    assert c.inversoVector([[-5,2],[3,0],[0,-1]])==[[5, -2], [-3, 0], [0, 1]], "DeberiaSer [[5, -2], [-3, 0], [0, 1]]"
def test_multiplicacionDeVectores():
    assert c.multiplicacionDeVectores([(-2,5),(-1,-1),(2,-9)],[-1,1])==[[-3, -7], [2, 0], [7, 11]], "DeberiaSer [[-3, -7], [2, 0], [7, 11]]"
def test_sumaMatrices():
    assert c.sumaMatrices([[(-8,-3),(-6,-4),(0,-4)],[(-1,8),(6,-10),(8,-5)],[(4,0),(8,5),(-7,-9)]],[[(-7,-2),(-4,-2),(7,7)],[(5,9),(0,3),(6,-5)],[(1,5),(-6,-6),(5,8)]])==[[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]], "DeberiaSer [[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]]"
def test_inversoMatriz():
    assert c.inversoMatriz([[(7,3),(-1,7)],[(-9,-4),(-7,-9)]])==[[[-7, -3], [1, -7]], [[9, 4], [7, 9]]], "DeberiaSer 0,8.01"
def test_multiplicacionPorUnEscalarYMatriz():
    assert c.multiplicacionPorUnEscalarYMatriz([-2,3],[[[3,-2],[8,-4]],[[4,-10],[-2,-8]]])==[[[0, 13], [-4, 32]], [[22, 32], [28, 10]]], "DeberiaSer [[[0, 13], [-4, 32]], [[22, 32], [28, 10]]]"
def test_transpuestaMatriz():
    assert c.transpuestaMatriz([[[3,-2],[8,-4]],[[4,-10],[-2,-8]]])==[[[3, -2], [4, -10]], [[8, -4], [-2, -8]]], "DeberiaSer [[[3, -2], [4, -10]], [[8, -4], [-2, -8]]]"
def test_conjugadaMatriz():
    assert c.conjugadaMatriz([[[-6,1],[3,8]],[[2,-6],[3,0]]])==[[[-6,-1],[3,-8]],[[2,6],[3,0]]], "[[[-6,1],[3,8]],[[2,-6],[3,0]]]"
def test_adjuntaMatriz():
    assert c.adjuntaMatriz([[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]])==[[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]], "DeberiaSer [[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]]"
def test_productoDeDosMatrices():
    assert c.productoMatricesImaginarias([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]],[[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]])==[[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]], "DeberiaSer [[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]]"
def test_AccionMatrizSobreVector():
    assert c.AccionMatrizSobreVector([[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],[[1,-3],[4,3],[-3,1]])==[[54, -32], [0, 17], [41, 30]], "DeberiaSer [[54, -32], [0, 17], [41, 30]]"
def test_normaVector():
    assert c.normaVector([[4,5],[3,1],[0,-7]])==10.0, "DeberiaSer 10.0"
def test_distanciaEntreDosVectores():
    assert c.distanciaEntreDosVectores([[2,7],[4,-1],[2,-4]],[[7,8],[2,-8],[1,4]])==12.0, "DeberiaSer 12"
    assert c.distanciaEntreDosVectores([[9,-7],[-1,-6]],[[7,-8],[5,-9]])==7.07, "DeberiaSer 7.07"
def test_unitariaMatriz():
    assert c.unitariaMatriz([[[0,1],[1,0],[0,0]],[[0,0],[0,1],[1,0]],[[1,0],[1,0],[0,1]]])==False, "DeberiaSer 0,8.01"
def test_hermitianaMatriz():
    assert c.hermitianaMatriz([[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]])==True, "DeberiaSer 0,8.01"
def test_productoTensorial():
    assert c.productoTensorialImaginario([[[1,1],[0,0]],[[1,0],[0,1]]],[[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]])==[[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]], "DeberiaSer [[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]]"

if __name__=='__main__':
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_modulo()
    test_conjugado()
    test_fase()
    test_polar()
    test_cartesiano()
    test_potencia()

    #TESTLABORATORIO2#

    test_sumaVector()
 
    test_inversoVector()
    test_multiplicacionDeVectores()
    test_sumaMatrices()
    test_inversoMatriz()
    test_multiplicacionPorUnEscalarYMatriz()
    test_transpuestaMatriz()
    test_conjugadaMatriz()
    test_adjuntaMatriz()
    test_productoDeDosMatrices()
    test_AccionMatrizSobreVector()
    test_normaVector()
    test_distanciaEntreDosVectores()
    test_unitariaMatriz()
    test_hermitianaMatriz()
    test_productoTensorial()

    
    
    print('prueba exitosa')
    



