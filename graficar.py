import numpy as np
import matplotlib.pyplot as plt
import mandelbrot as t

plano=np.zeros((400,700))

for parte_real in range(700):
    for parte_imaginaria in range(400):
        c = [parte_real/200-2.5, parte_imaginaria/200-1]
        pertenece,color = t.esta_en_mandelbrot(c)
        if pertenece:
            plano[parte_imaginaria,parte_real]=color
        else:
            plano[parte_imaginaria,parte_real]=color
plt.figure(figsize=(10,10))
plt.imshow(plano,"magma")
plt.show()
