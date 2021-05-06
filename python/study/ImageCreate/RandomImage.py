from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as img

path = "python/study/ImageCreate/ImageData/"
filename = "test"

starttime = time.time()

np.random.randint(100, 400)
width = 32
height = 32

inputpixel = np.zeros((width, height, 3))

for x in range(len(inputpixel)):
    for y in range(len(inputpixel[0])):
        inputpixel[x, y] = np.random.choice(100, size=(3))

print(inputpixel)



dataimage = np.random.randint(256, size= [width, height, 3]).astype('uint8')

result = Image.fromarray(dataimage)

result.save(path + filename + ".png")
# result.close()
endtime = time.time()
print("worktime = ", round((endtime - starttime),3))

plt.imshow(result)
plt.show()