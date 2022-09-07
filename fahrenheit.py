
def ftoc(f):
    return (f - 32)/(9/5)
def main():
    #Check for input error
    while True:
        try:
            F = int(input("Enter fahrenheit: "))
            break
        except ValueError:
            print("This is not a number ")


    print(ftoc(F))

if __name__ == "__main__":
    main()