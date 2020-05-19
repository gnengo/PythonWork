#The shutil Module
#The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.

#Copying Files and Folders
#The shutil module provides functions for copying files, as well as entire folders.

#Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination.
#(Both source and destination can be strings or Path objects.) If destination is a filename, it will be used as the new name
#of the copied file. This function returns a string or Path object of the copied file.

import shutil, os
from pathlib import Path
'''
p = Path.cwd()
shutil.copy(p / 'capitalsquiz_answers1.txt', p / 'SampleDir')
shutil.copy(p / 'capitalsquiz_answers1.txt', p / 'SampleDir/capitalsquiz_answers100.txt')

#While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained
#in it. Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and
#subfolders, to the folder at the path destination.

shutil.copytree(p / 'SampleDir', p / 'SampleDir_backup')
'''
#Moving and Renaming Files and Folders
#Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will
#return a string of the absolute path of the new location.
#shutil.move('bacon.txt', 'C:\\Users\\godfrey.kihamba\\Documents\\PythonProgramming\\Automating Boring Stuff\\Files\\SampleDir')

shutil.move('bacon.txt', 'C:\\Users\\godfrey.kihamba\\Documents\\PythonProgramming\\Automating Boring Stuff\\Files\\SampleDir\\bacon20.txt')