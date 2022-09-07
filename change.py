from math import floor
#This function calculates the amount of each currency type, takes in change and the array of currency types
def calcAmount(change, currencyArray):
    #Initialize all the value of all indices to 0 with the length of currencyArray
    currencyAmount = [0 for i in range(len(currencyArray))]
    for index in range(0, len(currencyArray), 1):
        #amount stores how many bills or coins of current type
        amount = floor(change // currencyArray[index]) 
        #Checking if there is a bill of coin of current type
        if amount > 0:
            currencyAmount[index] = amount
            #Subtracting the value of the bills or coins to get the remaining change
            change -= currencyArray[index] * amount
    return currencyAmount

#Calculates the change depending on price and payment and rounds the change to nearest whole number
def calculateChange(payment, price):
    if payment > price:
        return round(payment) - round(price)

    return 0

#Takes a string as a parameter to determine if the user is going to get the Price interface or the Payment interface
#then it checks for type errors
def userInput(string):
    if string == "Price":
        while True:
            try:
                price = float(input("Price: "))
                return price
            except ValueError:
                print("Enter a float!")
    if string == "Payment":
        while True:
            try:
                payment = float(input("Payment: "))
                return payment
            except ValueError:
                print("Enter a float!")

def main():
    price = userInput("Price")
    payment = userInput("Payment")
    change = calculateChange(payment, price)
    currency = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    print(f"Price: {price}")
    print(f"Payment: {payment}")
    print(f"\nChange: {change}")

    amountOfCurrency = calcAmount(change, currency)
    #Prints the amount of bills and coins
    for i in range(0, 6, 1):
        print(f"{currency[i]}kr bills: {amountOfCurrency[i]}")
    
    for i in range(6, len(currency), 1):
        print(f"{currency[i]}kr coins: {amountOfCurrency[i]}")

if __name__ == "__main__":
    main()







