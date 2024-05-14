""""""
"""
Oh Soldier Prettify My Folder

path is given as input
dictionary file that do not need to be change as input
file format as input

[1] do not mess with the folders inside the folder
[2] you can mess with the files inside the folder and if they starts with small letters then make their first letter capital and for the given file format change their names staring from 1 to required last number

def soldier("C://", "67 dummy.txt", "jpg")

for jpg format file change all files as
    1.jpg, 2.jpg, 3.jpg, ... 100.jpg

"""

import os


def soldier(path, file, fileFormat):
    os.chdir(path)
    var_i = 1
    files = os.listdir(path)

    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == fileFormat:
            os.rename(file, f"{var_i}{fileFormat}")
            var_i += 1

soldier(r"Your-Folder-Path", r"Your-File-path", "Your-File-Foramt")
