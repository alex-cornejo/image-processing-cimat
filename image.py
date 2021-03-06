from __future__ import division   # impone aritmética no entera en la división
from PIL import Image             # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
from main import normalize

I = Image.open("lena.png") #Cargar la imagen

plt.imshow(np.asarray(I))
#plt.show()                             #Ver imagen con Python

print (I.size, I.mode, I.format)        # Obtener tamaño, tipo (escala de grises, RGB

I1 = I.convert('L')                     # Convierte a escala de grises 
#I1.show()
print (I1.size, I1.mode, I1.format)
plt.imshow(np.asarray(I1))
#plt.show() 

a = np.asarray(I,dtype=np.float32)
a = normalize(a, 100, 250)
Image.fromarray(a.astype(np.uint8)).save("lena2.png")
print(a)

plt.imshow(a)
plt.show()
