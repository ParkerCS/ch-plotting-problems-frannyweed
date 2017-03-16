#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.
# Make appropriate lists for plotting.
# Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list)
# to place the labels on
# the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org

from operator import itemgetter
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

plt.title("Chicago Life Expectancy")
plt.figure(tight_layout = True, figsize = [12,5])
file = open("chi_life_expectancy.txt","r")

reader = csv.reader(file, delimiter = "\t")
life_data = []
for line in reader:
    life_data.append(line)

print(life_data)

headers = life_data[0]
life_data = life_data[1:]

#Putting the Life Expectancies in Order
life_data.sort(key=itemgetter(8))

life_expectancy = []
life_expectancy_1990 = []
community_list = []

for i in range(len(headers)):
    if headers[i] == "2010 Life Expectancy":
        for a in range(len(life_data)):
            life_expectancy.append(float(life_data[a][i]))
            community_list.append(life_data[a][1])
    elif headers[i] == "1990 Life Expectancy":
        for b in range(len(life_data)):
            life_expectancy_1990.append(float(life_data[b][i]))

plt.bar(np.arange(len(life_expectancy)),life_expectancy, color = "darkblue")
plt.text(len(community_list)/2 - 5,life_expectancy[len(life_expectancy) - 1], "Minimum Value: " + str(life_expectancy[0]) + "\nMaximum Value: " + str(life_expectancy[len(life_expectancy) -1]), size = 9)
plt.xticks(np.arange(len(life_expectancy)),community_list, rotation = 90, size = 9, color = "darkgreen")
plt.ylim([0,life_expectancy[len(life_expectancy)-1]+10])

plt.subplot()
plt.bar(np.arange(len(life_expectancy_1990)),life_expectancy_1990, color = "olivedrab")

twenty_patch = mpatches.Patch(color = "darkblue", label = "2010 Life Expectancy")
ninety_patch = mpatches.Patch(color = "olivedrab", label = "1990 Life Expectancy")

plt.legend(handles = [twenty_patch, ninety_patch], shadow = True)
plt.xlabel("Community Name")
plt.ylabel("Life Expectancy")

plt.show()