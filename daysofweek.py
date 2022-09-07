
def userInput(weekArray):
    #Checks input for a valid weekday, capitalizes the first letter in the input
    continueLoop = True
    while continueLoop:
        weekDay = input("What day would you like to translate? ").capitalize()
        validDay = checkValidWeekDay(weekDay, weekArray)
        if validDay == False:
            print("Please enter a valid weekday")
        else:
            continueLoop = False

    return weekDay

def checkValidWeekDay(day, week):
    for element in week:
        if element == day:
            return True
    return False
    
def main():
    weekDayEng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #Using dictionary to map the swedish translation to an english equivalent
    weekDictionary = {
        "Monday": "Måndag",
        "Tuesdag": "Tisdag",
        "Wednesday": "Onsdag",
        "Thursday": "Torsdag",
        "Friday": "Fredag",
        "Saturday": "Lördag",
        "Sunday": "Söndag"
    }
    #Takes the weekday input and then prints the swedish equivalent
    engDay = userInput(weekDayEng)
    print(weekDictionary[engDay])

if __name__ == "__main__":
    main()




