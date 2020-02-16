
# Write a program that outputs whether today is a weekday or a weekend.

import datetime

x = datetime.datetime.now()

y = (input)('Ask me a tricky question, like "Weekday or weekend?"')

question = ("Weekday or weekend?")

while y == question:

    if x.weekday() <= 3:                                                    # if today is Monday to Thursday - program answers
        print("Unfortunately today is still a weekday.")                   
        break                   
    elif x.weekday() == 4:                                                  # If today is Friday - program answers
        print("Hold on, still weekday but nearly there, my friend")        
        break

    elif x.weekday() == 5 or 6:                                             # If today is Saturday or Sunday - program answers
        print("It is weekend, thanks God!")                     
        break                     
    
else:                                                                       # If incorrect input - program answers
    print("I don't understand your question")                               
