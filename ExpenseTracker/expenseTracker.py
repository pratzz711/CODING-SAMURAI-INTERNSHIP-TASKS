import os
import datetime
import pandas as pd

class ExpenseTracker:
    def __init__(self):
        self.expenseList = []

    def addExpense(self,date,amount,category,description):
        expense = {
        "Date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "Amount": amount,
        "Category": category,
        "Description": description
        }
        self.expenseList.append(expense)
        print("\nExpense added successfully!")

    def listExpenses(self):
        if self.expenseList != []:
            print("\n-------------------------Expense List--------------------------")
            df = pd.DataFrame(self.expenseList)
            df.index = df.index +1
            print(df, "\n")
        else:
            print("\nNo Expenses found")

    def totalExpense(self):
        try:
            start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
            end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
            amount = 0
            for expense in self.expenseList:
                if (start_date <= datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S") <= end_date):
                    amount += expense["Amount"]
            print(f"\nThe Total Amount from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} is : {amount}")
        except ValueError:
            print("You have entered the wrong date format. Please use YYYY-MM-DD.")

    def monthlyReport(self):
        try:
            report_month = datetime.datetime.strptime(input("Enter report month in (YYYY-MM): "), "%Y-%m")
            monthly_expenses = []
            categories = set()
            category_amount = 0
            for expense in self.expenseList:
                if (datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S").month == report_month.month):
                    monthly_expenses.append(expense)
            
            if len(monthly_expenses) == 0:
                print("No expenses found for the mentioned month.")
            else:
                print(f"\nMonthly Report for {report_month.strftime('%B %Y')}:")
                for expense in monthly_expenses:
                    categories.add(expense['Category'])
                    
                for category in categories:
                    for expense in monthly_expenses:
                        if expense['Category'] == category:
                            category_amount += expense['Amount']
                    print(f"{category}: {category_amount}")
                    category_amount = 0
        except ValueError:
            print("Invalid date format. Please use YYYY-MM.")

    def saveExpenses(self):
        with open("expenses.txt", "w") as file:
            for expense in self.expenseList:
                file.write(f"{expense['Date']},{expense['Amount']},{expense['Category']},{expense['Description']}\n")
        print("Expenses saved to 'expenses.txt'\n")

    def loadExpenses(self):
        if os.path.exists("expenses.txt"):
            with open("expenses.txt", "r") as file:
                for line in file:
                    date, amount, category, description = line.strip().split(",")
                    self.expenseList.append({
                        "Date": date,
                        "Amount": float(amount),
                        "Category": category,
                        "Description": description
                    })
            print("\nExpenses loaded from 'expenses.txt'.")

if __name__ == "__main__":
    expenses = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses for a given Time")
        print("4. Generate Monthly Report")
        print("5. Save Expenses and Exit")
        print("6. Load Expenses")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            date = datetime.datetime.now()
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            description = input("Write a description: ")
            expenses.addExpense(date,amount,category,description)
        elif choice == "2":
            expenses.listExpenses()
        elif choice == "3":
            expenses.totalExpense()
        elif choice == "4":
            expenses.monthlyReport()
        elif choice == "5":
            expenses.saveExpenses()
            break
        elif choice == "6":
            expenses.loadExpenses()
        else:
            print("Invalid choice!!")