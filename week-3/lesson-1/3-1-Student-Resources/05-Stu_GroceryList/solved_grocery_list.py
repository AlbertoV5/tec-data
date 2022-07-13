# Create a Python list to store your grocery list
groceries = ["Milk", "Jelly", "Orange Juice","Peanut Butter"]
# Print the grocery list
print(groceries)
# Change "Peanut Butter" to "Almond Butter" and print out the updated list
groceries[groceries.index("Peanut Butter")] = "Almond Butter"
print(groceries)
# Remove "Jelly" from grocery list and print out the updated list
groceries.remove("Jelly")
print(groceries)
# Add "Coffee" to grocery list and print the updated list
groceries.append("Coffee")
print(groceries)