# Tip Calculator

This is a simple tip calculator script written in Python. It helps you calculate the total bill including the tip and splits it among a specified number of people.

### Welcome Message:
This line prints a welcome message to the user, introducing the purpose of the script.  
`print('Welcome to the tip calculator!')`  
### Total Bill Amount
This line prompts the user to input the total bill amount and then `float()` converts the user input from a string to a floating-point number, allowing for decimal values.  
`bill = float(input('What was the total bill?\n$'))`
### Get the Desired Tip Percentage
This line prompts the user to input the tip percentage they want to give then `int()` converts the user input from a string to an integer.  
`tip = int(input('How much tip would you like to give? 10, 12, or 15?\n'))`
### Number of People to Split the Bill
Asks the user for the number of people then `int()` converts the user input from a string to an integer.  
`people = int(input('How many people to split the bill?\n'))`
### Calculate the tip
Converts the tip percentage to a decimal and calculates the total tip amount.  
`total_tip = (tip / 100) * bill`
### Total Bill Including the Tip
Adds the total tip to the original bill to get the final total.  
`total = bill + total_tip`
### Amount Each Person Should Pay
Divides the total bill by the number of people to find the share for each person.  
`bill_per_person = total / people`
### Format the Amount to 2 Decimal Places
Using the `'{:.2f}'.format()` formats the amount each person should pay to two decimal places for a cleaner display.   
`rounded_per_person = '{:.2f}'.format(bill_per_person)`
### Display the Amount Each Person Should Pay
Uses an f-string to insert the formatted amount into the message.  
`print(f'Each person should pay:\n{rounded_per_person}')`
