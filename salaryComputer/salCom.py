print("=== Employee Salary Calculator ===")

# Employee 1
print("\nEmployee 1")
name1 = input("Enter name: ")
hours1 = float(input("Enter hours worked: "))
rate1 = float(input("Enter hourly rate: "))

salary1 = hours1 * rate1

# Employee 2
print("\nEmployee 2")
name2 = input("Enter name: ")
hours2 = float(input("Enter hours worked: "))
rate2 = float(input("Enter hourly rate: "))

salary2 = hours2 * rate2

# Display results
print("\n=== Salary Details ===")
print("Employee:", name1)
print("Salary: ₱", salary1)

print("\nEmployee:", name2)
print("Salary: ₱", salary2)