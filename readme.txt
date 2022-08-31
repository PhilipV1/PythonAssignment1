sumofthree.py:
The program takes input from the user and checks if it's an actual number. The getNumber returns a single digit depending on what index is passed through the parameters using integer division along with the modulus operator. The calcSum takes a number from the parameter and calls getNumber three times to get all single digits and then adds them together. After that the main function prints the result of the sum.

change.py:
This program takes a price input and a payment input. It then calculates the change using the calculateChange function. The program has 2 arrays of integers, one for coins and one for bills. The program first calculate the number of bills using the calcBills function taking the change and the array of bills as parameters. This function stores the amount of each bill in an array and then returns that array. After the bills are stores the program calculates the left over change with calcLeftOver and returns the updated change. The calculateCoins follows the exact same structure as the one for bills. Once the data is stores for the program uses two loops to print the amount of bills and amount of coins.

tax.py:
The tax program calculates the tax based on the tax bracket of the input value. The calcTax takes a value and check which taxbracket the value belongs to then calculates the tax according to that tax bracket and potential other brackets. It then adds all the different tax brackets together to get the total tax of the income and then prints the results.

quadequation.py:
The program takes three inputs from the user, A, B and C. Then the quadEquation function takes these three values and uses the quadratic formula to calculate the number of solutions. It has check for different cases such as if A == 0 and B != 0 so that it only presents one solution. If A == 0 and B == 0 or if the value under the square root is negative there are no solutions. It handles this with the singleSolution boolean and if it is false the function will calculate the two solutions using the quadratic formula and print them. 

