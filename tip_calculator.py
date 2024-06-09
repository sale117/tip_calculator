print('Welcome to the tip calculator!')
bill = float(input('What was the total bill?\n$'))
tip = int(input('How much tip would you like to give? 10, 12, or 15?\n'))
people = int(input('How many people to split the bill?\n'))
total_tip = (tip / 100) * bill
total = bill + total_tip
bill_per_person = total / people
rounded_per_person = '{:.2f}'.format(bill_per_person)
print(f'Each person should pay:\n{rounded_per_person}')