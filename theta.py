def getTheta(path = "asset/theta.txt"):
	try :
		with open(path, "r") as fd:
			line = fd.readline()
			count = 1
			while line:
				if count == 1:
					slope = float(line.strip())
				elif count == 2:
					const = float(line.strip())
				else:
					print("Error : Invalid file")
					exit()
				# print("Line {}: {}".format(count, line.strip()))
				line = fd.readline()
				count += 1
		fd.close()
		return (slope, const)
	except OSError:
		print("can't load :", path)
		exit()
	except Exception:
		print("Error while reading file")
		exit()

def setTheta(slope, const, path = "asset/theta.txt"):
	try:
		fd = open(path, "w")
		fd.write("{}\n{}".format(slope, const))
		fd.close()
	except OSError:
		print("can't open :", path)
		exit()
	except Exception:
		print("Error while writing file")
		exit()

# setTheta(123.4221, 21.000031415)
# a, b = getTheta()

# print("a = {}, b = {}".format(a, b))
