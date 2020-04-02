# Calculating my Body Mass Index (BMI)

print("Dimitri BMI")

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in metres: "))

BMI = weight/(height **2)
print ("Dimitri, your super BMI is", BMI)

# Run the program first time - enter weight in kilograms - 70
# Run the program second time - enter height in metres - 1.76
# Run the program again to get the BMI result and start thinking about joining the gym 
# If you want the end result as integer, line 8 should read 'BMI = (int(weight/height ** 2))'
