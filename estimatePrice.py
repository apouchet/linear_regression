import pandas as pd
from matplotlib import pyplot as plt

theta_a = 0
theta_b = 0
data = 0
init = 0


class FileLoader():
	def load(self, path):
		try :
			panda_data = pd.read_csv(path)
		except Exception:
			print("can't load :", path)
			exit()
		print("Loading dataset of dimensions {} x {})".format(panda_data.shape[0], panda_data.shape[1]))
		return panda_data

	def display(self, panda_data, size):
		print(panda_data[:size])



def estimatePrice(mileage):
	return (theta_a + theta_b * mileage);

def estimaPriceTraining(mileage, tmp_a, tmp_b):
	return (tmp_a + tmp_b * mileage);

def training():
	global theta_a
	global theta_b
	global data
	global init

	learningRate = 0.02
	km = 61789
	if init == 0:
		init = 1
		fl = FileLoader()
		data = fl.load("data.csv")
		plt.scatter(data.km, data.price, c = 'blue')

	tmp_a = theta_a;
	tmp_b = theta_b;
	tmp_a = (sum(estimatePrice(data.km[i]) - data.price[i] for i in range(data.shape[0]))) / data.shape[0] * learningRate
	tmp_b = (sum(estimatePrice(data.km[i] - data.price[i]) * data.km[i] for i in range(data.shape[0]))) / data.shape[0] * learningRate
	# for j in range(10):
	theta_a = tmp_a - tmp_b
	theta_b = tmp_b - (sum(theta_b * data.km[i] + theta_b * (data.km[i] - data.price[i]) + tmp_a for i in range(data.shape[0]))) / data.shape[0]
		# print("{} | price for {}km : {}\n".format(j, km, estimatePrice(km)))
	print(theta_a)
	print(theta_b)
	print("\n")
	plt.plot([22899, 240000], [estimatePrice(22899), estimatePrice(240000)], color = 'red', linestyle = 'solid')
	plt.show()
	# theta_a = tmp_a
	# theta_b = tmp_b

# sum(bx + a - y) deriv = b
# sum((b(x - y) + a) * x)/m deriv = sum(b*x+b*(x-y)+a)/m
# print("theta_a =", theta_a, ", theta_b =", theta_b)
