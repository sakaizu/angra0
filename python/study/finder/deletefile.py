import os

currentPath = os.getcwd()

print(currentPath)


target = os.path.join(currentPath, 'test')

targetfiles = os.listdir(target)


for file in targetfiles:
    print(os.path.join(target, file))
    os.remove('./test/' + str(file))


