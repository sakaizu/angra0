import os

workpath = os.getcwd()
downloadpath = '/Users/seojanghyeob/Downloads'

makefilepath = downloadpath

count = 20

for file in range(count):
    f = open(os.path.join(makefilepath, "test_" + str(file) + ".txt"), 'w', encoding = 'UTF8')
    f.close()


print("end")
