import pandas as pd
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

csvdata = pd.read_csv("exportCsv.csv")

data = csvdata.loc[0: 1000]

PositionData = data.loc[:, ('Position.X', 'Position.Y', 'Position.Z')]
Posdatanp = np.asarray(PositionData)

#print(csvdata.loc[:, 'Position.X'])
print(Posdatanp[:,1])



fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.scatter(Posdatanp[:,0], Posdatanp[:,1], Posdatanp[:,2])
plt.show()
