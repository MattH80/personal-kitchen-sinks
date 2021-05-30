import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import linregress
import math

plot_title = "Total Strain at failure vs Stress graph"

#stress/strain calcs
force_2kg = 19.62
area_2kg = (0.9167/2*10**-3)**2*math.pi
stress_2kg = force_2kg/area_2kg

force_2_3kg = 22.563
area_2_3kg = (0.9167/2*10**-3)**2*math.pi
stress_2_3kg = force_2_3kg/area_2_3kg

force_2_5kg = 24.525
area_2_5kg = (0.9167/2*10**-3)**2*math.pi
stress_2_5kg = force_2_5kg/area_2_5kg

xPlot = [stress_2kg, stress_2_3kg, stress_2_5kg]
yPlot = [float(264 - 251) / 251, float(312 - 287) / 287, float(255 - 247) / 247]
plt.plot(xPlot, yPlot, marker='.', markersize=20)


plt.xlabel("Stress - Pa")
plt.ylabel("Strain - mm/mm")

#actually plot them

plt.legend()
plt.title(plot_title)
plt.show()
#plt.savefig("Lab5-3.png")