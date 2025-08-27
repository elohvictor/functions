#returns discount on amount_purchase 
def discountOnPurchase(amount_purchase,interest_rate):
    discount = (amount_purchase * interest_rate) /100
    return discount

#returns the modulus of any number
def modulusOfNumber(number1,number2):
    modulus = (number1 % number2)
    return modulus;

#convert celsius to farhenheit
def convertCelsiusToFarhenheit(temperature):
    return (temperature*9/5)+35

#authentication
def userLogin(user_name,password):
    return user_name=="admin" and password=="password123"


def validatePasswordLength(password):
    return len(password)>=6


def validateYearDates(year):
    return year%4==0 and year%100!=0 or year %400==0



    
# amount = int(input('Enter amount_purchase:'))
# rate = 3
# discount_amount = discountOnPurchase(amount,rate)
# print('discount amount =',discount_amount)


# number = modulusOfNumber(10,3)
# print("modulus =",number)

def validatePinLength(pin):
    if len(pin) == 4:
        return True
    else:
        return False


def validatePin(pin,default_pin='1234'):
    if pin != default_pin:
        return False
    else:
        return True
    


def debitAmount(amount,balance=5000):
    if amount>balance:
        return False
    else:
        return True 
    
def balanceAfterDebit(amount,balance=5000):
    return balance-amount            


def validateAccountNumberLength(accountNumber):
    if len(accountNumber) == 10:
        return True
    else:
        return False
    
    
def balanceAfterCredit(amount,balance=5000):
    return balance+amount   
    
    
    

def salesDiscount(amount_purchase):
    if(amount_purchase < 5000):
        print("No discount. Try next time")
    elif(amount_purchase >= 5000 and amount_purchase < 8000):
        discount = amount_purchase*3/100
        print("3% discount")
        print(f"amount = {amount_purchase}")
        print(f"discount = {discount}")
        print(f"total amount = {amount_purchase - discount}")
    elif(amount_purchase >= 8000 and amount_purchase < 10000):
        discount = amount_purchase*5/100
        print("5% discount")
        print(f"amount = {amount_purchase}")
        print(f"discount = {discount}")
        print(f"total amount = {amount_purchase - discount}")
    elif (amount_purchase >= 10000 and amount_purchase < 50000):
        discount = amount_purchase*10/100
        print("10% discount")
        print(f"amount = {amount_purchase}")
        print(f"discount = {discount}")
        print(f"total amount = {amount_purchase - discount}")
    elif (amount_purchase >= 50000):
        discount = amount_purchase*15/100
        print("15% discount")
        print(f"amount = {amount_purchase}")
        print(f"discount = {discount}")
        print(f"total amount = {amount_purchase - discount}")


