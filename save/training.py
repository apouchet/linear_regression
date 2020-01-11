import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

const = 1
slope = 1

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

def error(const, slope, x, y):
	y_pred		= const + x * slope
	y_observed	= y
	size		= len(x)

	diff = sum((y_pred - y_observed)**2)/ size / 2
	return diff

def estimatePrice(mileage):
	return (const + slope * mileage);

ta = []
tb = []

learningRate = 0.0001
# fl = FileLoader()
# data = fl.load("data2.csv")
# print(data[0])
data = pd.read_csv('../data.csv')

x = np.array(data.iloc[:, 0])
y = np.array(data.iloc[:, 1])
size = len(x)

print("min =", min(x), ", max =", max(x))
for i in np.arange(0, 5, 0.2):
	# for j in np.arange(-5, 5, 0.1):
	ta.append(error(1, i, x, y))
	# ta.append(sum(((x * i) - y)**2)/len(x))
	tb.append(i)
# plt.scatter(tb, ta, c = 'red')

print((sum((1 + 50 * x) - y)) / size)
print((sum(((1 + 50 * x) - y) * x)) / size)

# ---- 144500 = 5999
# print("144500 = 5999 --- estimation : 144500 =", estimatePrice(144500))
# for i in range(100):
accepted_diff = 0.0001
pres_const = 2 / size * sum(estimatePrice(x) - y)
pres_slope = 2 / size * sum((estimatePrice(x) - y) * x)
i = 0;
while (abs(pres_const) > 0.005 and abs(pres_slope) > 0.005):
	i += 1
	tmp_const = const - learningRate * pres_const
	tmp_slope = slope - learningRate * pres_slope
	pres_const = 2 / size * sum(estimatePrice(x) - y)
	pres_slope = 2 / size * sum((estimatePrice(x) - y) * x)
	# if (abs(const - tmp_const) <= accepted_diff) and (abs(slope - tmp_slope) <= accepted_diff):
		# break ;
	# else:
	# print("pres_const =", pres_const / 1000)
	# print("pres_slope =", pres_slope / 1000)

	const = tmp_const
	slope = tmp_slope
	# print("error =", error())
	# print("{} - a = {}, b = {}".format(i, const, slope))

# print("144500 = 5999 --- estimation : 144500 =", estimatePrice(144500))
# print("price for {}km = {}$".format(240000, estimatePrice(240000)))

Y_pred = slope * x + const

plt.scatter(x, y, c = 'blue')
plt.plot([min(x), max(x)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.show()

