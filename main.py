import numpy as np

data = np.loadtxt("iris/iris.data", usecols=(0,1,2,3), delimiter=',' )
averages = np.round(np.mean(data, axis=0),4)

print("\nAverage sepal length: ",averages[0])
print("\nAverage sepal width: ",averages[1])
print("\nAverage petal length: ",averages[2])
print("\nAverage petal width: ",averages[3])