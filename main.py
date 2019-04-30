import numpy

def normalize(image, a, b):
	min = numpy.min(image)
	max = numpy.max(image)
	for i in range(len(image)):
		for j in range (len(image[i])):
			x=image[i][j]
			image[i][j]=a+((x-min)*(b-a))/(max-min)

	return image


image = numpy.array([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])

print min
print max

print (normalize(image, 0, 255))	
