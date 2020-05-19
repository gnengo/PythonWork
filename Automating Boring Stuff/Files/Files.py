from pathlib import Path
import os
import shelve
import pprint

#Path('spam', 'bacon', 'eggs')
#myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#for filename in myFiles:
#    print(Path(r'C:\Users\Al', filename))
    
#Using the / Operator to Join Paths
#print(Path('spam') / 'bacon' / 'eggs')
#print(Path('spam') / Path('bacon/eggs'))
#print(Path('spam') / Path('bacon', 'eggs'))

#The home directory
#print(Path.home())

#Creating New Folders Using the os.makedirs() Function
#Your programs can create new folders (directories) with the os.makedirs() function.
#os.makedirs('C:\\Users\\godfrey.kihamba\\Documents\\PythonProgramming\\Automating Boring Stuff\\Files\\SampleDir')

#To make a directory from a Path object, call the mkdir() method.
#Path(r'C:\Users\godfrey.kihamba\Documents\PythonProgramming\spam').mkdir()

#Handling Absolute and Relative Paths
#The pathlib module provides methods for checking whether a given path is an absolute path and returning the absolute path of a relative path.
#Calling the is_absolute() method on a Path object will return True if it represents an absolute path or False if it represents a relative path.
#print(Path.cwd())

#print(Path.cwd().is_absolute())

#print(Path('spam/bacon/eggs').is_absolute())

#To get an absolute path from a relative path, you can put Path.cwd() / in front of the relative Path object.
#print(Path('my/relative/path'))
#print(Path.cwd() / Path('my/relative/path'))

#Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
#Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
#Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path.
#If start is not provided, the current working directory is used as the start path.

#print(os.path.abspath('.'))

#print(os.path.abspath('.\\Scripts'))

#print(os.path.isabs('.'))

#print(os.path.isabs(os.path.abspath('.')))

#print(os.path.relpath('C:\\Windows', 'C:\\'))

#print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
'''
#Getting the Parts of a File Path
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

#The parents attribute (which is different from the parent attribute) evaluates to the ancestor folders of a Path object with an integer index:
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
print(Path.cwd().parents[4])
print(Path.cwd().parents[5])

#The older os.path module also has similar functions for getting the different parts of a path written in a string value.
#os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument.
#os.path.basename(path) will return a string of everything that comes after the last slash in the path argument.

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))

#If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings
print(os.path.split(calcFilePath))

#The os.sep variable is set to the correct folder-separating slash for the computer running the program, '\\' on Windows and '/'
#on macOS and Linux, and splitting on it will return a list of the individual folders.

print(calcFilePath.split(os.sep))

#This returns all the parts of the path as strings.
#On macOS and Linux systems, the returned list of folders will begin with a blank string
print('/usr/bin'.split(os.sep))

#Finding File Sizes and Folder Contents
#Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
#Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)
print(Path.cwd())
print(os.listdir(Path.cwd()))

print(os.path.getsize('C:\\Users\\godfrey.kihamba\\Documents\\PythonProgramming\\Automating Boring Stuff\\Files\\Files.py'))

#If I want to find the total size of all the files in this directory, I can use os.path.getsize() and os.listdir() together.
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

#Modifying a List of Files Using Glob Patterns
#If you want to work on specific files, the glob() method is simpler to use than listdir(). Path objects have a glob() method for
#listing the contents of a folder according to a glob pattern.
#Glob patterns are like a simplified form of regular expressions often used in command line commands. The glob() method returns a
#generator object (which are beyond the scope of this book) that you’ll need to pass to list() to easily view

p = Path('C:/Users/godfrey.kihamba/Desktop')
#print(list(p.glob('*')))

#The asterisk (*) stands for “multiple of any characters,” so p.glob('*') returns a generator of all files in the path stored in p.

print(list(p.glob('*.txt'))

#Checking Path Validity
#Calling p.exists() returns True if the path exists or returns False if it doesn’t exist.
#Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
#Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.
winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
print(winDir.exists())
print(winDir.is_dir())
print(notExistsDir.exists())
print(calcFile.is_file())
print(calcFile.is_dir())

#You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the exists() method.
dDrive = Path('D:/')
print(dDrive.exists())

#The older os.path module can accomplish the same task with the os.path.exists(path), os.path.isfile(path), and os.path.isdir(path)
#functions, which act just like their Path function counterparts.

#The File Reading/Writing Process
p = Path('spam.txt')
p.write_text('Hello, world!')
print(p.read_text())

#Opening Files with the open() Function
helloFile = open(Path.cwd() / 'spam.txt')

#The open() function can also accept strings.
#helloFile = open('C:\\Users\\your_home_folder\\hello.txt')


#Reading the Contents of Files
#use the File object’s read() method

helloContent = helloFile.read()
print(helloContent)

#you can use the readlines() method to get a list of string values from the file, one string for each line of text.
sonnetFile = open(Path.cwd() / 'sonnet29.txt')
print(sonnetFile.readlines())

#Writing to Files
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

#Saving Variables with the shelve Module
#You can save variables in your Python programs to binary shelf files using the shelve module. This way, your program can restore
#data to variables from the hard drive. The shelve module will let you add Save and Open features to your program. For example,
#if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the
#program load them the next time it is run.

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()


shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

#Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values
#in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
'''

#Saving Variables with the pprint.pformat() Function
#Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use.
#Using pprint.pformat() will give you a string that you can write to a .py file. This file will be your very own
#module that you can import whenever you want to use the variable stored in it.
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()