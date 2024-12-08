import csv
from datetime import datetime

def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
    print("-" * 37)
    for expense in expenses:
        print(f"{expense['category']:<15}{expense['amount']:<10.2f}{expense['date']:<12}")

def calculate_totals_by_category(expenses):
    totals = {}
    for expense in expenses:
        category = expense['category']
        totals[category] = totals.get(category, 0) + expense['amount']
    print("\nTotal Expenses by Category:")
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")

def save_expenses_to_file(expenses, filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}!")

def load_expenses_from_file(filename="expenses.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            return [{"category": row["category"], "amount": float(row["amount"]), "date": row["date"]} for row in reader]
    except FileNotFoundError:
        return []

def main():
    expenses = load_expenses_from_file()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Totals by Category")
        print("4. Save Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_totals_by_category(expenses)
        elif choice == "4":
            save_expenses_to_file(expenses)
        elif choice == "5":
            save_expenses_to_file(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
