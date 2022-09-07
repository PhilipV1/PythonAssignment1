from cmath import pi

def sphereVolume(radius):
    return round((4/3)*pi*pow(radius, 3), 1)

def main():
    while True:
        try:
            radius = float(input("Enter a radius: "))
            break
        except ValueError:
            print("This is not a number ")

    #Prints the result of calculating the volume of a sphere given a radius
    print(sphereVolume(radius))
    
if __name__ == "__main__":
    main()
