from colorama import Fore, Style
from variables import Variable

class FindAttribute():
    def __init__(self):
        self.limitType = ""
        self.limitAttribute = ""

    def check_input_validity_attribute(self, attribute):
        if attribute == "1" or attribute == "2" or attribute == "3":
            return True
        print(Fore.RED + f"ERROR: Invalid menu choice: \"{attribute}\"" + Style.RESET_ALL, end="\n\n")
        return False

    def check_input_validity_limit(self, limit):
        # return false if the input is empty
        if limit == "":
            print(Fore.RED + f"ERROR: Invalid range limit: \"{limit}\"" + Style.RESET_ALL)
            return False

        # return false if the input is not a number
        for char in limit:
            if (ord(char) < 48 or ord(char) > 57) and (char != "Q"):
                print(Fore.RED + f"ERROR: Invalid range limit: \"{limit}\"" + Style.RESET_ALL)
                return False
        return True

    def sortDataBasedOnAttribute(self, column):
        line = Variable.file.readline()
        while (line != ""):
            line = line.strip("\n").split("\t")
            if (line[column] != "") and (float(line[column]) >= float(Variable.lwrLimit)) and (float(line[column]) <= float(Variable.uprLimit)):
                Variable.massList.append(line)
            line = Variable.file.readline()

    def sortDataBasedOnAttributeIfFileIsReadable(self, column):
        if Variable.isFileReadable:
            self.sortDataBasedOnAttribute(column)
        else:
            print(Fore.RED + "not readable" + Style.RESET_ALL, end="\n\n")
            print("The program is now exiting... GOODBYE!")
            exit()

    def exitIfPrompted(self, limit):
        if (limit == "Q"):
            print("\nThe program is now exiting... GOODBYE!")
            exit()

    def exitIfPromptedBasedOnLimitType(self):
        if self.limitType == "LOWER":
            self.exitIfPrompted(Variable.lwrLimit)
        elif self.limitType == "UPPER":
            self.exitIfPrompted(Variable.uprLimit)

    def assignToUpperOrLower(self, limitValue):
        if self.limitType == "LOWER":
            Variable.lwrLimit = limitValue
        elif self.limitType == "UPPER":
            Variable.uprLimit = limitValue

    def get_limit_of_type(self, limitType):
        self.limitType = limitType

        boolean = False
        while (boolean == False):
            limitValue = input("Enter the " + limitType + " limit (inclusive) for the meteor's " + self.limitAttribute + " ('Q' to QUIT): ")
            boolean = self.check_input_validity_limit(limitValue)
        self.assignToUpperOrLower(limitValue)

    def getLimits(self, limitAttribute):
        self.limitAttribute = limitAttribute

        self.get_limit_of_type("LOWER")
        self.exitIfPromptedBasedOnLimitType()

        self.get_limit_of_type("UPPER")
        self.exitIfPromptedBasedOnLimitType()

        #adding empty line after prompts
        print()

    def SortDataBasedOnMass(self):
        attributePositionInRow = 4
        self.getLimits("MASS (g)")
        self.sortDataBasedOnAttributeIfFileIsReadable(attributePositionInRow)

    def SortDataBasedOnYear(self):
        attributePositionInRow = 6
        self.getLimits("year")
        self.sortDataBasedOnAttributeIfFileIsReadable(attributePositionInRow)

    def prompt_for_attribute(self):
        attribute = input("What attribute would you like to filter the data on?\n"
                          "1. meteor MASS (g)\n"
                          "2. the YEAR the meteor fell to earth\n"
                          "3. QUIT\n"
                          ">> ")
        print("")
        if attribute == "1":
            self.SortDataBasedOnMass()
        elif attribute == "2":
            self.SortDataBasedOnYear()
        elif attribute == "3":
            exit("Closing program.")

        return attribute

    def find_attribute(self):
        boolean = False
        while (boolean == False):
            attribute = self.prompt_for_attribute()
            boolean = self.check_input_validity_attribute(attribute)