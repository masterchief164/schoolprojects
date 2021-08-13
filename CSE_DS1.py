import csv
import numpy as np

rows_wine = []
with open('wine.csv') as iris:
    reader = csv.reader(iris, delimiter=',')
    for row in reader:
        rows_wine.append(list(map(float, row)))

a = np.array(rows_wine)
means_iris = a.mean(axis=0)
mini_iris = a.min(axis=0)
maxi_iris = a.max(axis=0)
means_iris = means_iris[1:]
mini_iris = mini_iris[1:]
maxi_iris = maxi_iris[1:]
print(means_iris)
