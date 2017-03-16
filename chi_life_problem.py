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
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using
# this dataset, just let me know your intentions before you start and I will do my best to support you.


from operator import itemgetter
import csv
import matplotlib.pyplot as plt
import numpy as np

life_data = []
file = open("chi_life_expectancy.txt","r")

reader = csv.reader(file, delimiter = "\t")

for line in reader:
    life_data.append(line)

print(life_data)

headers = life_data[0]
life_data = life_data[1:]
print(headers)
print(life_data)
life_data.sort(key=itemgetter(8))
print(life_data)

life_expectancy = []
community_list = []

for i in range(len(headers)):
    if headers[i] == "2010 Life Expectancy":
        for a in range(len(life_data)):
            life_expectancy.append(float(life_data[a][i]))
            community_list.append(life_data[a][1])

print(community_list)

#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list)
# to place the labels on
# the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])

plt.figure(tight_layout = True, figsize = [12,5])

plt.bar(np.arange(len(life_expectancy)),life_expectancy, color = "olivedrab")
plt.xticks(np.arange(len(life_expectancy)),community_list, rotation = 90, size = 9, color = "darkgreen")

plt.xlabel("Community Name")
plt.ylabel("2010 Life Expectancy")

plt.show()