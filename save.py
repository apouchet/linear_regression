import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

def sign(a):
	if a < 0:
		return -1
	return 1

def numberLen(a):
	return len(str(int(a)))

plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
# data = pd.read_csv('data.csv')
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

ratio_x = max(X)
ratio_y = max(Y)
s_x = numberLen(max(X))
s_y = numberLen(max(Y))

print("s_x : {} -- s_y : {}".format(s_x, s_y))
plt.scatter(X, Y, c = "blue")

ratio = max(X) / max(Y)

# X = X / ratio_x
# Y = Y / ratio_y / ratio

slope = 0
const = 0

l_s = 1 / (2 * pow(10, (s_x + s_y - 1)))
l_c = 0.5
print("l_s : {} -- l_c : {}".format(l_s, l_c))

# exit()
size = float(len(X))

evol_c = []
evol_s = []
lst_s = 0.1
lst_c = 0.1
Y_pred = slope * X + const
tmp_s = sum(X * (Y_pred - Y)) / size
tmp_c = sum(Y_pred - Y) / size
i = 0
# for i in range(5000):
while abs(tmp_c) > 0.05 or abs(tmp_s) > 0.05:
	i += 1
	# evol_s.append(slope)
	# evol_c.append(const)
	Y_pred = slope * X + const
	tmp_s = sum(X * (Y_pred - Y)) / size
	tmp_c = sum(Y_pred - Y) / size

	if sign(lst_c) != sign(tmp_c):
		l_c = l_c / 2
	if sign(lst_s) != sign(tmp_s):
		l_s = l_s / 2
	lst_c = tmp_c
	lst_s = tmp_s

	print("tmp_s = {} --- l_s = {}".format(tmp_s, l_s))
	print("tmp_c = {} --- l_c = {}".format(tmp_c, l_c))
	slope -= l_s * tmp_s
	const -= l_c * tmp_c
	if (slope == float('Inf') or const  == float('Inf')):
		print("Stop for inf")
		break
	print ("{} : slope = {}\nconst = {}\n".format(i + 1, slope, const))

# X = X * ratio_x
# Y = Y * ratio_y * ratio
for i in range(len(evol_s)):
	if i == 0:
		plt.plot([min(X), max(X)], [evol_s[i] * min(X) + evol_c[i], evol_s[i] * max(X) + evol_c[i]], color='orange')
	else:
		plt.plot([min(X), max(X)], [evol_s[i] * min(X) + evol_c[i], evol_s[i] * max(X) + evol_c[i]], color='green')

# const = 1000
print ("{} : slope = {}\nconst = {}\n".format(i + 1, slope, const))
plt.plot([min(X), max(X)], [slope * min(X) + const, slope * max(X) + const], color='red')
plt.show()

# tmp_s = 0.007125317458163946
# tmp_c = -0.3634002782132524
# 100 : slope = 1.4809944432235216
# const = 0.032870522205023484


# tmp_s = 4.1464100713315216e-08 --- l_s = 2.5e-11
# tmp_c = -1.8387610274974417e-11 --- l_c = 0.05
# 4239 : slope = -0.022438680766947112
# const = 8580.685056410068
