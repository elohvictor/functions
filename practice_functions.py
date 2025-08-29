import costom_functions

C = int(input("Enter temperature in celsius :"))
F = costom_functions.convertCelsiusToFarhenheit(C)
print(F)

amount_purchase = int(input("Enter amount: "))
if(amount_purchase < 5000):
    print("No discount. Try next time")
elif(amount_purchase >= 5000 and amount_purchase < 8000):
    discount = costom_functions.discountOnPurchase(amount_purchase,3)
    print("3% discount")
    print(f"amount = {amount_purchase}")
    print(f"discount = {discount}")
    print(f"total amount = {amount_purchase - discount}")
elif(amount_purchase >= 8000 and amount_purchase < 10000):
    discount = costom_functions.discountOnPurchase(amount_purchase,5)
    print("5% discount")
    print(f"amount = {amount_purchase}")
    print(f"discount = {discount}")
    print(f"total amount = {amount_purchase - discount}")
elif (amount_purchase >= 10000 and amount_purchase < 50000):
    discount = costom_functions.discountOnPurchase(amount_purchase,10)
    print("10% discount")
    print(f"amount = {amount_purchase}")
    print(f"discount = {discount}")
    print(f"total amount = {amount_purchase - discount}")
elif (amount_purchase >= 50000):
    discount = costom_functions.discountOnPurchase(amount_purchase,15)
    print("15% discount")
    print(f"amount = {amount_purchase}")
    print(f"discount = {discount}")
    print(f"total amount = {amount_purchase - discount}")


user_input = input("Enter username: ")
pass_word = input("Enter password: ")
if (costom_functions.validatePasswordLength(pass_word)==False):
    print("password must not be less than 6 characters")
else:
    print("Access Denied")
    

year = int(input("Enter year: "))
if (costom_functions.validateYearDates(year)==True):
    print("Ieap year")
else:
    print("Not a leap year")
