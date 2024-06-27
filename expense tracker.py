class Expense:
    def __init__(self, amount, description, category, date):
        self.amount = float(amount)
        self.description = description
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def display_monthly_summary(self):
        monthly_expenses = {}
        for expense in self.expenses:
            month = expense.date.strftime("%B")
            if month in monthly_expenses:
                monthly_expenses[month] += expense.amount
            else:
                monthly_expenses[month] = expense.amount
        for month, total in monthly_expenses.items():
            print(f"Total expenses for {month}: ${total:.2f}")

    def display_category_wise_expenditure(self):
        category_expenses = {}
        for expense in self.expenses:
            if expense.category in category_expenses:
                category_expenses[expense.category] += expense.amount
            else:
                category_expenses[expense.category] = expense.amount
        for category, total in category_expenses.items():
            print(f"Total expenses for {category}: ${total:.2f}")

def main():
    tracker = ExpenseTracker()
    while True:
        user_input = input("Enter your expense (amount description category date(yyyy-mm-dd)) or type 'summary' for monthly summary, 'categories' for category-wise expenditure, or 'quit' to exit: ")
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "summary":
            tracker.display_monthly_summary()
        elif user_input.lower() == "categories":
            tracker.display_category_wise_expenditure()
        else:
            try:
                amount, description, category, date = user_input.split()
                expense = Expense(amount, description, category, datetime.datetime.strptime(date, "%Y-%m-%d"))
                tracker.add_expense(expense)
            except ValueError:
                print("Invalid input. Please enter in the format: amount description category date(yyyy-mm-dd)")

if __name__ == "__main__":
    import datetime
    main()