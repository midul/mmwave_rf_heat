import re
import sys
import os.path
from pathlib import Path

my_list = []
data_peak = []
data_range = []


f = open('temp.txt', 'r')
lines = f.readlines()
f.close()

for x in lines:
    x = x.replace(":", "_")
    my_list.append(re.sub('[\s+]', '', x))


for i, line in enumerate(my_list):
    if "PacketID_" in line and i+1 < len(my_list):
        print(my_list[i])
        # break
    if "ObjId_" in line and (i + 3) < len(my_list) and (i + 5) < len(my_list):
        print(my_list[i])
        print(my_list[i + 3])
        print(my_list[i + 5])
        num = my_list[i + 5]
        num = num. replace("Y_", "")
        num = float(num)
        num = round(num, 1)
        if "Y_" in my_list[i + 5]:
            x = my_list[i + 5].replace(".", "_")

        print(num)
        num = num - 0.1
        num = round(num, 1)
        if num >= 0.0:
            num1 = "Y_" + str(num).replace(".", "_") + ".csv"
            if os.path.isfile(num1):
                print("File exists")
                with open(num1, 'a') as fd:
                    x1 = my_list[i + 3].replace("PeakVal_", "")
                    x1 = x1 + "\n"
                    fd.write(x1)
                fd.close()
            else:
                num = num + 0.2
                num = round(num, 1)
                num1 = "Y_" + str(num).replace(".", "_") + ".csv"
                if os.path.isfile(num1):
                    print("File exists")
                    with open(num1, 'a') as fd:
                        x1 = my_list[i + 3].replace("PeakVal_", "")
                        x1 = x1 + "\n"
                        fd.write(x1)
                    fd.close()
                else:
                    num = num - 0.1
                    num = round(num, 1)
                    num1 = "Y_" + str(num).replace(".","_") + ".csv"
                    if os.path.isfile(num1):
                        print("File exists")
                        with open(num1, 'a') as fd:
                            x1 = my_list[i + 3].replace("PeakVal_", "")
                            x1 = x1 + "\n"
                            fd.write(x1)
                        fd.close()
                    else:
                        print("File does not exist - creating a new file")
                        num1 = "Y_" + str(num).replace(".", "_") + ".csv"
                        with open(num1, 'a') as fd:
                            x1 = my_list[i + 3].replace("PeakVal_", "")
                            x1 = x1 + "\n"
                            fd.write(x1)
                        fd.close()

