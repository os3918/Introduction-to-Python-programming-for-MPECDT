import numpy as np
import pylab as pl

#reading the file of data
infile = open("../data/xy.dat", "r")

#create empty lists
x = []
y = []

for line in infile:
    x_, y_ = [float(w) for w in line.split()]
    x.append(x_)
    y.append(y_)

infile.close()

#change type
x = np.array(x)
y = np.array(y)

pl.plot(x, y)
pl.show()
