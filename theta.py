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
		print("getTheta:\ncan't load :", path)
		exit()
	except Exception:
		print("getTheta:\nError while reading file")
		exit()

def setTheta(slope, const, path = "asset/theta.txt"):
	try:
		fd = open(path, "w")
		fd.write("{0:f}\n{1:f}".format(slope, const))
		fd.close()
	except OSError:
		print("setTheta:\nError : can't open :", path)
		exit()
	except ValueError:
		print("setTheta:\nError : invalid value")
		exit()
	except Exception:
		print("setTheta:\nError while writing file")
		exit()
		