# expense_tracker.py
import json
from datetime import datetime
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    amount = float(input("Enter amount: $"))
    category = input("Enter category (food, travel, bills, etc.): ").strip().lower()
    note = input("Optional note: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")
    expense = {"amount": amount, "category": category, "note": note, "date": date}

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added ${amount:.2f} for {category} on {date}.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return

    total = 0
    print("\n--- All Expenses ---")
    for e in expenses:
        print(f"{e['date']} - ${e['amount']:.2f} ({e['category']}) {e['note']}")
        total += e['amount']
    print(f"\n💰 Total Spent: ${total:.2f}")

def view_summary():
    expenses = load_expenses()
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n--- Expense Summary by Category ---")
    for cat, amt in summary.items():
        print(f"{cat.title()}: ${amt:.2f}")

def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
