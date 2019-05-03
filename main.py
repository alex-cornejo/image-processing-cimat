import numpy
import matplotlib.pyplot as plt
from PIL import Image 

def normalize(image, a, b):
	min = numpy.min(image)
	max = numpy.max(image)
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j]=a+((x-min)*(b-a))/(max-min)

	return image

def histograma(image):
	vec=numpy.zeros(256)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			aux=image[i][j]
			vec[aux]+=1
	return vec


def obtAcumulativo(vec, max):
	vecresult=numpy.zeros(256)

	for i in range(max+1):
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

I = Image.open("lena.png") #Cargar la imagen

image = numpy.asarray(I,dtype=numpy.int32)

#image = numpy.array([[2, 2, 3],[4, 5, 6]])
x=histograma(image)
plt.plot(x)	
plt.show()
x=obtAcumulativo(x, 255)
x= ecualizar(x,255)

#print(x)
#plt.plot(x)	
#plt.show()

new_ma = toMatrix(x, image)
Image.fromarray(new_ma.astype(numpy.uint8)).save("lena9.png")

x2=histograma(new_ma)
plt.plot(x2)
plt.show()