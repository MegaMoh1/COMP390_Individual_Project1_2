from colorama import Fore, Style
from variables import Variable
from datetime import datetime
import xlwt

def check_input_validity_outputOption(option):
    if (option == "1") or(option == "2") or (option == "3") or (option == "4"):
        return True
    print(Fore.RED + f"ERROR: Invalid menu choice: \"{option}\"" + Style.RESET_ALL, end="\n\n")
    return False

def writeTitlesInExcel(file):
    for columnIndex in range(len(Variable.titles)):
        file.write(0, columnIndex, Variable.titles[columnIndex])

def writeRowInExcel(file, rowIndex):
    for columnIndex in range(len(Variable.titles)):
        file.write(rowIndex, columnIndex, Variable.massList[rowIndex - 1][columnIndex])

'''def createSheet():
    Variable.fileName = datetime.now()
    Variable.fileName = Variable.fileName.strftime("%Y-%m-%d_%H_%M_%S_%f.xls")
    workbook = xlwt.Workbook()
    return workbook.add_sheet(Variable.fileName)'''

def nameFileAsTimeNow(fileType):
    timeNow = datetime.now()
    return timeNow.strftime("%Y-%m-%d_%H_%M_%S_%f" + fileType)

def writeInExcel(excel_sheet):
    writeTitlesInExcel(excel_sheet)
    for rowIndex in range(len(Variable.massList)):
        writeRowInExcel(excel_sheet, rowIndex + 1)       #adding 1 to start from the second row since the first has titles

def putOutputInExcel():
    Variable.fileName = nameFileAsTimeNow(".xls")
    workbook = xlwt.Workbook()
    excel_sheet = workbook.add_sheet("filteredMeteoriteData")
    writeInExcel(excel_sheet)
    workbook.save(Variable.fileName)

def writeTitlesInFile(file):
    for columnIndex in range(len(Variable.titles)):
        file.write(Variable.titles[columnIndex] + "\t")
    file.write("\n")

def writeRowInFile(file, rowIndex):
    for columnIndex in range(len(Variable.titles)):
        file.write(Variable.massList[rowIndex][columnIndex] + "\t")
    file.write("\n")

def writeInFile(outputFile):
    writeTitlesInFile(outputFile)
    for rowIndex in range(len(Variable.massList)):
        writeRowInFile(outputFile, rowIndex)



def putOutputInTextFile():
    Variable.fileName = nameFileAsTimeNow(".txt")
    outputFile = open(Variable.fileName, "x")
    writeInFile(outputFile)

def makeTable():
    topLeftBlankSpace = 10
    tableIndentationSpace = 30

    print(f"{Variable.strBlank:<{topLeftBlankSpace}}", end="")
    for i in range(len(Variable.titles)):
        print(f"{Variable.titles[i]:<{tableIndentationSpace}}", end="")
    print("")

    print("=" * ((tableIndentationSpace + 1) * len(Variable.massList[0])))

    for rowIndex in range(len(Variable.massList)):                          #for row in massList??????????
        print(f"{rowIndex + 1:<{topLeftBlankSpace}}", end="")
        for columnIndex in range(len(Variable.titles)):
            print(f"{Variable.massList[rowIndex][columnIndex]:<{tableIndentationSpace}}", end="")
        print("")

def giveOutput(option):
    if option == "1":
        # print the table with the sorted data
        print()
        makeTable()
    elif option == "2":
        putOutputInTextFile()
        print(Fore.GREEN + f"\nFiltered output sent to \"{Variable.fileName}\"" + Style.RESET_ALL)
    elif option == "3":
        putOutputInExcel()
        print(Fore.GREEN + f"\nFiltered output sent to \"{Variable.fileName}\"" + Style.RESET_ALL)
    else:
        print("\nThe program is now exiting... GOODBYE!")
        exit()

def looping():
    boolean = False
    while (boolean == False):
        option = input("How would you like to output the filter results?"
                       "\n1. On screen (in terminal)"
                       "\n2. To a TEXT file "  + Fore.RED + "(Warning: if you enter a name of a file that already\n"
                       "     exists in the directory, the file's content will be deleted!)" + Style.RESET_ALL + ""
                       "\n3. To an EXCEL sheet"
                       "\n4. QUIT"
                       "\n>> ")
        boolean = check_input_validity_outputOption(option)
    return option

def outputOptions():
    option = looping()
    giveOutput(option)