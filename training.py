from estimatePrice import estimatePrice
from matplotlib import pyplot as plt
import theta as th
import pandas as pd
import numpy as np

def sign(a):
		if a < 0:
			return -1
		return 1

def numberLen(a):
	return len(str(abs(int(a))))


def display_value(mileage, path = "asset/data.csv"):
	slope, const = th.getTheta()
	try :
		data = pd.read_csv(path)
	except Exception:
		print("display_value\ncan't load :", path)
		exit()
	X = data.iloc[:, 0]
	Y = data.iloc[:, 1]
	
	plt.rcParams['figure.figsize'] = (12.0, 9.0)
	plt.xlabel(sorted(data)[1])
	plt.ylabel(sorted(data)[0])

	plt.scatter(X, Y, c = "blue")
	plt.scatter(mileage, estimatePrice(mileage, slope, const), c = "green")
	print("estimate price for {} = {}".format(mileage, estimatePrice(mileage, slope, const)))
	
	plt.show()
	plt.clf()


def display(training = False, evol_slope = 0, evol_const = 0, path = "asset/data.csv", step = 10):
	slope, const = th.getTheta()
	try :
		data = pd.read_csv(path)
	except ValueError:
		print("display\nError : const and slope need to be float")
		exit()
	except Exception:
		print("display\ncan't load :", path)
		exit()
	X = data.iloc[:, 0]
	Y = data.iloc[:, 1]

	if training == True and (evol_slope == 0 or evol_const == 0):
		print("display\nError : to show training display need to get evol_slope and evol_const in param")
		exit()

	plt.rcParams['figure.figsize'] = (12.0, 9.0)
	plt.xlabel(sorted(data)[1])
	plt.ylabel(sorted(data)[0])

	if step < 1:
		print("display\nError : step must be superior at 0")
		exit()

	if training == True:
		for i in range(len(evol_slope)):
			if i == 0:
				plt.plot([min(X), max(X)], [evol_slope[i] * min(X) + evol_const[i],
					evol_slope[i] * max(X) + evol_const[i]], color='orange')
			elif i % step == 0:
				plt.plot([min(X), max(X)], [evol_slope[i] * min(X) + evol_const[i],
					evol_slope[i] * max(X) + evol_const[i]], color='green')
	plt.scatter(X, Y, c = "blue")

	plt.plot([min(X), max(X)], [estimatePrice(min(X), slope, const), estimatePrice(max(X), slope, const)], color='red')
	plt.show()
	plt.clf()


def training(path = "asset/data.csv", info = False, learning_slope = None, learning_const = None, iteration = 0, precision = 0.05):
	""">> Use training to train your model with the data set in init\n\tArgs : info, learning_slope, learning_const, iteration, precision"""
	print("start Training")
	evol_const = []
	evol_slope = []
	last_slope = 0
	last_const = 0
	slope = 0
	const = 0
	step = 0

	if iteration < 0:
		print("Error : iteration need to be positive")
		return

	try :
		if learning_slope != None:
			learning_slope = float(learning_slope)
		if learning_const != None:
			learning_const = float(learning_const)
		precision = float(precision)
		iteration = int(iteration)
		data = pd.read_csv(path)
	except ValueError:
		print("training\nError : const, slope and precision need to be float, iteration need to be int")
		exit()
	except Exception:
		print("can't load :", path)
		exit()

	X = data.iloc[:, 0]
	Y = data.iloc[:, 1]
	size = float(len(X))

	if learning_slope == None:
		learning_slope = 1 / (2 * pow(10, (numberLen(max(X)) + numberLen(max(Y)) - 1)))
	if learning_const == None:
		learning_const = 0.5

	print("learning_slope : {} -- learning_const : {}".format(learning_slope, learning_const))

	Y_pred = slope * X + const
	tmp_s = sum(X * (Y_pred - Y)) / size
	tmp_c = sum(Y_pred - Y) / size
	while (iteration == 0 and (abs(tmp_c) > precision or abs(tmp_s) > precision)) or step < iteration:
		step += 1
		evol_slope.append(slope)
		evol_const.append(const)
		Y_pred = slope * X + const
		tmp_s = sum(X * (Y_pred - Y)) / size
		tmp_c = sum(Y_pred - Y) / size

		if sign(last_const) != sign(tmp_c):
			learning_const = learning_const / 2
		if sign(last_slope) != sign(tmp_s):
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

	th.setTheta(slope, const)
	print ("step : {} - slope = {}, const = {}\n".format(step, slope, const))
	return (evol_slope, evol_const)
