# Problem_Solving

Problem Solving Programming and Scripting Module

Week 2 assignment - Calculating my Body Mass Index (BMI)
We create variables weight and height for user to input their data
we create variable BMI with formula BMI = weight/(height **2)
Run the program first time - enter weight in kilograms 
Run the program second time - enter height in metres 
Run the program again to get the BMI result 
If you want the end result as integer, formula for BMI will be BMI = (int(weight/height ** 2))

Week 3 - A program that asks a user to input a string and outputs every second letter in reverse order
x = str(input("Enter any phrase now: "))   # we create a variable for a user to input any phrase  
x_reversed = (x[::-2])                     # we use function to output every second letter in reversed order
print(x_reversed)
For example, the user enters: "I've seen it all now, a Rabbitte chasing a Fox around Croke Park!"
The output then is: "!rPeoCdur o  nsh tibRa,o l ine vI"

Week 4 - Enter positive integer and perform calculation on it - divide by two if even and multiply by three and add one if odd

a = int(input("Enter Positive Number: "))   # we create a variable for a user to input any positive number
while a != 1:                        # while 'a' not equal to one
    if (a % 2) == 0:                 # if 'a' is even then its divided by 2
        a = a/2
    elif (a % 2) != 0:               # else if 'a' is odd then it is multiplied by 3 and then 1 is added
        a = (a * 3) + 1
 
       
© 2020 GitHub, Inc.

