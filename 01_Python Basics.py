# 01_Python as a Calculator
print(3 * 5) #Multiplication
print(5 + 5) #Addition
print(5 - 5) #Subtraction
print(10 / 2) #Division
print(18 % 7) #Modulo
print(4 ** 2) #Exponentiation
print(100 * 1.1 ** 7) #How much is your $100 worth after 7 years?



# 02_Variables and Types  
profitable = True

savings = 100
growth_multiplier = 1.1
result = savings * growth_multiplier ** 7
print(result)

year1 = savings * growth_multiplier #Assign product of growth_multiplier and savings to year1
print(type(year1)) #Print the type of year1

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!") #Fix the printout

desc = "compound interest"
doubledesc = desc + desc #Assign sum of desc and desc to doubledesc
print(doubledesc)          

pi_string = "3.1415926"
pi_float = float(pi_string) #Convert pi_string into float: pi_float
print(pi_float)  