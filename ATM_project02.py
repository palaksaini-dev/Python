balance = 25000
user_pin = 2010
pin = int (input("Enter your pin:"))

if pin == user_pin:
    print ("PIN is correct!")

    while True :
        print ("1. Check Balance")
        print ("2. Withdraw Money")
        print ("3. Deposit Money")
        print ("4. Exit")

        choice = int (input("Enter your choice:"))


        if choice == 1 :
            print ("Your balance is:", balance)


        elif choice == 2 :
            money = int (input ("Enter amount to withdraw:"))

            if money > 0 :

                if money <= balance :
                    balance = balance - money
                    print ("Money withdraw successfully")
                    print ("Remaining balance", balance)
                else :
                    print ("Not enough balance")
            else :
                print ("Enter a positive amount")


        elif choice == 3 :
            money = int (input ("Enter amount to deposite:"))

            if money > 0 :
                balance = balance + money
                print ("Money deposited successfully")
                print ("New balance", balance)
            else :
                print ("Enter positive amount")


        elif choice == 4 :
            print ("Thank you for using ATM")

            break
        else :
            print ("Wrong choice")
            

else :
    print ("Wrong PIN")
            