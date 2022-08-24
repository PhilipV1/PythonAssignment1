while True:
    try:
        F = int(input("Enter fahrenheit: "))
        break
    except ValueError:
        print("This is not a number ")

def ftoc(f):
    return (f - 32)/(9/5)

print(ftoc(F))