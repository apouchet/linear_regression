import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

class ClassName(object):
	
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

class linearRegression():
	"""Class linear regression : call training to train a model"""
	def __init__(self, path = 'data.csv'):
		self.__data = pd.read_csv(path)
		self.setTheta()

	def setTheta(self, const = 0, slope = 0):
		self.__const = const
		self.__slope = slope		

	def __sign(self, a):
		if a < 0:
			return -1
		return 1

	def __numberLen(self, a):
		return len(str(abs(int(a))))

	def estimatePrice(self, mileage):
		return (self.__slope * mileage + self.__const)

	def display_value(self, mileage):
		X = self.__data.iloc[:, 0]
		Y = self.__data.iloc[:, 1]
		
		plt.rcParams['figure.figsize'] = (12.0, 9.0)
		plt.xlabel(sorted(self.__data)[0])
		plt.ylabel(sorted(self.__data)[1])

		plt.scatter(X, Y, c = "blue")
		plt.scatter(mileage, self.estimatePrice(mileage), c = "green")
		print("estimate price for {} = {}".format(mileage, self.estimatePrice(mileage)))
		
		plt.show()
		plt.clf()


	def display(self, training = False, step = 1):
		X = self.__data.iloc[:, 0]
		Y = self.__data.iloc[:, 1]
		
		plt.rcParams['figure.figsize'] = (12.0, 9.0)
		plt.xlabel(sorted(self.__data)[0])
		plt.ylabel(sorted(self.__data)[1])

		if step < 1:
			print("Error : step must be superior at 0")
			return

		if training == True:
			for i in range(len(self.__evol_slope)):
				if i == 0:
					plt.plot([min(X), max(X)], [self.__evol_slope[i] * min(X) + self.__evol_const[i],
						self.__evol_slope[i] * max(X) + self.__evol_const[i]], color='orange')
				elif i % step == 0:
					plt.plot([min(X), max(X)], [self.__evol_slope[i] * min(X) + self.__evol_const[i],
						self.__evol_slope[i] * max(X) + self.__evol_const[i]], color='green')
		plt.scatter(X, Y, c = "blue")

		plt.plot([min(X), max(X)], [self.estimatePrice(min(X)), self.estimatePrice(max(X))], color='red')
		plt.show()
		plt.clf()

	def data_info(self):
		return self.__data


	def training(self, info = False, learning_slope = 0, learning_const = 0, iteration = 0, precision = 0.05):
		""">> Use training to train your model with the data set in init\n\tArgs : info, learning_slope, learning_const, iteration, precision"""
		print("start Training")
		self.setTheta()
		self.__evol_const = []
		self.__evol_slope = []
		last_slope = 0
		last_const = 0
		slope = 0
		const = 0
		step = 0

		if iteration < 0:
			print("Error : iteration need to be positive")
			return

		X = self.__data.iloc[:, 0]
		Y = self.__data.iloc[:, 1]
		size = float(len(X))

		if learning_slope == 0:
			learning_slope = 1 / (2 * pow(10, (self.__numberLen(max(X)) + self.__numberLen(max(Y)) - 1)))
		if learning_const == 0:
			learning_const = 0.5

		print("learning_slope : {} -- learning_const : {}".format(learning_slope, learning_const))

		Y_pred = slope * X + const
		tmp_s = sum(X * (Y_pred - Y)) / size
		tmp_c = sum(Y_pred - Y) / size
		while (iteration == 0 and (abs(tmp_c) > precision or abs(tmp_s) > precision)) or step < iteration:
			step += 1
			self.__evol_slope.append(slope)
			self.__evol_const.append(const)
			Y_pred = slope * X + const
			tmp_s = sum(X * (Y_pred - Y)) / size
			tmp_c = sum(Y_pred - Y) / size

			if self.__sign(last_const) != self.__sign(tmp_c):
				learning_const = learning_const / 2
			if self.__sign(last_slope) != self.__sign(tmp_s):
				learning_slope = learning_slope / 2
			last_const = tmp_c
			last_slope = tmp_s

			slope -= learning_slope * tmp_s
			const -= learning_const * tmp_c
			if (slope == float('Inf') or const  == float('Inf')):
				print("Error : inf value, iteration : {}".format(step))
				return
			if info == True:
				print ("{} : slope = {}\nconst = {}\n".format(step, slope, const))
				print("tmp_s = {} --- learning_slope = {}".format(tmp_s, learning_slope))
				print("tmp_c = {} --- learning_const = {}".format(tmp_c, learning_const))


		
		self.__const = const
		self.__slope = slope
		print ("step : {} - slope = {}, const = {}\n".format(step, slope, const))

km = 200000		
lr = linearRegression()
# lr.data_info()
print(lr.training.__doc__)
# print("data :\n", lr.data_info())
# print("estimate price for {} = {}".format(km, lr.estimatePrice(km)))
# lr.training(iteration = 10)
# print("estimate price for {} = {}".format(km, lr.estimatePrice(km)))
# lr.training(iteration = 100)
# print("estimate price for {} = {}".format(km, lr.estimatePrice(km)))
# lr.training()
# lr.training(precision = 0.005)
# lr.display()
# lr.display(True)
# lr.display_value(km)

# tmp_s = 0.007125317458163946
# tmp_c = -0.3634002782132524
# 100 : slope = 1.4809944432235216
# const = 0.032870522205023484


# tmp_s = 4.1464100713315216e-08 --- l_s = 2.5e-11
# tmp_c = -1.8387610274974417e-11 --- learning_const = 0.05
# 4239 : slope = -0.022438680766947112
# const = 8580.685056410068
