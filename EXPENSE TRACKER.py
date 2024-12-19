
class Expense:
    def __init__(self,date,description,amount):
        self.date=date
        self.description=description
        self.amount=amount
#     def__init__ method is like default constructor in C++ and Java. Constructors are used to initialize the object’s state.
# The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
class Expense_Tracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self,expense):
        self.expenses.append(expense)

    def remove_expense(self,index):
        if 0<=index<=len(self.expenses):
            self.expenses.remove(index)
            print("expense removed successfully")
        else:
            print("invalid expense index")

    def view_expenses(self):
        if len(self.expenses)==0:
            print("no expenses found")
        else:
            print("Expense List:")
            for i,expense in enumerate(self.expenses,start=1):
                print(f"{i}.Date:{expense.date},Description:{expense.description},Amount:${expense.Amount}")

    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        print(f"Total expenses:${total:0.2f}")

def main():
    tracker=Expense_Tracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1.ADD Expense")
        print("2.REMOVE Expense")
        print("3.VIEW Expense")
        print("4.TOTAL Expense")
        print("5.Exit")
        choice=input("enter the choice from above(choose 1-5)")
        if choice=='1':
            date=input("enter the date yyyy-mm-dd:")
            description=input("enter the description:")
            amount=float(input("enter the amount:$"))
            expense=Expense(date,description,amount)
            Expense_Tracker().add_expense(expense)
            print("Expenses are added successfully")
            Expense_Tracker().view_expenses()

        elif choice=="2":
            index=int(input("enter the expense index to remove:"))-1
            tracker.remove_expense(index)
        elif choice=='3':
            tracker.view_expenses()
        elif choice=='4':
            tracker.total_expenses()
        elif choice=='5':
            print("good bye")
            break
        else :
            print("invalid character")
if __name__==main():
    main()





