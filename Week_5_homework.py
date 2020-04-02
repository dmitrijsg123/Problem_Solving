
# Write a program that outputs whether today is a weekday or a weekend.

import datetime

x = datetime.datetime.now()
y = x.weekday()
z = str(input('Ask me a tricky question, like "Weekday or weekend?"'))

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
    print("I don't understand your question")                               
