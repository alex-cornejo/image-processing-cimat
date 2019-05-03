from __future__ import division   	# impone aritmética no entera en la división
from PIL import Image             	# funciones para cargar y manipular imágenes
import numpy as np                	# funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   	# funciones para representación gráfica

def normalize(image, a, b):
	min = np.min(image)
	max = np.max(image)
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j]=a+((x-min)*(b-a))/(max-min)
	return image

def histograma(image):
	vec=np.zeros(256)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			aux=image[i][j]
			vec[aux] = vec[aux] + 1
	vec = vec.astype(int)			# Convertir una matrix de tipo flotante a intero
	return vec

def obtAcumulativo(vec):
	vecresult=np.zeros(256)
	for i in range(len(vec)):
		if(i==0):
			vecresult[i]=vec[0]/sum(vec)
		else:
			vecresult[i]=vec[i]/sum(vec)+vecresult[i-1]
	return vecresult

def ecualizar(vec, range):
	ecualizado=range*vec
	ecualizado = ecualizado.astype(int)
	return ecualizado

def toMatrix(ec, image):
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j] = ec[x];
	return image

def imageNormalize():
	I = Image.open("lena_problema.jpg") #Cargar la imagen
	a = np.asarray(I,dtype=np.int32) 	#Convertimos la imagen a una matrix
	x=histograma(a)						# Se obtiene el histograma
	minA= int(input("Valor a "))
	maxB= int(input("Valor b "))
	a = normalize(a, minA, maxB) 		#Normalizamos la imagen con los datos que nos dan
	Image.fromarray(a.astype(np.uint8)).save("lena_norma.png")		#Guardamos la imagen.
	IN = Image.open("lena_norma.png") 	#Cargar la imagen
	aN = np.asarray(IN,dtype=np.int32) 	#Convertimos la imagen a una matrix
	xN=histograma(aN)						# Se obtiene el histograma
	I.show()							#Mostramos la imagen original
	plt.title('Histograma')
	plt.grid(True)
	plt.plot(x)
	plt.show()

	IN.show()							#Mostramos la imagen ecualizada
	plt.title('Histograma')
	plt.grid(True)
	plt.plot(xN)
	plt.show()

def imageEcualiza():
	I = Image.open("lena_problema.jpg") 	#Cargar la imagen
	image = np.asarray(I,dtype=np.int32)	#Convertimos la imagen a una matrix
	x=histograma(image)						# Se obtiene el histograma

	xA = obtAcumulativo(x)
	xAE= ecualizar(xA,255)

	new_ma = toMatrix(xAE, image)
	Image.fromarray(new_ma.astype(np.uint8)).save("lena_contra.png")
	IE = Image.open("lena_contra.png") 	#Cargar la imagen
	x2=histograma(new_ma)				# Se obtiene el histograma
	x2A = obtAcumulativo(x2)

	I.show()
	plt.title('Histograma')
	plt.grid(True)
	plt.plot(x)
	plt.show()

	IE.show()
	plt.title('Histograma')
	plt.grid(True)
	plt.plot(x2)
	plt.show()

	plt.title('Histograma Acumulativo')
	plt.grid(True)
	plt.plot(x2A)
	plt.show()
	plt.clf()




# Código para la parte A
imageNormalize()

input()
# Código para la parte B
imageEcualiza()
