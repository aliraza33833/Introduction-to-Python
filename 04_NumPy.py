import numpy as np  # Import the numpy package as np

# 01_NumPy
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200]

np_baseball = np.array(baseball)  # Create a numpy array from baseball
print(type(np_baseball))

np_height_in = np.array(height_in)  # Create a numpy array from height
print(np_height_in)

np_height_m = np_height_in * 0.0254  # Convert np_height to m
print(np_height_m)

np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2  # Calculate the BMI
print(bmi)

light = np.array(bmi < 21)  # Create the light array
print(light)
print(bmi[light])  # Print out BMIs of all baseball players whose BMI is below 21

np_weight_lb = np.array(weight_lb)  # Store weight and height lists as numpy arrays
np_height_in = np.array(height_in)

print(np_weight_lb[50])  # Print out the weight at index 50
print(
    np_height_in[100:111]
)  # Print out sub-array of np_height: index 100 up to and including index 110


# 02_2D NumPy
baseball = [
    [180, 78.4],
    [215, 102.7],
    [210, 98.5],
    [188, 75.2],
]  # Create baseball, a list of lists

updated = [
    [1.29, 1.18, 1][1.02, 6.09, 1,][1.15, 5.08, 1,][1.25, 4.23, 1,][
        0.89,
        7.75,
        1,
    ][0.99, 8.11, 1]
]

np_baseball = np.array(
    [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
)  # Create a 2D numpy array from baseball
print(type(np_baseball))
print(np_baseball.shape)  # Print out the shape of np_baseball

np_baseball = np.array(baseball)  # Create a 2D numpy array from baseball
print(np_baseball.shape)  # Print out the shape of np_baseball

np_baseball = np.array(baseball)  # Create np_baseball (2 cols)
print(np_baseball[49:50, :])  # Print out the 50th row of np_baseball

np_weight_lb = np_baseball[:, 1]  # Select the entire second column of np_baseball
print(np_baseball[123:124, :])  # Print out height of 124th player

np_baseball = np.array(baseball)  # Create np_baseball (3 cols)
print(np_baseball + updated)  # Print out addition of np_baseball and updated

conversion = np.array([0.0254, 0.453592, 1])  # Create numpy array
print(np_baseball * conversion)  # Print out product of np_baseball and conversion


# 03_Numpy: Basic Statistics
np_height_in = np.array(np_baseball[:, 0])  # Create np_height from np_baseball
print(np.mean(np_height_in))  # Print out the mean of np_height
print(np.median(np_height_in))  # Print out the median of np_height

avg = np.mean(np_baseball[:, 0])  # Print mean height (first column)
print("Average: " + str(avg))

med = np.median(np_baseball[:, 0])  # Print median height. Replace 'None'
print("Median: " + str(med))

stddev = np.std(
    np_baseball[:, 0]
)  # Print out the standard deviation on height. Replace 'None'
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(
    np_baseball[:, 0], np_baseball[:, 1]
)  # Print out correlation between first and second column. Replace 'None'
print("Correlation: " + str(corr))

positions = ["GK", "M", "A", "D", "M", "D", "M", "M"]
heights = [
    191,
    184,
    185,
    180,
    181,
    187,
    170,
    179,
]
np_positions = np.array(positions)  # Convert positions and heights to numpy arrays
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == "GK"]  # Heights of the goalkeepers: gk_heights
other_heights = np_heights[
    np_positions != "GK"
]  # Heights of the other players: other_heights

print(
    "Median height of goalkeepers: " + str(np.median(gk_heights))
)  # Print out the median height of goalkeepers. Replace 'None'
print(
    "Median height of other players: " + str(np.median(other_heights))
)  # Print out the median height of other players. Replace 'None'
