"""
Swear Jar plot generator for the ESDLab.

by: James Cook
"""
import matplotlib.pyplot as plt
from heapq import nlargest

# Add names and values here. Format is *name*: *number of jar papers*
peopleInJar = {
                'Marc Secanell': 10,
                'Mayank Sabharwal': 3,
                'James Cook': 6,
                'Alexandre Jarauta': 4,
                'Jeremy Zhou': 2,
                }

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = []
sizes = []
explode = []
for key, val in peopleInJar.items():
    labels.append(key)
    sizes.append(val)
    explode.append(0)

# find 2 largest values and make them stand out
largest, secondLargest = nlargest(2, sizes)
explode[sizes.index(largest)] = 0.15
explode[sizes.index(secondLargest)] = 0.1

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(loc='upper right', shadow=True)

xbar = [x for x in range(len(labels))]

fig2, ax2 = plt.subplots()
ax2.bar(xbar, sizes, align='center')
plt.xticks(xbar, labels)

plt.show()
