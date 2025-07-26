import csv

def add_expense():
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        date = input("Date (YYYY-MM-DD): ")
        desc = input("Description: ")
        amount = float(input("Amount: "))
        writer.writerow([date, desc, amount])
        print("Expense recorded.")

def view_expenses():
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

print("1. Add Expense\n2. View Expenses")
choice = input("Choose: ")
if choice == "1":
    add_expense()
elif choice == "2":
    view_expenses()
