import random


def main():
    number = random.randint(-10, 10)
    #Check if number is odd or even with modulus and if the number is positive, negative or zero
    if number % 2 == 0 and number > 0:
        print(f"{number} is even and positive")
    elif number % 2 != 0 and number > 0:
        print(f"{number} is odd and positive")
    elif number % 2 == 0 and number < 0:
        print(f"{number} is even and negative")
    elif number % 2 != 0 and number < 0:
        print(f"{number} is odd and negative")
    else:
        print(f"{number} is zero")

if __name__ == "__main__":
    main()