expense1_name = input("entrer le nom de l'expense 1: ")
price1 = float(input("entrer le prix de l'expense 1: "))
category1 = input("entrer la categorie de l'expense 1: ")

print(f"Expense: {expense1_name}")
print(f"Price: {price1} MAD")
print(f"Category: {category1}")

expense2_name = input("entrer le nom de l'expense 2: ")
price2 = float(input("entrer le prix de l'expense 2: "))
category2 = input("entrer la categorie de l'expense 2: ")

print(f"Expense: {expense2_name}")
print(f"Price: {price2} MAD")
print(f"Category: {category2}")

somme_expenses = price1 + price2
print(f"Total expenses: {somme_expenses} MAD")
print("Expense Program finished")

average_expense = somme_expenses / 2
print(f"Average expense: {average_expense} MAD")
