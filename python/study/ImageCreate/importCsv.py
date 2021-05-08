import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from PIL import Image

data = pd.read_csv('particles.csv')
data = data.iloc[0:1000]
data = data.iloc[:, 13:16]

datanp = np.asarray(data)

print(len(datanp))
print(datanp)


a = np.zeros((10, 100, 3))

for x in range(10):
    for y in range(100):
        a[x, y] = datanp[(x*10) + y]
 
#print(a)

dataimage = a.astype('uint8')

result = Image.fromarray(dataimage)

plt.imshow(result)
plt.show()
