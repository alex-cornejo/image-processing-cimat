from __future__ import division   	# impone aritmética no entera en la división
from PIL import Image             	# funciones para cargar y manipular imágenes
import numpy as np                	# funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   	# funciones para representación gráfica
import matplotlib.pyplot as plt

def normalize(image, a, b):
	min = np.min(image)
	max = np.max(image)
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j]=a+((x-min)*(b-a))/(max-min)

	return image

def histograma(image):
	vec=np.zeros(255)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			aux=image[i][j]
			vec[aux] = vec[aux] + 1
	vec = vec.astype(int)			# Convertir una matrix de tipo flotante a intero
	return vec

def obtAcumulativo(vec):
	vecresult=np.zeros(255)
	for i in range(len(vec)):
		if(i==0):
			vecresult[i]=vec[0]
		else:
			vecresult[i]=vec[i]+vecresult[i-1]
	return vecresult

def imageNormalize():
	I = Image.open("lena_problema.jpg") #Cargar la imagen
	a = np.asarray(I,dtype=np.float32) 	#Convertimos la imagen a una matrix
	minA= int(input("Dame el valor de a "))
	maxB= int(input("Dame el valor de b "))
	a = normalize(a, minA, maxB) 		#Normalizamos la imagen con los datos que nos dan
	Image.fromarray(a.astype(np.uint8)).save("lena_norma.png")		#Guardamos la imagen.
	IN = Image.open("lena_norma.png") 	#Cargar la imagen
	I.show()							#Mostramos la imagen original
	IN.show()							#Mostramos la imagen ecualizada



# Código para la parte A
# imageNormalize()

# Código para la parte B
I = Image.open("lena_problema.jpg") #Cargar la imagen
a = np.asarray(I,dtype=np.float32) 	#Convertimos la imagen a una matrix
a = a.astype(int)
print(a)						#Convertir una matrix de tipo flotante a intero
x=histograma(a)
plt.title('Histograma')
plt.grid(True)
plt.plot(x)
plt.show()

xA = obtAcumulativo(x)


print (obtAcumulativo(x))






# image = np.array([[2, 2, 3],[4, 5, 6]])





