# expense_tracker.py
def add_expense(amount, category):
    with open("expenses.txt", "a") as f:
        f.write(f"{category}: {amount}\n")
    print("✅ Expense added!")

def view_expenses():
    with open("expenses.txt", "r") as f:
        print(f.read())

while True:
    print("\n1. Add Expense  2. View Expenses  3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        amt = input("Amount: ")
        cat = input("Category: ")
        add_expense(amt, cat)
    elif choice == "2":
        view_expenses()
    else:
        break
