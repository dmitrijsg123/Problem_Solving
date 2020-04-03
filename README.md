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
 
Week 5 - Write a program that outputs whether today is a weekday or a weekend
import datetime                 # we import datetime
x = datetime.datetime.now()      # we create variable using function datetime.datetime.now()
y = x.weekday()                   # we create variable y
z = str(input('Ask me a tricky question, like "Weekday or weekend?"'))     # we create variable for user to input a question

question = ("Weekday or weekend?")

while z == question:

    if y <= 3:                                                          # if today is Monday to Thursday - program answers
        print("Unfortunately today is still a weekday.")                   
        break                   
    elif y == 4:                                                        # If today is Friday - program answers
        print("Hold on, still weekday but nearly there, my friend")        
        break

    elif y == 5 or 6:                                                   # If today is Saturday or Sunday - program answers
        print("It is weekend, thanks God!")                     
        break                     
    
else:                                                                   # If incorrect input - program answers
                               

© 2020 GitHub, Inc.

