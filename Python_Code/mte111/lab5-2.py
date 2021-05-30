import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import linregress
import math

def findErrorBarDeviation(xlist: list, mean: int, numberOfDataPoints: int):
    length = len(xlist)
    runningTotal = 0
    for i in range(length):
        runningTotal += (xlist[i] - mean)**2
    return math.sqrt(runningTotal/numberOfDataPoints)


plot_title = "Strain Rate vs Stress graph of 3 specimens"

filename2kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2kg.csv'
filename2decimal3kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2decimal3kg.csv'
filename2decimal5kg = r'C:\Users\Sahil\Documents\GitHub\PythonCode\mte111\results1-2decimal5kg.csv'

#Load Files
x_2kg,y_2kg = np.loadtxt(filename2kg, unpack=True, delimiter=",") 
x_2_3kg,y_2_3kg = np.loadtxt(filename2decimal3kg, unpack=True, delimiter=",")
x_2_5kg,y_2_5kg = np.loadtxt(filename2decimal5kg, unpack=True, delimiter=",")


#2kg regression and stress/strain calcs
force_2kg = 19.62
area_2kg = (0.9167/2*10**-3)**2*math.pi
stress_2kg = math.log(force_2kg/area_2kg, math.e) #Calculate ln of stress 
#bound the parts we want for the estimation
slice_2kg_start = 6
slice_2kg_end = 18
x_2kg_sliced = x_2kg[slice_2kg_start:slice_2kg_end]
y_2kg_sliced = y_2kg[slice_2kg_start:slice_2kg_end]
#use scipy for linear regression stuff
slope_2kg, intercept_2kg, r_value_2kg, p_value_2kg, std_err_2kg = linregress(x_2kg_sliced, y_2kg_sliced)
#get the epicc strain
strain_2kg = math.log(slope_2kg, math.e)

force_2_3kg = 22.563
area_2_3kg = (0.9167/2*10**-3)**2*math.pi
stress_2_3kg = math.log(force_2_3kg/area_2_3kg, math.e)
slice_2_3kg_start = 4
slice_2_3kg_end = 9
x_2_3kg_sliced = x_2_3kg[slice_2_3kg_start:slice_2_3kg_end]
y_2_3kg_sliced = y_2_3kg[slice_2_3kg_start:slice_2_3kg_end]
slope_2_3kg, intercept_2_3kg, r_value_2_3kg, p_value_2_3kg, std_err_2_3kg = linregress(x_2_3kg_sliced, y_2_3kg_sliced)
strain_2_3kg = math.log(slope_2_3kg, math.e)

force_2_5kg = 24.525
area_2_5kg = (0.9167/2*10**-3)**2*math.pi
stress_2_5kg = math.log(force_2_5kg/area_2_5kg, math.e)
slice_2_5kg_start = 3
slice_2_5kg_end = 8
x_2_5kg_sliced = x_2_5kg[slice_2_5kg_start:slice_2_5kg_end]
y_2_5kg_sliced = y_2_5kg[slice_2_5kg_start:slice_2_5kg_end]
slope_2_5kg, intercept_2_5kg, r_value_2_5kg, p_value_2_5kg, std_err_2_5kg = linregress(x_2_5kg_sliced, y_2_5kg_sliced)
strain_2_5kg = math.log(slope_2_5kg, math.e)


#Actual plotting stuff
xPlot = [stress_2kg, stress_2_3kg, stress_2_5kg]
yPlot = [strain_2kg, strain_2_3kg, strain_2_5kg]
yerr = np.std(yPlot)/3 #divide by 3 due to 3 datapoints
#yerr = [math.log(slope_2kg + std_err_2kg, math.e) - strain_2kg, math.log(slope_2_3kg + std_err_2_3kg, math.e) - strain_2_3kg,math.log(slope_2_5kg + std_err_2_5kg, math.e) - strain_2_5kg]
#print(yerr)
print(yerr*3)
plt.errorbar(xPlot, yPlot, yerr=yerr)
plt.plot(xPlot, yPlot, marker='.', markersize=20, label="Strain Rate compared to Stress of specimens")

#more linear regression stuff
slope_plot, intercept_plot, r_value_plot, p_value_plot, std_err_plot = linregress(xPlot, yPlot)
A_value = math.pow(math.e, intercept_plot)
print (intercept_plot)
print("n value is: " + str(slope_plot) + " intercept: " + str(A_value))


plt.xlabel("ln(stress)")
plt.ylabel("ln(strain)")


plt.legend()
plt.title(plot_title)
plt.show()
#plt.savefig("Lab5-2.png")