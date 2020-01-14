from training import training, display, display_value
from estimatePrice import estimatePrice
from theta import setTheta

km = 100000
setTheta(0, 0)
print("before training : {}km = {}$".format(km, estimatePrice(km)))
slope, const = training()
print("after training : {}km = {}$".format(km, estimatePrice(km)))
# display_value(km)
display()
