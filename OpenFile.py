from colorama import Fore, Style
from variables import Variable

def exitIfPrompted(input):
    if (input == ">q") or (input == ">Q"):
        print("\nThe program is now exiting... GOODBYE!")
        exit()

def openTestFile(fileName):
    # running commands that run later in the code, running them now so that if they cause in error, then we know from
    # now that the file is flawed and so prompt the user to enter a different file name
    temporaryFile = open(fileName, "r")
    firstLine = temporaryFile.readline()
    firstLine.strip("\n").split("\t")[4]
    firstLine.strip("\n").split("\t")[6]
    temporaryFile.close()

def check_input_validity_fileName(fileName):
    try:
        if fileName != ">q" and fileName != ">Q":
            openTestFile(fileName)
    except:
        print(Fore.RED + "ERROR: TARGET FILE NAME \"" + fileName + "\" IS NOT A VALID TEXT FILE!\n" + Style.RESET_ALL)
        return False
    #print("\nTarget file: " + fileName, end="\n\n")
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
        Variable.isFileReadable = False

def check_input_validity_fileMode(fileMode):
    if fileMode == "r" or fileMode == "w" or fileMode == "x" or fileMode == "a" or fileMode == ">q" or fileMode == ">Q":# or fileMode == "b" or fileMode == "t" or fileMode == "+" or fileMode == ">q" or fileMode == ">Q":
    #print("\nFile Mode: " + fileMode, end="\n\n")
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
    return fileMode

def open_file():
    Variable.fileName = get_file_name()
    exitIfPrompted(Variable.fileName)
    print("\nTarget file: " + Variable.fileName, end="\n\n")

    Variable.fileMode = get_file_reading_mode()
    exitIfPrompted(Variable.fileMode)
    print("\nFile Mode: " + Variable.fileMode, end="\n\n")
    checkFileReadability(Variable.fileMode)

    ##########################################################################I think we should delete this place
    try:
        return open(Variable.fileName, Variable.fileMode)
    except:
        print("could not return file", end="")
        ######################################################is it possible that a file is readable but not writable to?