
# Weekly task 6

# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
# You should create a function called sqrt that does this.


# We were asked to implement a Newton's method for finding square roots. 
# Formula of the Newton's method is: new x = 1/2 * (x + b/x) - 
# "one can start with b as a rough guess and compute New x; from New x, one can generate an even better guess, and so on.
#  Each next guess will be closer to exact value" 
# https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html



def sqrt(b,no_of_guesses):                         # where b is our positive number
    x = 1/2 * b                                    # where x is our initial rough guess of the square root. Let us choose this one as half of b
    for i in range(no_of_guesses):
        new_x = 1/2 * (x + b/x)
        x = new_x
    return new_x

b = float(input("Enter a positive number: "))
a = sqrt(b,3)                                     # we can choose any number of guesses (remember Newton - "each next guess will be closer to exact value"), let's choose 3 

print("The square root of {} is approx. {}".format(b,round(a,2)))     # we will round the final result to 2 decimal places
