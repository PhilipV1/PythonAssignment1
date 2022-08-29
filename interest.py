
def main():
    saving = 880
    percent = 9
    years = 5

    def calcInterest(saving, percent, years):
        return round(saving * pow((1 + (percent/100)), years))
        

    print(calcInterest(saving, percent, years))

if __name__ == "__main__":
    main()