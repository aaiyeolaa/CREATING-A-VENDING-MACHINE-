#for inserting money
further = True

#Amount of cents in the machine
centsInMachine = 0

#Prices for the drinks
cokePrice = 25
pepsiPrice = 35
sodaPrice = 45

#Number of drinks that are in the machine
count = 10

#sets the count of drinks to 0
def resetMachine():
    return 0

#cancels the deal
def cancel(centsInMachine):
    print("Here is your refund of " + str(centsInMachine) + " cents")
    exit(0)

#user can enter coins
def enterCoins(further, centsInMachine, cokePrice, pepsiPrice, sodaPrice):
    # Input as long as the user wants
    while further:
        print("Do you want to insert a / another coin? [y,n]")
        f1 = input(">>> ")
        # c... to cancel the process
        if f1.lower() == 'c':
            cancel(centsInMachine)
        # if f1 is not y then the user doesn´t want to enter antother coin and the buyItems
        elif f1.lower() != 'y':
            # further is set to False so the loop doesn´t run anymore
            further == False
            break
        print("Which coin do you want to insert? [1,5,10,25]")
        coin = int(input(">>> "))
        # Check if the entered coin is a valid coin
        if coin == 1 or coin == 5 or coin == 10 or coin == 25:
            centsInMachine += coin
            print("The machine contains " + str(centsInMachine) + " cent")
        else:
            print("Your coin doesn´t exist. Please enter another coin.")
    # The "buy-part" begins
    buyItem(centsInMachine, cokePrice, pepsiPrice, sodaPrice)

#buy drinks
def buyItem(centsInMachine, cokePrice, pepsiPrice, sodaPrice):
    #1 is Coke, 2 is Pepsi, 3 is Soda
    print("Which drink do you want to buy? [1,2,3]")
    drinkId = int(input(">>> "))
    # Check if selected drink is Coke
    if drinkId == 1:
        # Check if user has enough money to buy Coke
        if int(centsInMachine) >= cokePrice:
            # The price in the machine gets reduced by the price of the drink
            centsInMachine -= cokePrice
            print("Here is your Coke!")
            print("\nHere is you change of " + str(centsInMachine) + " cents!")
        else:
            print("You have to little money to buy a coke.")
            enterCoins(further, centsInMachine, cokePrice, pepsiPrice, sodaPrice)
    # Check if selected drink is Pepsi
    elif drinkId == 2:
        # Check if user has enough money to buy Pepsi
        if int(centsInMachine) >= pepsiPrice:
            # The price in the machine gets reduced by the price of the drink
            centsInMachine -= pepsiPrice
            print("Here is your Pepsi!")
            print("\nHere is you change of " + str(centsInMachine) + " cents!")
        else:
            print("You have to little money to buy a Pepsi.")
            enterCoins(further, centsInMachine, cokePrice, pepsiPrice, sodaPrice)
    # Check if selected drink is Soda
    elif drinkId == 3:
        # Check if user has enough money to buy Soda
        if int(centsInMachine) >= sodaPrice:
            # The price in the machine gets reduced by the price of the drink
            centsInMachine -= sodaPrice
            print("Here is your Soda!")
            print("\nHere is you change of " + str(centsInMachine) + " cents!")
        else:
            print("You have to little money to buy a Soda.")
            enterCoins(further, centsInMachine, cokePrice, pepsiPrice, sodaPrice)


# prints out the Price list
print("Price list:")
print("-----------")
print("1 Coke   25")
print("2 Pepsi  35")
print("3 Soda   45")
print("\nEnter 'c' to cancel")

inp = input()
# The supplier can reset the machine
if inp == "I am the supplier":
    count = resetMachine()
    
# If the count of drinks is greater than 0 the machine is able to give out drinks
if count > 0:
    centsInMachine = enterCoins(further, centsInMachine, cokePrice, pepsiPrice, sodaPrice)
else:
    print("There are no drink to buy!")




