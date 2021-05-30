import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import linregress
import math

def findError(xlist: list, ylist: list, slope: int):
    n = len(xlist)
    averageXValue = sum(xlist)/n
    averageYValue = sum(ylist)/n

    elementOneTop = 0
    elementOneBottom = 0
    for i in range(n):
        elementOneTop += (ylist[i] - averageYValue)**2
        elementOneBottom += (ylist[i] - averageXValue)**2
    
    elementOne = elementOneTop/elementOneBottom - slope**2
    return math.sqrt(elementOne/(n-2))
    

plot_title = "Strain vs Time of specimens"

filename2kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2kg.csv'
filename2decimal3kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2decimal3kg.csv'
filename2decimal5kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2decimal5kg.csv'

#Load Files
x_2kg,y_2kg = np.loadtxt(filename2kg, unpack=True, delimiter=",") 
x_2_3kg,y_2_3kg = np.loadtxt(filename2decimal3kg, unpack=True, delimiter=",")
x_2_5kg,y_2_5kg = np.loadtxt(filename2decimal5kg, unpack=True, delimiter=",")
plt.plot(x_2kg,y_2kg, label='2kg', marker='.')
plt.plot(x_2_3kg,y_2_3kg, label='2.3kg', marker='.')
plt.plot(x_2_5kg,y_2_5kg, label='2.5kg', marker='.')

#Linear Regression Stuff
slice_2kg_start = 6
slice_2kg_end = 18
x_2kg_sliced = x_2kg[slice_2kg_start:slice_2kg_end]
y_2kg_sliced = y_2kg[slice_2kg_start:slice_2kg_end]
#findSlope(x_2kg_sliced, y_2kg_sliced)
slope_2kg, intercept_2kg, r_value_2kg, p_value_2kg, std_err_2kg = linregress(x_2kg_sliced, y_2kg_sliced)
print("Linear Reg of 2kg: " + str(slope_2kg) + " Error: " + str(std_err_2kg))


#This part is to graph the line of best fit. Commented out since assignment doesn't require them
lobf_2kg = np.poly1d(np.polyfit(x_2kg_sliced, y_2kg_sliced, 1))
#Call this AFTER plotting the other stuff
plt.plot(x_2kg_sliced, lobf_2kg(x_2kg_sliced), '--',label="Line of best fit - 2kg sample")


slice_2_3kg_start = 4
slice_2_3kg_end = 9
x_2_3kg_sliced = x_2_3kg[slice_2_3kg_start:slice_2_3kg_end]
y_2_3kg_sliced = y_2_3kg[slice_2_3kg_start:slice_2_3kg_end]
slope_2_3kg, intercept_2_3kg, r_value_2_3kg, p_value_2_3kg, std_err_2_3kg = linregress(x_2_3kg_sliced, y_2_3kg_sliced)
print("Linear Reg of 2.3kg: " + str(slope_2_3kg) + " Error: " + str(std_err_2_3kg))
lobf_2_3kg = np.poly1d(np.polyfit(x_2_3kg_sliced, y_2_3kg_sliced, 1))
#Call this AFTER plotting the other stuff
plt.plot(x_2_3kg_sliced, lobf_2_3kg(x_2_3kg_sliced), '--',label="Line of best fit - 2.3kg sample")


slice_2_5kg_start = 3
slice_2_5kg_end = 8
x_2_5kg_sliced = x_2_5kg[slice_2_5kg_start:slice_2_5kg_end]
y_2_5kg_sliced = y_2_5kg[slice_2_5kg_start:slice_2_5kg_end]
slope_2_5kg, intercept_2_5kg, r_value_2_5kg, p_value_2_5kg, std_err_2_5kg = linregress(x_2_5kg_sliced, y_2_5kg_sliced)
print("Linear Reg of 2.5kg: " + str(slope_2_5kg) + " Error: " + str(std_err_2_5kg))
lobf_2_5kg = np.poly1d(np.polyfit(x_2_5kg_sliced, y_2_5kg_sliced, 1))
#Call this AFTER plotting the other stuff
plt.plot(x_2_5kg_sliced, lobf_2_5kg(x_2_5kg_sliced), '--',label="Line of best fit - 2.5kg sample")


plt.xlabel("Time - s")
plt.ylabel("Strain - mm/mm")

#actually plot them

plt.legend()
plt.title(plot_title)
plt.show()
#plt.savefig("Lab5-1.png")