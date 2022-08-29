import pprint

def createDict():
    bills = {
        "1000kr bills": 0,
        "500kr bills": 0,
        "200kr bills": 0,
        "100kr bills": 0,
        "50kr bills": 0,
        "20kr bills": 0,
        "10kr coins": 0,
        "5kr coins": 0,
        "2kr coins": 0,
        "1kr coins": 0
    }
    return bills

def calcBills(num):
    retVal = 0

    return retVal

def calChange(payment, price):
    if payment > price:
        return round(payment) - round(price)

    return 0

def main():
    bills = createDict()
    price = 372.38
    payment = 1000

    pprint.pprint(bills, sort_dicts=False)

if __name__ == "__main__":
    main()







