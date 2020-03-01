
#Count a number of letters "w" in a text file - extract from "Alice in Wonderland" by Lewis Carroll

from collections import Counter                                             # collection imported as seen on stackoverflow.com
with open("alice.txt") as f:
    L = []
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
            







