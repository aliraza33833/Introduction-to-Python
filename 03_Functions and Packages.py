# 01_Functions
var1 = [1, 2, 3, 4]
var2 = True
print(type(var1))
print(len(var1))

out2 = int(var2) # Convert var2 to an integer

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second

full_sorted = sorted(full, reverse=True) # Sort full in descending order
print(full_sorted)


# 02_Methods
place = "poolhouse"
place_up = place.upper()
print(place)
print(place_up)
print(place.count("o")) # Print out the number of o's in place

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0)) # Print out the index of the element 20.0
print(areas.count(9.50)) # Print out how often 9.5 appears in areas
print(areas)

areas.append(24.5) # Use append twice to add poolhouse and garage size
areas.append(15.45)
print(areas)

areas.reverse() # Reverse the orders of the elements in areas
print(areas)


# 03_Package
import math # Import the math package
r = 0.43 # Definition of radius
C = 2 * math.pi * r # Calculate C
A = math.pi*r**2 # Calculate A
print("Circumference: " + str(C))
print("Area: " + str(A))

from math import radians # Import radians function of math package
r = 192500 # Definition of radius
phi = 12
dist = radians(12)*r # Travel distance of Moon over 12 degrees. Store in dist.
print(dist)
