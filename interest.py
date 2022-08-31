
def main():
    saving = 880
    percent = 9
    years = 5
    

    print(f"Initial savings: {saving}")
    print(f"Interest rate (in percentages): {percent}")
    print(f"Number of years: {years}")
    print(f"\nThe value of your savings after {years} years is: {calcInterest(saving, percent, years)}")

def calcInterest(saving, percent, years):
    return round(saving * pow((1 + (percent/100)), years))
        


if __name__ == "__main__":
    main()