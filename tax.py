

def userInput():
    while True:
        try:
            income = round(float(input("Please provide monthly income: ")))
            return income
        except ValueError:
            print("Please enter a valid income")
    
def main():
    income = userInput()
    
    