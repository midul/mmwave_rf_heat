import sys


f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

loop_num = int(len(lines)/40)
x = 0
y = 39
final_arr = []
for i in range(0, loop_num):
    temp = lines[x:y]
    minimum = min(temp)
    x = x + 40
    y = y + 40
    final_arr.append(minimum)

temp = str(sys.argv[1])
temp = temp.replace(".csv", "")

with open(temp + "_mins.csv", 'a') as fd:
    for x in final_arr:
        fd.write(x)
fd.close()
