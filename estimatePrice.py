from theta import getTheta

def estimatePrice(mileage, slope = None, const = None):
	try :
		if slope != None:
			slope = float(slope)
		if const != None:
			const = float(const)
	except ValueError:
		print("estimatePrice\nError : const and slope need to be float")
		exit()

	if mileage < 0:
		print("estimatePrice\nError : mileage can't be negatif")
		exit()
	if slope == None or const == None:
		slope, const = getTheta()
	return (slope * mileage + const)