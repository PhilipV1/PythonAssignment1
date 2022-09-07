
def main():
    saving = 1000
    percent = 9
    years = 1
    
    #Prints the inputs in order
    print(f"Initial savings: {saving}")
    print(f"Interest rate (in percentages): {percent}")
    print(f"Number of years: {years}")
    print(f"\nThe value of your savings after {years} years is: {calcInterest(saving, percent, years)}")

def calcInterest(saving, percent, years):
    #Calulates interest
    return round(saving * pow((1 + (percent/100)), years))
        


if __name__ == "__main__":
    main()