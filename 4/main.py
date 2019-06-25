#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm
#5. class: 
#-- Iris Setosa
#-- Iris Versicolour
#-- Iris Virginica

#%% [markdown]
# ## b)
# Laden sie den Iris-Datensatz in einen Dataframe (Datei:datasets.zip/datasets/iris/data.all) 
# und drucken Sie grundlegende Statistiken zu den Daten (wie geht das einfach mit einem Dataframe?)!
import pandas

columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
df = pandas.read_csv(
    "4/data.all",
    sep = "\s+",
    header = 0,
    names = columns)
print(df) # Print whole dataframe
df.describe() # Print Statistics (like min, max, mean etc.)

#%% [markdown]
# ## c)
# Visualisieren Sie den Datensatz
# Als Scattermatrix (mittels des python Paketes matplotlib)
# Als Boxplots für die einzelnen Spalte des Datensatzes
from matplotlib import pyplot as plt
import pandas

def colorByClass(c): # Assign to every Flower Species a specific color
    if c == "Iris-setosa":
        return "r"
    elif c == "Iris-versicolor":
        return "g"
    elif c == "Iris-virginica":
        return "b"
    return "c" # default to cyan; shouldn't appear here

columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
df = pandas.read_csv(
    "4/data.all",
    sep = "\s+",
    header = 0,
    names = columns)
colors = map(colorByClass, df["Class"])
plt.scatter(df["Sepal Length"], df["Sepal Width"], c=colors)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

plt.scatter(df["Petal Length"], df["Petal Width"], c=colors)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

df.plot(kind="box", subplots = True) # for every column a new plot