name = input("Enter your name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

salary = hours_worked * hourly_rate

print("\n--- Salary Details ---")
print("Employee:", name)
print("Hours Worked:", hours_worked)
print("Hourly Rate: ₱", hourly_rate)
print("Total Salary: ₱", salary)

