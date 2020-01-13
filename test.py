from training import training, display, display_value
from estimatePrice import estimatePrice
from theta import setTheta

setTheta(0, 0)
print("before training : 100 000km = {}$".format(estimatePrice(100000)))
slope, const = training(path = "asset/vehicule.csv")
print("after training : 100 000km = {}$".format(estimatePrice(100000)))
# display_value(100000)
display(path = "asset/vehicule.csv")
