def getNumber(num, index):
    #Using floor division/integer division to access each digit separately
    return num // 10**index % 10 #Divide by 10 to the power of index and then modulus 10 to access the single digit

def calcSum(digits):
    return getNumber(digits, 0) + getNumber(digits, 1) + getNumber(digits, 2)

def digitError(num):
    if len(num) != 3:
        print("Number is not three digits! ")
        return False        
    elif not num.isdigit():
        return False

    return True

def main():
    digitCheck = False
    while not digitCheck:
        digits = input("Enter a three digit number: ")
        digitCheck = digitError(digits)

    digits = int(digits) 
    print("Sum of digits: " + str(calcSum(digits))) 

#Good practise for preventing execution of code in zero indent if imported as a module
if __name__ == "__main__":
    main()



