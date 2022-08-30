from math import floor

import pprint

def createDict(intArray):
    #using the intArray from calcBills to assign value to matching key
    bills = {
        "1000kr bills": intArray[0],
        "500kr bills": intArray[1],
        "200kr bills": intArray[2],
        "100kr bills": intArray[3],
        "50kr bills": intArray[4],
        "20kr bills": intArray[5],
        "10 coins": intArray[6],
        "5kr coins": intArray[7],
        "2kr coins": intArray[8],
        "1kr coins": intArray[9]
    }
    return bills

def calcBills(change):
    dividerArray = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    billArray = [0 for i in range(10)]#Initialize all the value of all indices to 0
    for index in range(0, len(dividerArray), 1):
        billAmount = floor(change // dividerArray[index]) #billAmount stores how many bills of current type
        if billAmount > 0:#Checking if there is a bill of current type
            billArray[index] = billAmount
            change -= dividerArray[index] * billAmount#Subtracting the value of the bills to get the remaining change

    return billArray

def calChange(payment, price):
    if payment > price:
        return round(payment) - round(price)

    return 0

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
    return 0

def main():
    price = userInput("Price")
    payment = userInput("Payment")
    change = calChange(payment, price)

    print(f"Price: {price}")
    print(f"Payment: {payment}")

    print(f"\nChange: {change}")
    billDictionary = createDict(calcBills(change)) 
    pprint.pprint(billDictionary, sort_dicts=False)


if __name__ == "__main__":
    main()







