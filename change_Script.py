from os import listdir
from os import rename

path = 'Files'

for file in listdir(path):
    file_short=file[18:]
    rename(r'%s\\%s'% (path,file),r'%s\\%s'% (path,file_short))
