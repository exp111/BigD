#%%
from csv import reader
from collections import defaultdict
from matplotlib import pyplot as plt

with open('P.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')
    for row in reader:
        counter = defaultdict(int)
        for i in row:
            try:
                counter[int(i)] += 1
            except ValueError:
                # Not a number
                print(i + " is not a Number")
        
        plt.title("Occurrence of Numbers")
        plt.ylabel("Count")
        plt.xlabel("Number")
        plt.bar(counter.keys(), counter.values())
        plt.show()