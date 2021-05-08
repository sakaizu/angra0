import os
import fnmatch
from datetime import datetime


def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp)
    formatdate = d.strftime('%Y-%m-%d, %H:%M:%S')
    return formatdate


def main():
    currentpath = os.getcwd()
    filelist = os.scandir(currentpath)
    checkfilelist = []
    
    print(type(filelist))

    with filelist as files:
        for i in files:
            if i.is_file():
                info = i.stat()
                print(i.name, convert_date(info.st_mtime))
                checkfilelist.append(i.name)

            elif i.is_dir():
                print('Directory ---', i.name)
    #print(checkfilelist)


main()


