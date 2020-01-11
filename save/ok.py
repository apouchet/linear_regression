import pandas as pd
import collections
from matplotlib import pyplot as plt
import numpy as np


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

def read_data() :
    fl = FileLoader()
    data = fl.load("vehicle_sale_data.csv")
    print(data)
    gdp = np.array(data.GDP)
    sale = np.array(data.sale)

    array = [gdp, sale]
    # data = open("vehicle_sale_data.csv" , "r")
    # gdp_sale = collections.OrderedDict()
    # print("sale :\n", data)
    # for line in data.readlines()[1:] :
    #     record = line.split(",")
    #     gdp_sale[float(record[1])] = float(record[2].replace('\n', ""))
    # print("sale :\n", gdp_sale)
    # return gdp_sale
    return array



def step_cost_function_for(gdp, sale, constant, slope) :
    stepSize = 0.01
    # diff_sum_constant = 0 # diff of sum for constant 'c' in "c + ax" equation
    # diff_sum_slope = 0  # diff of sum for 'a' in "c + ax" equation
    # # gdp_for_years = list(gdp_sale.keys())
    # # print(gdp_for_years)

    # for year_gdp in gdp_for_years: # for each year's gdp in the sample data
    #     # get the sale for given 'c' and 'a'by giving the GDP for this sample record
    #     diff_sum_slope = diff_sum_slope + (((constant + slope * year_gdp) - gdp_sale.get(year_gdp)) * year_gdp) # slope's (h(y) - y) * x
    #     diff_sum_constant = diff_sum_constant + ((constant + slope * year_gdp) - gdp_sale.get(year_gdp)) # consant's (h(y) - y)

    # diff_sum_constant = sum(((constant + slope * gdp) - sale))
    # diff_sum_slope = sum((((constant + slope * gdp) - sale) * gdp))

    step_for_constant = (stepSize / len(gdp)) *  sum((((constant + slope * gdp) - sale) * gdp))# distance to be moved by c
    step_for_slope = (stepSize / len(gdp)) * sum(((constant + slope * gdp) - sale)) # distance to be moved by a

    new_constant = constant - step_for_constant # new c
    new_slope = slope - step_for_slope # new a

    return new_constant, new_slope



def get_weights(array):
    constant = 1
    slope = 1
    accepted_diff = 0.01
    plt.scatter(array[0], array[1], c = 'blue')
    while 1 == 1:  # continue till we reach local minimum

        new_constant, new_slope = step_cost_function_for(array[0], array[1], constant, slope)
        # if the diff is too less then lets break
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            print("done. Diff is less than", accepted_diff)
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope
            print("new values for constant and slope are {}, {}".format(new_constant, new_slope))
        # plt.show()

constant, slope = get_weights(read_data())
# constant += 10
# slope -= 1.5
print( "constant :", constant, ", slope:", slope)
plt.plot([5.48, 7.93], [(constant + slope * 5.48), (constant + slope * 7.93)], color = 'red', linestyle = 'solid')
plt.show()
