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

Week 6 - Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
You should create a function called sqrt that does this.
We were asked to implement a Newton's method for finding square roots. 
Formula of the Newton's method is: new x = 1/2 * (x + b/x) - 
"one can start with b as a rough guess and compute New x; from New x, one can generate an even better guess, and so on.
Each next guess will be closer to exact value" 
https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
def sqrt(b,no_of_guesses):                     # we create a function sqrt, where b is our positive number
    x = 1/2 * b                                # x is our initial rough guess of the square root. Let us choose this one as half of b
    for i in range(no_of_guesses):
        new_x = 1/2 * (x + b/x)
        x = new_x
    return new_x
b = float(input("Enter a positive number: "))    # we create variable for user to input a positive number
a = sqrt(b,3)                                    # we can choose any number of guesses (remember Newton - "each next guess will be closer to exact value"), let's choose 3 
print("The square root of {} is approx. {}".format(b,round(a,2)))     # we will round the final result to 2 decimal places


Week 7 - Count a number of letters "w" in a text file - extract from "Alice in Wonderland" by Lewis Carroll
from collections import Counter                           # collection imported as seen on stackoverflow.com
with open("alice.txt") as f:                              # we open text file 
    L = []                                                # create a list
    letter_count = Counter()
    for x in f:
        letter_count = Counter(x)
        w_count = letter_count["w"]
        L.append(w_count)                                                   
    numbers = [L]                                                          
    max = numbers[0]                                                        
    for number in numbers:
        if number > max:
            max = number
        y = sum(max)                                                        
        print(y)   

© 2020 GitHub, Inc.

