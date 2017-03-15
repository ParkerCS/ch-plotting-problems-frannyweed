
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.
#  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import csv
import matplotlib.pyplot as plt
import numpy as np

lib_data = []
file = open("chilib_visitors_2016","r")

reader = csv.reader(file, delimiter = "\t")

for line in reader:
    lib_data.append(line)

headers = lib_data[0]
lib_data = lib_data[1:]
print(lib_data)
print(headers)

total_visitors_by_month = []
for i in range(1, len(headers) - 1):
    total = 0
    for j in range(len(lib_data)):
        total += int(lib_data[j][i])
        #del (lib_data[j][i])
    total_visitors_by_month.append(total)
print()
print(lib_data)
print(total_visitors_by_month)
plt.subplot()
line, = plt.plot(np.arange(len(total_visitors_by_month)), total_visitors_by_month) # don't forget a comma
#np.arange(len(total_visitors_by_month))
line.set_linewidth(5)
line.set_color("purple")
line.set_marker('8') # look up under plt.plot or set_properties
line.set_markersize(10)

plt.xlabel("Months")
plt.ylabel("Number of Visits")
plt.title("Chicago Public Library Visits", color = "black")
plt.xticks(np.arange(len(total_visitors_by_month)),headers[1:], rotation = 45)

zoo_year_total = []
for a in range(len(lib_data)):
    zoo_year_total.append(lib_data[a][13])
print(zoo_year_total)

for pos in range(len(zoo_year_total)):
    min_pos = pos
    for scan_pos in range(min_pos, len(zoo_year_total)):
        if zoo_year_total[scan_pos] < zoo_year_total[min_pos]:
            min_pos = scan_pos
    temp = zoo_year_total[pos]
    zoo_year_total[pos] = zoo_year_total[min_pos]
    zoo_year_total[min_pos] = temp

del(zoo_year_total[:len(zoo_year_total) -3])
print(zoo_year_total)

line2, = plt.plot(np.arange(len(zoo_year_total)), zoo_year_total)

plt.grid()
plt.show()


'''
months_total = []
for month in range(12):
    total = 0
    for i in range(len(lib_data)):
        total += int(lib_data[i][month+1]
    month_totals.append(total)
print(month_totals)
'''