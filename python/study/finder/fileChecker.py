import os
import shutil

workpath = os.getcwd()
print("currentpath = ", workpath)

a = input('select command \n 1:delete targetfolder \n 2:copy download files to target \n 3:move download files to target \n Answer = ')
a = int(a)

downloadfolder  = '/Users/seojanghyeob/Downloads'
targetfolder = os.path.join(workpath, 'test')


downloadfiles = os.listdir(downloadfolder)
targetfiles = os.listdir(targetfolder)

#print(downloadfiles)
#print(targetfiles)


if a == 1:
    print('delete files!')
    
    if len(targetfiles) > 0:
        for file in targetfiles:
            print("delete file ->" + os.path.join(targetfolder, file))
            os.remove(os.path.join(targetfolder, file))
    else:
        print("nothing in this folder!")

elif a == 2:
    print('copy files!')

    if len(downloadfiles) > 0:
        for file in downloadfiles:
            shutil.copy2(os.path.join(downloadfolder, file), os.path.join(targetfolder, file))
elif a == 3:
    print('move files!')
    
    if len(downloadfiles) > 0:
        for file in downloadfiles:
            shutil.move(os.path.join(downloadfolder, file), targetfolder)

else:
    print('WrongAnser!')
