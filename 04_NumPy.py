# 01_NumPy
baseball = [180, 215, 210, 210, 188, 176, 209, 200] # Create list baseball
import numpy as np # Import the numpy package as np

np_baseball = np.array(baseball) # Create a numpy array from baseball
print(type(np_baseball)) 

np_height_in = np.array(height_in) # Create a numpy array from height
print(np_height_in)

np_height_m = np_height_in*0.0254 # Convert np_height to m
print(np_height_m)

np_height_m = np.array(height_in) * 0.0254 # Create array from height with correct units
np_weight_kg = np.array(weight_lb)* 0.453592 # Create array from weight with correct units
bmi = np_weight_kg/np_height_m**2 # Calculate the BMI
print(bmi)

np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2 # Calculate the BMI

light = np.array(bmi<21) # Create the light array
print (light)
print(bmi[light]) # Print out BMIs of all baseball players whose BMI is below 21

np_weight_lb = np.array(weight_lb) # Store weight and height lists as numpy arrays
np_height_in = np.array(height_in)

print(np_weight_lb[50]) # Print out the weight at index 50
print(np_height_in[100:111]) # Print out sub-array of np_height: index 100 up to and including index 110