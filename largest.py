
def userInput(key):
    retVal = 0
    while True:
        try:
            retVal = int(input(f"Enter {key}: "))
            break
        except:
            print("Please input an integer")
    return retVal

def largest(a, b, c):
    #Determines which number is largest or if all numbers are equal
    if a == b == c:
        print(f"The numbers are all equal: {a}")
    elif a > b and a > c:
       print(f"Largest number is: {a}")
    elif b > a and b > c:
        print(f"Largest number is: {b}")
    elif a == b and b > c:
        print(f"Largest number is: {a}")
    elif b == c and c > a:
        print(f"Largest number is: {b}")
    elif a == c and a > b:
        print(f"Largest number is: {a}")
    else:
        print(f"Largest number is: {c}")

def main():
    A = userInput("A")
    B = userInput("B")
    C = userInput("C")

    largest(A, B, C)

if __name__ == "__main__":
    main()