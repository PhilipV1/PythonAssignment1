
def userInput(string):
    isAlpha = False
    #Loop to check if the user inputs alphabetical characters
    while not isAlpha:
        myName = str(input(f"{string} name: "))
        if myName.isalpha():
            isAlpha = True
        else:
            print("Please use alphabetic characters") 

    return myName

def createShortName(first, middle, last):
    return first[0] + ". " + middle[0] + ". " + last


def main():
    firstName = userInput("First").capitalize()
    middleName = userInput("Middle").capitalize()
    lastName = userInput("Last").capitalize()

    shortName = createShortName(firstName, middleName, lastName)

    print(f"Short name: {shortName}")

if __name__ == "__main__":
    main()