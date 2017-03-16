
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
import matplotlib.patches as mpatches

plt.title("Chicago Public Library Visitors by Month")
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

zoo_year_total = []
for a in range(len(lib_data)):
    zoo_year_total.append(int(lib_data[a][13]))

for pos in range(1, len(zoo_year_total)):
    key_pos = pos
    scan_pos = key_pos - 1
    key_val = zoo_year_total[key_pos]
    while zoo_year_total[scan_pos] > key_val and scan_pos >= 0:
        zoo_year_total[scan_pos + 1] = zoo_year_total[scan_pos]
        scan_pos -= 1
    zoo_year_total[scan_pos + 1] = key_val
del(zoo_year_total[:len(zoo_year_total) - 3])
print(zoo_year_total)
top_three = []
for i in range(len(lib_data)):
    for j in range(len(zoo_year_total)):
        if int(lib_data[i][13]) == zoo_year_total[j]:
            top_three.append(lib_data[i][1:13])
print(top_three)

Total_Visitors, = plt.plot(np.arange(len(total_visitors_by_month)), total_visitors_by_month) # don't forget a comma
#np.arange(len(total_visitors_by_month))
Total_Visitors.set_linewidth(3)
Total_Visitors.set_color("red")
Total_Visitors.set_marker('8') # look up under plt.plot or set_properties
Total_Visitors.set_markersize(10)
Total_Visitors_patch = mpatches.Patch(color = "red", label = "Total Visitors")

Chinatown, = plt.plot(np.arange(len(top_three[0])), top_three[0])
Chinatown.set_color("darkblue")
Chinatown.set_linewidth(2)
Chinatown.set_marker("o")
Chinatown.set_markersize(5)
Chinatown_patch = mpatches.Patch(color = "darkblue", label = "Chinatown")

Harold_Washington, = plt.plot(np.arange(len(top_three[1])), top_three[1])
Harold_Washington.set_color("violet")
Harold_Washington.set_linewidth(2)
Harold_Washington.set_marker("o")
Harold_Washington.set_markersize(5)
Harold_Washington_patch = mpatches.Patch(color = "violet", label = "Harold Washington")

Sulzer_Regional, = plt.plot(np.arange(len(top_three[2])), top_three[2])
Sulzer_Regional.set_color("purple")
Sulzer_Regional.set_linewidth(2)
Sulzer_Regional.set_marker("o")
Sulzer_Regional.set_markersize(5)
Sulzer_Regional_patch = mpatches.Patch(color = "purple", label = "Sulzer Regional")

plt.legend(handles = [Total_Visitors_patch, Chinatown_patch, Harold_Washington_patch, Sulzer_Regional_patch], shadow = True)
plt.xlabel("Months")
plt.ylabel("Number of Visits")
plt.title("Chicago Public Library Visits", color = "black")
plt.xticks(np.arange(len(total_visitors_by_month)),headers[1:], rotation = 45)

plt.grid()
plt.show()
