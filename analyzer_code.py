
# =====================================================
#           PERSONAL EXPENSE ANALYZER
# =====================================================

# Function 1: Validate and collect positive amounts

def get_positive_amount(message):

    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("Amount cannot be negative. Try again.")

            else:
                return amount

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function 2: Collect user and expense details

def add_expenses():

    print("\n========== ADD MONTHLY EXPENSES ==========")

    while True:
        name = input("Enter your name: ").strip()

        if name:
            break

        print("Name cannot be empty!")

    income = get_positive_amount("Enter monthly income: ₹")

    expenses = {}

    expenses["Food"] = get_positive_amount("Enter food expenses: ₹")
    expenses["Rent"] = get_positive_amount("Enter rent expenses: ₹")
    expenses["Transport"] = get_positive_amount("Enter transport expenses: ₹")
    expenses["Shopping"] = get_positive_amount("Enter shopping expenses: ₹")
    expenses["Entertainment"] = get_positive_amount("Enter entertainment expenses: ₹")
    expenses["Others"] = get_positive_amount("Enter other expenses: ₹")

    data = {
        "name": name,
        "income": income,
        "expenses": expenses
    }

    print("\nExpenses added successfully!")

    return data


# Function 3: Calculate total expenses

def calculate_total_expenses(expenses):

    return sum(expenses.values())


# Function 4: Calculate savings

def calculate_savings(income, total_expenses):

    savings = income - total_expenses

    if income > 0:
        percentage = (savings / income) * 100
    else:
        percentage = 0

    return savings, percentage


# Function 5: Determine financial status

def get_financial_status(savings, percentage):

    if savings < 0:
        return "Overspending"

    elif percentage >= 50:
        return "Excellent Savings"

    elif percentage >= 30:
        return "Good Savings"

    elif percentage >= 10:
        return "Moderate Savings"

    else:
        return "Low Savings"


# Function 6: Display expense report

def view_report(data):

    expenses = data["expenses"]
    income = data["income"]

    total = calculate_total_expenses(expenses)

    savings, percentage = calculate_savings(income, total)

    status = get_financial_status(savings, percentage)

    print("\n==========================================")
    print("          MONTHLY EXPENSE REPORT")
    print("==========================================")

    print("Name:", data["name"])
    print("Monthly Income: ₹", round(income, 2))

    print("\n---------- EXPENSE BREAKDOWN ----------")

    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")

    print("------------------------------------------")

    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Remaining Savings: ₹{savings:.2f}")
    print(f"Savings Percentage: {percentage:.2f}%")

    print("------------------------------------------")

    print("Financial Status:", status)

    if savings < 0:
        print("Warning: Your expenses exceed your income!")

    # Find highest expense category

    highest_category = max(expenses, key=expenses.get)

    print("Highest Expense Category:", highest_category)

    # Additional expense analysis

    if income > 0 and data["expenses"]["Rent"] > income * 0.40:
        print("Warning: Rent exceeds 40% of your income.")

    if data["expenses"]["Shopping"] > 5000:
        print("Warning: Shopping expenses exceed ₹5,000.")

    print("==========================================")

    return total, savings, percentage


# Function 7: Save report to a text file

def save_report(data):

    expenses = data["expenses"]
    total = calculate_total_expenses(expenses)

    savings, percentage = calculate_savings(
        data["income"], total
    )

    status = get_financial_status(savings, percentage)

    try:

        with open("expense_report.txt", "a", encoding="utf-8") as file:

            file.write("\n====================================\n")
            file.write("       PERSONAL EXPENSE REPORT\n")
            file.write("====================================\n")

            file.write(f"Name: {data['name']}\n")
            file.write(f"Monthly Income: ₹{data['income']:.2f}\n")

            for category, amount in expenses.items():
                file.write(f"{category}: ₹{amount:.2f}\n")

            file.write(f"Total Expenses: ₹{total:.2f}\n")
            file.write(f"Savings: ₹{savings:.2f}\n")
            file.write(f"Savings Percentage: {percentage:.2f}%\n")
            file.write(f"Financial Status: {status}\n")

            file.write("====================================\n")

        print("Report saved successfully!")

    except OSError as error:
        print("Unable to save report:", error)


# Function 8: Read saved reports

def view_saved_reports():

    try:

        with open("expense_report.txt", "r", encoding="utf-8") as file:

            content = file.read()

            if content:
                print("\n========== SAVED EXPENSE REPORTS ==========")
                print(content)

            else:
                print("No saved reports found!")

    except FileNotFoundError:
        print("No saved reports found yet.")

    except OSError as error:
        print("Unable to read reports:", error)


# Function 9: Display menu

def show_menu():

    print("\n==========================================")
    print("         PERSONAL EXPENSE ANALYZER")
    print("==========================================")

    print("1. Add Monthly Expenses")
    print("2. View Expense Report")
    print("3. Save Expense Report")
    print("4. View Saved Reports")
    print("5. Exit")

    print("==========================================")


# Function 10: Main application


def main():

    expense_data = None

    while True:

        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            expense_data = add_expenses()

        elif choice == "2":
            if expense_data is None:
                print("Please select option 1 and add expenses first!")
            else:
                view_report(expense_data)

        elif choice == "3":
            if expense_data is None:
                print("Please add expenses first!")
            else:
                save_report(expense_data)

        elif choice == "4":
            view_saved_reports()

        elif choice == "5":
            print("Thank you for using Personal Expense Analyzer!")
            break

        else:
            print("Invalid choice! Enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

