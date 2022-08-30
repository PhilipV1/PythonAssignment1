


from operator import truediv


def userInput(weekArray):
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
    
#def translateDay(day, weekEng, weekSwe):

    
    

def main():
    weekDayEng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekDictionary = {
        "Monday": "Måndag",
        "Tuesdag": "Tisdag",
        "Wednesday": "Onsdag",
        "Thursday": "Torsdag",
        "Friday": "Fredag",
        "Saturday": "Lördag",
        "Sunday": "Söndag"
    }

    engDay = userInput(weekDayEng)
    print(weekDictionary[engDay])

if __name__ == "__main__":
    main()




