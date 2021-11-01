# 01_Python lists
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath] # [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas)

areas = ["hallway",hall,"kitchen", kit, "living room", liv,"bedroom" ,bed, "bathroom", bath] # Create list with different types
print(areas)

house = [["hallway", hall],
        ["kitchen", kit],
        ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]] # List of lists or Sublists
print(house)
print(type(house))  



# 02_Subsetting Lists
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50] # Create the areas list

print(areas[-1]) # Print out last element from areas
print(areas[5]) # Print out the area of the living room
print(areas[1]) # Print out second element from areas

eat_sleep_area = areas[3] + areas[-3] # Sum of kitchen and bedroom area
print(eat_sleep_area)

downstairs = areas[:6] # Use slicing to create downstairs
upstairs = areas[6:] # Use slicing to create upstairs
print(downstairs)
print(upstairs)



# 03_Manipulating Lists

areas[9]= 10.50 # Correct the bathroom area
areas[4]="chill zone" # Change "living room" to "chill zone"
print(areas)

areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,"bedroom", 10.75, "bathroom", 10.50] # Create the areas list and make some changes
areas_1 = areas + ["poolhouse", 24.5] # Add poolhouse data to areas, new list is areas_1
areas_2 = areas_1 + ["garage", 15.45] # Add garage data to areas_1, new list is areas_2
print(areas_2)

areas_copy = areas[:] # Create areas_copy
areas_copy[0] = 5.0 # Change areas_copy
print(areas)
print(areas_copy)