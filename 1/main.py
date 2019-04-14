#%% [markdown]
# ## b)
# Schreiben Sie ein Programm, dass einen Zahlzähler als Map-Reduce mittels der
# entsprechenden Python-Funktionen implementiert. Dazu liest das Programm eine
# lokale Textdatei P.csv ein und gibt die Häufigkeit der einzelnen Zahlen tabellarisch
# aus. Nutzen Sie dazu die entsprechenden Python Funktionen! Stellen Sie
# dabei sicher, dass nur Zahlen erfasst werden - die Datei könnte Fehler beinhalten.

#%%
from csv import reader as csvReader
from collections import Counter
from matplotlib import pyplot as plt

def filterer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def mapper(n):
    return dict([[int(n), 1]])

def reducer(i, j):
    for k in j: i[k] = i.get(k, 0) + j.get(k, 0) # .get so we default to 0 if not existent
    return i

with open('P.csv', 'r') as csvFile:
    reader = csvReader(csvFile, delimiter=';')
    for row in reader:
        result = reduce(reducer, map(mapper, filter(filterer, row)))
        for k,v in sorted(result.items()):
            print("{0} : {1}".format(k, v))

#%% [markdown]
# ## c)
# Erstellen Sie ein Histogramm der Zahlenhäufigkeiten so, dass auf der x-Achse die Zahlen der Größe nach angeordnet sind!

#%%
from csv import reader as csvReader
from collections import Counter
from matplotlib import pyplot as plt

def filterer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def mapper(n):
    return int(n)

with open('P.csv', 'r') as csvFile:
    reader = csvReader(csvFile, delimiter=';')
    for row in reader:
        result = map(mapper, filter(filterer, row))
        
        plt.title("Occurrence of Numbers")
        plt.ylabel("Count")
        plt.xlabel("Number")
        plt.hist(result)
        plt.show()