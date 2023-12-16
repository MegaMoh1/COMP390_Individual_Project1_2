#from OpenFile import open_file
#from FindAttribute import FindAttribute
#from outputOptions import outputOptions
import OpenFile
import outputOptions
from FindAttribute import FindAttribute
from variables import Variable

'''errors to watch out for
main.py in file entering

giving a lwrLimit bigger than the uprLimit

'''

'''
3 stages:
stage 1: check whether functionality is good
stage 2: check whether code is clean
stage 3: '''



'''
do I have to keep doing "mainClass = MainClass()" everytime?"'''


def welcome_message():
    print("Welcome to the meteorite filtering program. This program filters the meteors' data in a file you choose based on their "
          "mass or the year the meteors fell in and then, based on your choice, outputs the filter meteors' data as either a message "
          "in the console, as a text file, or as an excel file."
          "\nThe developer's name is Mohannad. The release date of this program is December 2023")

def readFirstLine():
    try:
        Variable.titles = Variable.file.readline().strip("\n").split("\t")
    except:
        print("tttttttttttt", end="")

def main():
    welcome_message()
    findAttribute = FindAttribute()

    Variable.file = OpenFile.open_file()
    readFirstLine()
    findAttribute.find_attribute()
    outputOptions.outputOptions()

main()