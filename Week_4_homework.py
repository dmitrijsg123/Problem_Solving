
# Enter positive integer and perform calculation on it - divide by two if odd and multiply by three and add one if odd

a = int(input("Enter Positive Number: "))

while a != 1:                        # while 'a' not equal to one
    if (a % 2) == 0:                 # if 'a' is even
        a = a/2
        print(a)

    elif (a % 2) != 0:               # else if 'a' is odd
        a = (a * 3) + 1
        
        print(a)
       