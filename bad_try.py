import csv
import numpy as np


with open('iris/iris.data','r') as File:
    data = csv.reader(File) 
    data_arr = [row for row in data]

len_data_arr = len(data_arr)

sepal_l = []
sepal_w = []
petal_l = []
petal_w = []

for j in range(len_data_arr):
    sepal_l.append(float(data_arr[j][0]))
    sepal_w.append(float(data_arr[j][1]))
    petal_l.append(float(data_arr[j][2]))
    petal_w.append(float(data_arr[j][3]))

sepal_l = np.array(sepal_l)
sepal_w = np.array(sepal_w)
petal_l = np.array(petal_l)
petal_l = np.array(petal_l)

print("\nAverage sepal length: ",np.average(sepal_l))
print("\nAverage sepal width: ",np.average(sepal_w))
print("\nAverage petal length: ",np.average(petal_l))
print("\nAverage petal width: ",np.average(petal_w))

#for line in data:
