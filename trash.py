import os
import pathlib
#import xlwt
import datetime
import pytest
from colorama import Fore, Back, Style

class MeteorDataEntry:
    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, GeoLocation, States, Counties):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.GeoLocation = GeoLocation
        self.States = States
        self.Counties = Counties

file = None
massList = []
ageList = []
strBlank = ""
strName = "Name"
isFileReadable = True
lwrLimit = 0
uprLimit = 0
titles = 0

def welcome_message():
    print("Welcome to the meteorite filtering program. This program filters the meteors in a file you choose based on their mass or the year the meteors fell in. You can also choose to edit the file(but it won't work). \nThe developer's name is Mohannad. The release date of this program is December 2023")

def check_input_validity_fileName(fileName):
    try:
        global file
        file = open(fileName, "r")
    except:
        print(Fore.RED + "ERROR: TARGET FILE NAME \"" + fileName + "\" IS NOT VALID!\n" + Style.RESET_ALL)
        return False
    print("\nTarget file: " + fileName, end="\n\n")
    return True

def get_file_name():
    fileName = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or|\nEnter \">q\" or \">Q\" to quit: ")
    if (fileName == ">q") or (fileName == ">Q"):
        exit("\nClosing program.")
    return fileName

def check_input_validity_fileMode(fileMode):
    if fileMode == "r" or fileMode == "w" or fileMode == "x" or fileMode == "a"or fileMode == ">q" or fileMode == ">Q":# or fileMode == "b" or fileMode == "t" or fileMode == "+" or fileMode == ">q" or fileMode == ">Q":
        print("\nFile Mode: " + fileMode, end="\n\n")
        return True
    print(Fore.RED + "ERROR: MODE \"" + fileMode + "\" IS NOT VALID!\n" + Style.RESET_ALL)
    return False

def get_file_reading_mode():
    fileMode = input("What mode would you like to open the file with?\n"
                     "\"r\" - open for reading (default)\n"
                     "\"w\" - open for writing, truncating the file first " + Fore.RED + "(Warning: this mode will delete\n"
                     "        the contents of an existing file!)" + Style.RESET_ALL + "\n"
                     "\"x\" - open for exclusive creation, failing if the file already exists\n"
                     "\"a\" - open for writing, appending to the end of file if it exists\n"
                     #"\"b\" - binary mode\n"
                     #"\"t\" - text mode (default)\n"
                     #"\"+\" - open for updating (reading and writing) \n"
                     "Enter \">q\" or \">Q\" to quit\n"
                     "Mode -> ")
    if (fileMode == ">q") or (fileMode == ">Q"):
        exit("\nClosing program.")
    return fileMode

def checkFileReadability(fileMode):
    if fileMode == "w" or fileMode == "x" or fileMode == "a":
        global isFileReadable
        isFileReadable = False

def open_file():
    fileName, fileMode = None, None

    boolean = False
    while (boolean == False):
        fileName = get_file_name()
        boolean = check_input_validity_fileName(fileName)

    boolean = False
    while (boolean == False):
        fileMode = get_file_reading_mode()
        boolean = check_input_validity_fileMode(fileMode)
    checkFileReadability(fileMode)
    try:
        return open(fileName, fileMode)
    except:
        print("could not return file", end="")

def getLimits(type):
    global lwrLimit, uprLimit
    # get the input for lower limit
    lwrLimit = input("\nEnter the LOWER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
    if (lwrLimit == "Q"):
        exit("\nClosing program.")

    # get the input for lower limit
    uprLimit = input("Enter the UPPER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
    if (uprLimit == "Q"):
        exit("\nClosing program.")

def getColumn(column):
    line = file.readline()
    #print(line)               #debug
    while (line != ""):
        line = line.strip("\n").split("\t")
        #print(line[column] + " " + str(lwrLimit) + " " + str(uprLimit))           #debug
        '''print(column)                     #debug
        print(line[column])               #debug
        print(float(line[column]) >= float(lwrLimit))  # debug
        print(float(line[column]) <= float(uprLimit))  # debug
        print("")              #debug'''
        if (line[column] != "") and (float(line[column]) >= float(lwrLimit)) and (float(line[column]) <= float(uprLimit)):
            print(line)
            #meteor = MeteorDataEntry(*line)                      #old, remove
            massList.append(line)#meteor)                     #old, remove
        line = file.readline()
        '''print("while loop: " + str(line != "") + line)          #debug
    print("while loop done")                    #debug
    print(massList)'''

def getColumn1(column):
    global isFileReadable
    if isFileReadable:
        getColumn(column)
    else:
        print(Fore.RED + "not readable" + Style.RESET_ALL, end="\n\n")
        print("The program is now exiting... GOODBYE!")
        exit()

'''def makeTable(type):
    cntr = 0

    if type == "mass":
        columnName = "Mass (g)"
        tableTitle = "  Table of meteorite masses "    
    elif type == "age":
        columnName = "Age"
        tableTitle = "  Table of meteorite year "        

    strAttribute = columnName
    print(tableTitle)
    print(f"{strBlank:<4}{strName:<24}{strAttribute:<20}")
    print("=" * 48)
    for i in massList:
        cntr += 1
        print(f"{cntr:<4}{i.name:<24}{i.mass:<20}")'''

def makeTable():
    cntr = 0

    '''if type == "mass":
        columnName = "Mass (g)"
        tableTitle = "  Table of meteorite masses "    
    elif type == "age":
        columnName = "Age"
        tableTitle = "  Table of meteorite year "        

    strAttribute = columnName
    print(tableTitle)'''


    '''{strID: < 40}{strNameType: < 40}{strRecClass: < 40}{strMass: < 20}{strFall: < 20}{strYear: < 20}{strReclat: < 20}{
                                                                                                                         strReclong: < 20}{
                                                                                                                                              strGeoLocation: < 20}{
                                                                                                                                                                       strStates: < 20}{
                                                                                                                                                                                           strCounties: < 20}'''
    print(f"{strBlank:<10}", end="")
    for i in range(len(titles)):
        print(f"{titles[i]:<21}", end="")
    print("")


    print("=" * 250)


    for rowIndex in range(len(massList)):                          #for row in massList??????????
        #cntr += 1
        print(f"{rowIndex + 1:<10}", end="")
        for columnIndex in range(len(titles)):
            print(f"{massList[rowIndex][columnIndex]:<21}", end="")
        print("")
        #print(f"{cntr:<4}{i.name:<24}{i.mass:<20}")

def case1():
    getLimits("MASS (g)")

    # sort the data based on the meteors' masses in a list
    getColumn1(4)

    # print the table with the sorted data
    makeTable()#"mass")

def case2():
    '''# get the input for lower limit
    lwrLimit = input("\nEnter the LOWER limit (inclusive) for the meteor's year ('Q' to QUIT): ")
    if (lwrLimit == "Q"):
        exit("\nClosing program.")

    # get the input for lower limit
    uprLimit = input("Enter the UPPER limit (inclusive) for the meteor's year ('Q' to QUIT): ")
    if (uprLimit == "Q"):
        exit("\nClosing program.")'''

    getLimits("year")

    # sort the data based on the meteors' masses in a list
    '''    line = file.readline()
    while (line != ""):
        line = line.strip("\n").split("\t")
        if (line[6] != "") and (float(line[6]) >= float(lwrLimit)) and (float(line[6]) <= float(uprLimit)):
            meteor = MeteorDataEntry(*line)
            ageList.append(meteor)
        line = file.readline()'''
    getColumn1(6)

        # print the table with the sorted data
    '''strAttribute = "Age"
    print("  Table of meteorite year ")
    print(f"{strBlank:<4}{strName:<24}{strAttribute:<20}")
    print("=" * 48)
    for i in ageList:
        cntr += 1
        print(f"{cntr:<4}{i.name:<24}{i.year:<20}")'''
    makeTable()#"age")

def prompt_for_attribute():
    attribute = input("What attribute would you like to filter the data on?\n"
                      "1. meteor MASS (g)\n"
                      "2. the YEAR the meteor fell to earth\n"
                      "3. QUIT\n"
                      ">> ")
    if attribute == "1":
        case1()
    elif attribute == "2":
        case2()
    elif attribute == "3":
        # exit code
        exit("\nClosing program.")

    return attribute

def check_input_validity_attribute(attribute):
    if attribute == "1" or attribute == "2" or attribute == "3":
        return True
    print(Fore.RED + f"ERROR: Invalid menu choice: \"{attribute}\"" + Style.RESET_ALL, end="\n\n")
    return False

def readFirstLine():
    try:
        global titles
        titles = file.readline().strip("\n").split("\t")
    except:
        print("tttttttttttt", end="")

def find_attribute():
    boolean = False
    while (boolean == False):
        attribute = prompt_for_attribute()
        boolean = check_input_validity_attribute(attribute)

def main():
    welcome_message()

    global file
    file = open_file()
    readFirstLine()
    find_attribute()

main()


































#main



























import os
import pathlib
import pytest
from colorama import Fore, Style
from OpenFile import open_file
from FindAttribute import find_attribute
from outputOptions import outputOptions
from variables import Variable



'''errors to watch out for
main.py in file entering

giving a lwrLimit bigger than the uprLimit

'''

class MeteorDataEntry:
    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, GeoLocation, States, Counties):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.GeoLocation = GeoLocation
        self.States = States
        self.Counties = Counties

def welcome_message():
    print("Welcome to the meteorite filtering program. This program filters the meteors in a file you choose based on their "
          "mass or the year the meteors fell in. You can also choose to edit the file(but it won't work). "
          "\nThe developer's name is Mohannad. The release date of this program is December 2023")

def readFirstLine():
    try:
        global titles
        Variable.titles = Variable.file.readline().strip("\n").split("\t")
    except:
        print("tttttttttttt", end="")

def main():
    welcome_message()
    #variable_object = Variable()
    Variable.file = open_file()
    readFirstLine()
    find_attribute()
    outputOptions()

main()


















#open file


from colorama import Fore, Style
from main import MainClass
from variables import *


def exitIfPrompted(input):
    if (input == ">q") or (input == ">Q"):
        exit("\nClosing program.")


def check_input_validity_fileName(fileName):
    try:
        # running commands that run later in the code, running them now so that if they cause in error, then we know from
        # now that the file is flawed and so prompt the user to enter a different file name
        temporaryFile = open(fileName, "r")
        firstLine = temporaryFile.readline()
        firstLine.strip("\n").split("\t")[4]
        firstLine.strip("\n").split("\t")[6]
        temporaryFile.close()
    except:
        print(Fore.RED + "ERROR: TARGET FILE NAME \"" + fileName + "\" IS NOT A VALID TEXT FILE!\n" + Style.RESET_ALL)
        return False
    print("\nTarget file: " + fileName, end="\n\n")
    return True


def get_file_name():
    boolean = False
    while (boolean == False):
        fileName = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) |or|"
                         "\nEnter \">q\" or \">Q\" to quit: ")
        boolean = check_input_validity_fileName(fileName)
    return fileName


def checkFileReadability(fileMode):
    if fileMode == "w" or fileMode == "x" or fileMode == "a":
        # global isFileReadable
        Variable.isFileReadable = False


def check_input_validity_fileMode(fileMode):
    if fileMode == "r" or fileMode == "w" or fileMode == "x" or fileMode == "a" or fileMode == ">q" or fileMode == ">Q":  # or fileMode == "b" or fileMode == "t" or fileMode == "+" or fileMode == ">q" or fileMode == ">Q":
        print("\nFile Mode: " + fileMode, end="\n\n")
        return True
    print(Fore.RED + "ERROR: MODE \"" + fileMode + "\" IS NOT VALID!\n" + Style.RESET_ALL)
    return False


def get_file_reading_mode():
    boolean = False
    while (boolean == False):
        fileMode = input("What mode would you like to open the file with?\n"
                         "\"r\" - open for reading (default)\n"
                         "\"w\" - open for writing, truncating the file first " + Fore.RED + "(Warning: this mode will delete\n"
                                                                                             "        the contents of an existing file!)" + Style.RESET_ALL + "\n"
                                                                                                                                                              "\"x\" - open for exclusive creation, failing if the file already exists\n"
                                                                                                                                                              "\"a\" - open for writing, appending to the end of file if it exists\n"
                                                                                                                                                              "Enter \">q\" or \">Q\" to quit\n"
                                                                                                                                                              "Mode -> ")
        boolean = check_input_validity_fileMode(fileMode)
    checkFileReadability(fileMode)
    return fileMode


