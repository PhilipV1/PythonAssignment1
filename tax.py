
def userInput():  
    while True:
        try:
            income = round(float(input("Please provide monthly income: ")))
            return income
        except ValueError:
            print("Please enter a valid income")
    
def calcTax(income):
    totalTax = 0
    firstBracket = 0
    secondBracket = 0
    thirdBracket = 0
    
    if income < 38000:
        totalTax = income * 0.3
    elif income >= 38000 and income < 50000:
        firstBracket = 38000 * 0.3
        secondBracket = (income - 38000) * 0.35
        totalTax = firstBracket + secondBracket
    else:
        firstBracket = 38000 * 0.3
        secondBracket = (50000 - 38000) * 0.35
        thirdBracket = (income - 50000) * 0.4
        totalTax = firstBracket + secondBracket + thirdBracket

    return totalTax

def main():
    income = userInput()
    tax = round(calcTax(income))

    print(f"Corresponding income tax: {tax}")

if __name__ == "__main__":
    main()


    