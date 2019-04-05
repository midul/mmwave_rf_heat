from csv import reader
import sys
from pathlib import Path
from numpy import genfromtxt
import matplotlib.pyplot as plt


mypath = Path().absolute()
mypath = str(mypath)
mypath = mypath.replace("/home/mjacob/mmwave_rf_heat/","")
#
# per_data=genfromtxt('Y_0_2.csv',delimiter=',')
# # data_peak = [el[1] for el in per_data]
# # print(data_peak)
# fig = plt.figure()
# plt.plot(per_data)
# # plt.ylim(ymin=0)
# fig.suptitle(mypath + ' Peak Value Plot')
# plt.xlabel('Timesteps')
# plt.ylabel('Signal strength')
# fig.savefig('data_peak.png')
# # plt.show()
#

per_data=genfromtxt(sys.argv[1] ,delimiter=',')
fig = plt.figure()
plt.plot(per_data)
plt.ylim(ymin=0, ymax=7000)
plt.xlim(xmin=0)
fig.suptitle(mypath + ' Peak Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Signal strength')
fig.savefig('data_peak_scaled.png')
# plt.show()

per_data=genfromtxt('temperatures.csv', delimiter=',')
data_range = [el for el in per_data]
fig = plt.figure()
plt.plot(data_range)
plt.ylim(ymin=-10,ymax=500)
plt.xlim(xmin=0)
fig.suptitle(mypath + ' Temperature Value Plot')
plt.xlabel('Timesteps')
plt.ylabel('Temperature')
fig.savefig('data_temp_scaled.png')
# plt.show()

