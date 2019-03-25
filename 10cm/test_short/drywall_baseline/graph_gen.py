from csv import reader
from pathlib import Path
from numpy import genfromtxt
import matplotlib.pyplot as plt


mypath = Path().absolute()
mypath = str(mypath)
mypath = mypath.replace("/home/mjacob/mmwave_rf_heat/","")

per_data=genfromtxt('Y_000_219.csv',delimiter=',')
data_peak = [el[1] for el in per_data]
fig = plt.figure()
plt.plot(data_peak)
# plt.ylim(ymin=0)
fig.suptitle(mypath + ' Peak Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Signal strength')
fig.savefig('data_peak.png')
# plt.show()


per_data=genfromtxt('data_range.csv', delimiter=',')
data_range = [el[1] for el in per_data]
fig = plt.figure()
plt.plot(data_range)
# plt.ylim(ymin=0)
fig.suptitle(mypath + ' Range Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Distance to the detected point')
fig.savefig('data_range.png')
# plt.show()

per_data=genfromtxt('temperatures.csv', delimiter=',')
data_range = [el for el in per_data]
fig = plt.figure()
plt.plot(data_range)
# plt.ylim(ymin=0)
fig.suptitle(mypath + ' Range Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Temperature')
fig.savefig('data_temp.png')
# plt.show()

per_data=genfromtxt('Y_000_219.csv',delimiter=',')
data_peak = [el[1] for el in per_data]
fig = plt.figure()
plt.plot(data_peak)
plt.ylim(ymin=0, ymax=7000)
plt.xlim(xmin=0)
fig.suptitle(mypath + ' Peak Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Signal strength')
fig.savefig('data_peak_scaled.png')
# plt.show()


per_data=genfromtxt('data_range.csv', delimiter=',')
data_range = [el[1] for el in per_data]
fig = plt.figure()
plt.plot(data_range)
plt.ylim(ymin=0, ymax=300)
plt.xlim(xmin=0)
fig.suptitle(mypath + ' Range Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Distance to the detected point')
fig.savefig('data_range_scaled.png')
# plt.show()

per_data=genfromtxt('temperatures.csv', delimiter=',')
data_range = [el for el in per_data]
fig = plt.figure()
plt.plot(data_range)
plt.ylim(ymin=0,ymax=500)
plt.xlim(xmin=0)
fig.suptitle(mypath + ' Range Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Temperature')
fig.savefig('data_temp_scaled.png')
# plt.show()
