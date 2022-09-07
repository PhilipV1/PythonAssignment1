from math import floor
#This function calculates how many bills of each type and then returns an array with
#the amount of each type of bill
def calcBills(change, billArray):
    #Initialize all the value of all indices to 0 with the length of billArray
    billAmount = [0 for i in range(len(billArray))]
    for index in range(0, len(billArray), 1):
        #amount stores how many bills of current type
        amount = floor(change // billArray[index]) 
        #Checking if there is a bill of current type
        if amount > 0:
            billAmount[index] = amount
            #Subtracting the value of the bills to get the remaining change
            change -= billArray[index] * amount
    return billAmount

#Read info in calcBills
def calculateCoins(change, coinArray):
    coinAmount = [0 for i in range(len(coinArray))]
    for index in range(0, len(coinArray), 1):
        amount = floor(change // coinArray[index])
        if amount > 0:
            coinAmount[index] = amount
            change -= coinArray[index] * amount

    return coinAmount
#Calculates the change depending on price and payment
def calculateChange(payment, price):
    if payment > price:
        return round(payment) - round(price)

    return 0

def calcLeftOver(change, billArray, billAmount):
    #Calculates the left over change after the amount of bills have been calculated
    for i in range(0, len(billArray), 1):
        change -= billArray[i] * billAmount[i]
        
    return change

#Takes a string as a parameter to determine if the user is going to get the Price interface or the payment interface
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
    coins = [10, 5, 2, 1]
    bills = [1000, 500, 200, 100, 50, 20]

    print(f"Price: {price}")
    print(f"Payment: {payment}")
    print(f"\nChange: {change}")

    #Calculates the amount of bills then calculates the left over change to furhter calculate the amount of coins
    numOfBills = calcBills(change, bills)
    change = calcLeftOver(change, bills, numOfBills)
    numOfCoins = calculateCoins(change, coins)

    for i in range(0, len(bills), 1):
        print(f"{bills[i]}kr bills: {numOfBills[i]}")
    
    for i in range(0, len(coins), 1):
        print(f"{coins[i]}kr coins: {numOfCoins[i]}")

if __name__ == "__main__":
    main()







