import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import shutil
import os

input_file = 'expenses.csv'

def add_expense():
    try:
        name = input("Enter your name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description of expense: ")
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., groceries, utilities): ")

        new_data = pd.DataFrame([[name, date, description, amount, category]],
                                columns=['Name', 'Date', 'Description', 'Amount', 'Category'])
        if os.path.exists(input_file):
            new_data.to_csv(input_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(input_file, mode='w', index=False)
        
        print("Expense logged successfully!")
    except Exception as e:
        print(f"Error logging expense: {e}")

def analyze_expenses():
    try:
        df = pd.read_csv(input_file)
        member_totals = df.groupby('Name')['Amount'].sum()
        total_expenses = df['Amount'].sum()
        days = (datetime.now() - datetime.strptime(df['Date'].min(), "%Y-%m-%d")).days + 1
        average_daily_expense = total_expenses / days

        print("Total expenses for each member:")
        print(member_totals)
        print(f"\nAverage daily expense for the household: {average_daily_expense:.2f}")
    except Exception as e:
        print(f"Error analyzing expenses: {e}")

def plot_expense_trends():
    try:
        df = pd.read_csv(input_file)
        df['Date'] = pd.to_datetime(df['Date'])
        daily_expense = df.groupby('Date')['Amount'].sum().cumsum()

        plt.figure(figsize=(10, 5))
        plt.plot(daily_expense.index, daily_expense.values, marker='o')
        plt.xlabel("Date")
        plt.ylabel("Cumulative Expenses")
        plt.title("Expense Trends Over the Last Month")
        plt.xticks()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating expense trends: {e}")

def monthly_report(month, year):
    try:
        df = pd.read_csv(input_file)
        df['Date'] = pd.to_datetime(df['Date'])
        monthly_df = df[(df['Date'].dt.month == month) & (df['Date'].dt.year == year)]

        member_totals = monthly_df.groupby('Name')['Amount'].sum()
        category_totals = monthly_df.groupby('Category')['Amount'].sum()

        print(f"Total expenses for each member in {month}/{year}:")
        print(member_totals)
        print("\nBreakdown by category:")
        print(category_totals)

        monthly_totals = df.groupby(df['Date'].dt.to_period("M"))['Amount'].sum()
        monthly_totals.plot(kind='bar')
        plt.xlabel("Month")
        plt.ylabel("Total Expenses")
        plt.title("Monthly Expense Comparison")
        plt.show()
    except Exception as e:
        print(f"Error generating monthly report: {e}")

def set_budget():
    budgets = {}
    categories = input("Enter categories (comma-separated): ").split(',')
    for category in categories:
        budgets[category.strip()] = float(input(f"Set monthly budget for {category.strip()}: "))
    return budgets

def check_budget():
    try:
        df = pd.read_csv(input_file)
        budgets = set_budget()
        df['Date'] = pd.to_datetime(df['Date'])
        monthly_df = df[df['Date'].dt.month == datetime.now().month]
        category_totals = monthly_df.groupby('Category')['Amount'].sum()

        for category, budget in budgets.items():
            spent = category_totals.get(category, 0)
            remaining = budget - spent
            if remaining < 0:
                print(f"Warning: Budget exceeded for {category} by {-remaining:.2f}")
            else:
                print(f"{category}: {remaining:.2f} remaining in budget.")
    except Exception as e:
        print(f"Error checking budget: {e}")

def backup_data():
    try:
        shutil.copy(input_file, 'backup_' + input_file)
        print("Backup created successfully.")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_data():
    try:
        if os.path.exists('backup_' + input_file):
            shutil.copy('backup_' + input_file, input_file)
            print("Data restored from backup.")
        else:
            print("No backup file found.")
    except Exception as e:
        print(f"Error restoring data: {e}")

def main():
    print("Name: Dev Mehta\nRoll No: 22BCP282")
    while True:
        print("\nHousehold Expense Management")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. View Expense Trends")
        print("4. Generate Monthly Report")
        print("5. Set and Check Budget")
        print("6. Backup Data")
        print("7. Restore Data")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            analyze_expenses()
        elif choice == '3':
            plot_expense_trends()
        elif choice == '4':
            month = int(input("Enter month (MM): "))
            year = int(input("Enter year (YYYY): "))
            monthly_report(month, year)
        elif choice == '5':
            check_budget()
        elif choice == '6':
            backup_data()
        elif choice == '7':
            restore_data()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
