import re
import sys


my_list = []
data_peak = []
data_range = []
with open(sys.argv[1]) as my_file:
    head = [next(my_file) for x in range(20)]


for x in head:
    my_list.append(re.sub('[\s+]', '', x))


found = 0
str1 = ""
str2 = ""

for x in my_list:
    if found == 0 and "PeakVal" in x:
        t = x.split(":")
        data_peak.append(t)
        found = 1

    if found == 1 and "Range" in x:
        t = x.split(":")
        data_range.append(t)
        found = 2

for x in data_peak:
    str1 = ','.join(x)
    str1 = str1.replace("PeakVal", sys.argv[2])
    str1 = str1 + "\n"

for x in data_range:
    str2 = ','.join(x)
    str2 = str2.replace("RangeIdx", str(sys.argv[2]))
    str2 = str2.replace("m", '')
    str2 = str2 + "\n"

with open('data_range.csv', 'a') as fd:
    fd.write(str2)


with open('data_peak.csv', 'a') as fm:
    fm.write(str1)