def open_file():
    mainClass = MainClass()

    mainClass.fileName = get_file_name()
    exitIfPrompted(mainClass.fileName)

    mainClass.fileMode = get_file_reading_mode()
    exitIfPrompted(mainClass.fileMode)

    try:
        return open(mainClass.fileName, mainClass.fileMode)
    except:
        print("could not return file", end="")


































#find attribute








from colorama import Fore, Style
from variables import *


def check_input_validity_limit(limit):
    if limit == "":
        print(Fore.RED + f"ERROR: Invalid range limit: \"{limit}\"" + Style.RESET_ALL, end="\n\n")
        return False

    for char in limit:
        if ord(char) < 48 or ord(char) > 57:
            print(Fore.RED + f"ERROR: Invalid range limit: \"{limit}\"" + Style.RESET_ALL, end="\n\n")
            return False
    return True

'''def getLimits(type):
    global lwrLimit, uprLimit
    # get the input for lower limit
    lwrLimit = input("\nEnter the LOWER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
    if (lwrLimit == "Q"):
        exit("\nClosing program.")
    check_input_validity_limit(lwrLimit)

    # get the input for lower limit
    uprLimit = input("Enter the UPPER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
    if (uprLimit == "Q"):
        exit("\nClosing program.")
    check_input_validity_limit(uprLimit)'''

def exitIfPrompted(limit):
    if (limit == "Q"):
        exit("\nClosing program.")

