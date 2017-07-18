# import networkx as nx
import GraphCreator
import matplotlib.pyplot as plt
import pylab
"""
Script to calculate the average salary of every actor with age ranges of 10 years starting from 0
Returns a scatter plot of the values to spot any trends
"""


g = GraphCreator.json_to_graph("data.json")

sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in g.nodes(data=True):
    offset = -1
    if i[1]['json_class'] == 'Actor':
        if i[1]['age'] < 0:
            continue
        elif i[1]['age'] < 10:
            offset = 0
        elif i[1]['age'] < 20:
            offset = 1
        elif i[1]['age'] < 30:
            offset = 2
        elif i[1]['age'] < 40:
            offset = 3
        elif i[1]['age'] < 50:
            offset = 4
        elif i[1]['age'] < 60:
            offset = 5
        elif i[1]['age'] < 70:
            offset = 6
        elif i[1]['age'] < 80:
            offset = 7
        elif i[1]['age'] < 90:
            offset = 8
        elif i[1]['age'] < 100:
            offset = 9

    if offset > 0:
        sums[offset] += i[1]['total_gross']
        counts[offset] += 1

averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 9):
    if counts[i] is not 0:
        averages[i] = (sums[i]/counts[i])

ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.figure(figsize=(17, 6))
plt.scatter(ages, averages)
pylab.xlabel('Ages')
pylab.ylabel('Average Gross')

labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', ]
plt.ylim(-100, 60534868)
plt.xticks(ages, labels)
plt.show()
