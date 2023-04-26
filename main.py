# Tip calculator app with custom tip option

print("Welcome to the tip calculator app!")

# Ask user for the total bill amount
total_bill = float(input("What was the total bill? $"))

# Display the tip options
print("\nHow much tip would you like to leave?")
print("1. 15%")
print("2. 20%")
print("3. 25%")
print("4. Custom")

# Ask user to choose a tip option
tip_choice = input("Enter the number of your choice: ")

# Calculate the tip amount based on the user's choice
if tip_choice == "1":
    tip_percentage = 15
elif tip_choice == "2":
    tip_percentage = 20
elif tip_choice == "3":
    tip_percentage = 25
elif tip_choice == "4":
    tip_percentage = float(input("Enter the custom tip percentage: "))
else:
    print("Invalid choice. Please try again.")
    exit()

# Calculate tip amount and total amount to pay
tip_amount = round(total_bill * (tip_percentage / 100), 2)
total_amount = round(total_bill + tip_amount, 2)

# Display the tip amount and total amount to pay
print(f"\nTip amount: ${tip_amount}")
print(f"Total amount to pay: ${total_amount}")
