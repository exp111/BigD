#%% [markdown]
# ## Occurrence of Numbers
# The Graph below shows the Occurence of the numbers in the given P.csv file

#%%
from csv import reader as csvReader
from collections import Counter
from matplotlib import pyplot as plt

with open('P.csv', 'r') as csvFile:
    reader = csvReader(csvFile, delimiter=';')
    for row in reader:
        counter = Counter()
        for v in row:
            try:
                counter[int(v)] += 1
            except ValueError:
                # Not a number
                print(v + " is not a Number")
        
        plt.title("Occurrence of Numbers")
        plt.ylabel("Count")
        plt.xlabel("Number")
        plt.bar(counter.keys(), counter.values())
        plt.show()