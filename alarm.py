def numInput(msg):
    #Input error handling
    while True:
        try:
            retVal = int(input(msg))
            break
        except ValueError:
            print("Please enter a valid number")
    return retVal

def main():
    currentTime = 0
    timeToAlarm = 0
    alarmTime = 0
    firstMsg = "What time is it? "
    secMsg = "How many hours to the alarm? "

    currentTime = numInput(firstMsg)
    timeToAlarm = numInput(secMsg)

    alarmTime = (currentTime + timeToAlarm) % 24
    #Formats time to xx.xx
    timeFormat = "{:.2f}".format(alarmTime)
    round(alarmTime, 2)
    print(f"The alarm will go off at: {timeFormat}")

if __name__ == "__main__":
    main()





            
    