import math

def quadEquation(a, b, c):
    first = 0
    second = 0
    singleSolution = False
    if a == 0 and b != 0:
        print(f"There is one solution, namely {-c/b}")
        singleSolution = True
    elif a == 0 and b == 0:
        print("There are no solutions")
        singleSolution = True

    elif (b**2 - 4*a*c) < 0 and singleSolution != True:
        print("There are no solutions")

    elif (b**2 - 4*a*c) == 0 and singleSolution != True:
        print(f"There is one solution, namely: {-b/(2*a)}")

    elif singleSolution != True:
        first = float(((-b + math.sqrt(b**2 - 4*a*c))/(2*a)))
        second = float(((-b - math.sqrt(b**2 - 4*a*c))/(2*a)))
        print(f"There are two solutions, namely {first} and {second}")

    else:
        print("There are no solutions")

def checkSingleSolution(a, b, c):
    if a == 0:
        return -c/b
    elif a == 0 and b == 0:
        return c
    else:
        return 0
    
def userInput(string):
    while True:
        if string == "A":
            try:
                a = float(input("A: "))
                return a
            except ValueError:
                print("Please input a valid float number")
        if string == "B":
            try:
                b = float(input("B: "))
                return b
            except ValueError:
                print("Please input a valid float number")
        if string == "C":
            try:
                c = float(input("C: "))
                return c
            except ValueError:
                print("Please input a valid float number")

def main():
    A = userInput("A")
    B = userInput("B")
    C = userInput("C")

    quadEquation(A, B, C)

if __name__ == "__main__":
    main()

