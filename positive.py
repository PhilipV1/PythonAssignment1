
def userInt():
    retVal = 0
    loopCheck = True
    #Error handling to get an int input
    while loopCheck:
        try:
            retVal = int(input("Please enter an integer: "))
            loopCheck = False
        except ValueError:
            print("Please enter an integer!")
        
    return retVal

def classifyInt(num):
    if num == 0:
        print(f"{num} is neither negative or positive")
    elif num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")

def main():
    userInput = userInt()
    classifyInt(userInput)

if __name__ == "__main__":
    main()
    