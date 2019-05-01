import numpy
import matplotlib.pyplot as plt

def normalize(image, a, b):
	min = numpy.min(image)
	max = numpy.max(image)
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j]=a+((x-min)*(b-a))/(max-min)

	return image

def histograma(image):
	vec=numpy.zeros(255)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			aux=image[i][j]
			vec[aux]+=1
	return vec


def obtAcumulativo(vec, max):
	vecresult=numpy.zeros(255)

	for i in range(max+1):
		if(i==0):
			vecresult[i]=vec[0]
		else:
			vecresult[i]=vec[i]+vecresult[i-1]
	return vecresult


image = numpy.array([[2, 2, 3],[4, 5, 6]])
x=histograma(image)
print (obtAcumulativo(x, 6))	
