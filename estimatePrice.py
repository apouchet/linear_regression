from theta import getTheta

def estimatePrice(mileage, slope = '', const = ''):
	if slope == '' or const == '':
		slope, const = getTheta()
	return (slope * mileage + const)