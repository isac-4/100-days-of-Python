print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ :"))
split = int(input("How many people to split the bill? : "))
tip = int(input("How much tip would you like to give? : "))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