def findLimit(limit, type):
    limit = input("Enter the " + limit + " limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
    exitIfPrompted(limit)
    return limit

def assignToUpperOrLower(limitValue, limit):
    #global lwrLimit, uprLimit
    if limit == "LOWER":
        Variable.lwrLimit = limitValue
    elif limit == "UPPER":
        Variable.uprLimit = limitValue#findLimit(limit, type)

def loopingTillTheUserGivesCorrectLimit(limit, type):
    #global lwrLimit, uprLimit

    boolean = False
    while (boolean == False):
        limitValue = findLimit(limit, type)
        exitIfPrompted(limit)
        boolean = check_input_validity_limit(limitValue)
    return limitValue

#def getLimit(limit, type):
#    limitValue = loopingTillTheUserGivesCorrectLimit(limit, type)
#    assignToUpperOrLower(limitValue, limit)

def getLimits(type):
    #global lwrLimit, uprLimit
    # get the input for lower limit
    limitValue = loopingTillTheUserGivesCorrectLimit("LOWER", type)
    assignToUpperOrLower(limitValue, "LOWER")
    #getLimit("LOWER", type)

    limitValue = loopingTillTheUserGivesCorrectLimit("UPPER", type)
    assignToUpperOrLower(limitValue, "UPPER")
    '''boolean = False
    while (boolean == False):
        lwrLimit = findLimit("LOWER", type)
        boolean = check_input_validity_limit(lwrLimit)'''



    '''boolean = False
    while (boolean == False):
        lwrLimit = input("\nEnter the LOWER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
        if (lwrLimit == "Q"):
            exit("\nClosing program.")
        boolean = check_input_validity_limit(lwrLimit)'''

    # get the input for lower limit
    #Variable.uprLimit = findLimit("UPPER", type)
    '''boolean = False
    while (boolean == False):
        uprLimit = input("Enter the UPPER limit (inclusive) for the meteor's " + type + " ('Q' to QUIT): ")
        if (uprLimit == "Q"):
            exit("\nClosing program.")
        check_input_validity_limit(uprLimit)'''
    print("")

def getColumn(column):
    line = Variable.file.readline()
    while (line != ""):
        line = line.strip("\n").split("\t")
        '''print("a" + line[column])
        print("b" + Variable.lwrLimit)
        print("c" + Variable.uprLimit)'''
        if (line[column] != "") and (float(line[column]) >= float(Variable.lwrLimit)) and (float(line[column]) <= float(Variable.uprLimit)):
            Variable.massList.append(line)
        line = Variable.file.readline()

def getColumn1(column):
    #global isFileReadable
    if Variable.isFileReadable:
        getColumn(column)
    else:
        print(Fore.RED + "not readable" + Style.RESET_ALL, end="\n\n")
        print("The program is now exiting... GOODBYE!")
        exit()

def case1():
    getLimits("MASS (g)")

    # sort the data based on the meteors' masses in a list
    getColumn1(4)

def case2():
    getLimits("year")

    # sort the data based on the meteors' masses in a list
    getColumn1(6)

def prompt_for_attribute():
    attribute = input("What attribute would you like to filter the data on?\n"
                      "1. meteor MASS (g)\n"
                      "2. the YEAR the meteor fell to earth\n"
                      "3. QUIT\n"
                      ">> ")
    print("")
    if attribute == "1":
        case1()
    elif attribute == "2":
        case2()
    elif attribute == "3":
        # exit code
        exit("Closing program.")

    return attribute

def check_input_validity_attribute(attribute):
    if attribute == "1" or attribute == "2" or attribute == "3":
        return True
    print(Fore.RED + f"ERROR: Invalid menu choice: \"{attribute}\"" + Style.RESET_ALL, end="\n\n")
    return False

def find_attribute():
    boolean = False
    while (boolean == False):
        attribute = prompt_for_attribute()
        boolean = check_input_validity_attribute(attribute)

























#2.0


def getLimits(limitAttribute):
    # get the input for lower limit
    # limitValue = loopingTillTheUserGivesCorrectLimit("LOWER", type)
    # assignToUpperOrLower(limitValue, "LOWER")
    FindAttribute.limitAttribute = limitAttribute
    getLimit("LOWER")

    # limitValue = loopingTillTheUserGivesCorrectLimit("UPPER", type)
    # assignToUpperOrLower(limitValue, "UPPER")
    # get the input for lower limit
    Variable.uprLimit = askForLimit(limitAttribute)

    print("")


































#3.0









'''def askForLimit():
    limitValue = input("Enter the " + FindAttribute.limitType + " limit (inclusive) for the meteor's " + FindAttribute.limitAttribute + " ('Q' to QUIT): ")
    return limitValue'''

def assignToUpperOrLower(limitValue):
    findAttribute = FindAttribute()
    if findAttribute.limitType == "LOWER":
        Variable.lwrLimit = limitValue
    elif findAttribute.limitType == "UPPER":
        Variable.uprLimit = limitValue

'''def loopingTillTheUserGivesCorrectLimit():
    boolean = False
    while (boolean == False):
        limitValue = askForLimit()
        exitIfPrompted(limit)
        boolean = check_input_validity_limit(limitValue)
    return limitValue'''

'''def getLimit(limitType):
    FindAttribute.limitType = limitType
    limitValue = loopingTillTheUserGivesCorrectLimit()
    assignToUpperOrLower(limitValue)

def get_limit_of_type(limitType):
    findAttribute.limitType = limitType
    Variable.lwrLimit = askForLimit()

def getLimits(limitAttribute):
    #get the input for lower limit
    findAttribute = FindAttribute()
    findAttribute.limitAttribute = limitAttribute
    get_limit_of_type("LOWER")
    get_limit_of_type("UPPER")

    print("")'''





























#variables





class Variable:
    file = None
    fileName = ""
    fileMode = ""
    massList = []
    ageList = []
    strBlank = ""
    strName = "Name"
    isFileReadable = True
    lwrLimit = ""
    uprLimit = ""
    titles = []

    def __init__(self):#, file, massList, ageList, strBlank, strName, isFileReadable, lwrLimit, uprLimit, titles):
        self.file = None
        self.massList = []
        self.ageList = []
        self.strBlank = ""
        self.strName = "Name"
        self.isFileReadable = True
        self.lwrLimit = ""
        self.uprLimit = ""
        self.titles = []