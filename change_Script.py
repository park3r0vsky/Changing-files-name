from os import listdir
from os import rename

path = 'C:\\Users\\park3r\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\changeFileName\\Files'

for file in listdir(path):
    file_short=file[18:]
    rename(r'%s\\%s'% (path,file),r'%s\\%s'% (path,file_short))
