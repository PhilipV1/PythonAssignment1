
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
    if a == b == c:
        print("The intergers are all equal")
    elif a > b and a > c:
       print(f"Largest number is: {a}")
    elif b > a and b > c:
        print(f"Largest number is: {b}")
    else:
        print(f"Largest number is: {c}")

def main():
    A = userInput("A")
    B = userInput("B")
    C = userInput("C")

    largest(A, B, C)

if __name__ == "__main__":
    main()