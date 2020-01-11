from matplotlib import pyplot as plt
import numpy as np

tx = np.array([0, 1, 2, 2, 3, 4, 5])
ty = np.array([0, 2, 2, 3, 4, 4, 5])

def error(a):
	y_pred		= tx * a
	y_observed	= ty 
	size		= len(tx)

	diff = sum((y_pred - y_observed)**2)/size/2
	return diff


def derror(a):
	size = len(tx)
	return -sum(tx * (ty - a * tx)) / size


def descent_gradient(a=-20, taux = 400000):
	grad = 100.0 
	while True:
		grad = derror(a) 
		g = grad/ taux
		if -0.5 <= grad <= 0.5:
			return a
		a += -g

def estimation(a, x):
	return (a * x)

ta = []
tb = []
# for i in numpy.arange(0, 5.5, 0.5):
	# print(i, end=', ')
for i in np.arange(0, 2, 0.1):
	ta.append(error(i))
	tb.append(i)
plt.scatter(tx, ty, c = 'blue')
plt.scatter(tb, ta, c = 'red')
a = 0;
plt.plot([0, 5], [estimation(a, 0), estimation(a, 5)], color = 'green', linestyle = 'solid')
a = descent_gradient(a);
plt.plot([0, 5], [estimation(a, 0), estimation(a, 5)], color = 'red', linestyle = 'solid')
plt.show()

