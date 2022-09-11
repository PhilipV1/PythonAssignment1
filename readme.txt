sumofthree.py:
The program takes input from the user and checks if it's an actual number. The getNumber returns a single digit depending on what index is passed through the parameters using integer division along with the modulus operator. The calcSum takes a number from the parameter and calls getNumber three times to get all single digits and then adds them together. After that the main function prints the result of the sum.

change.py:
This program takes a price input and a payment input. It then calculates the change using the calculateChange function. The program has an array of integers that corresponds to each bill or coin type. The calcAmount function takes the change and this array to calculate the amount of each currency type and then returns the amount as an array. 

tax.py:
The tax program calculates the tax based on the tax bracket of the input value. The calcTax takes a value and check which taxbracket the value belongs to then calculates the tax according to that tax bracket and potential other brackets. It then adds all the different tax brackets together to get the total tax of the income and then prints the results.

quadequation.py:
The program takes three inputs from the user, A, B and C. Then the quadEquation function takes these three values and uses the quadratic formula to calculate the number of solutions. It has check for different cases such as if A == 0 and B != 0 so that it only presents one solution. If A == 0 and B == 0 or if the value under the square root is negative there are no solutions. It handles this with the singleSolution boolean and if it is false the function will calculate the two solutions using the quadratic formula and print them. 

