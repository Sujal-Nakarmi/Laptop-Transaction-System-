
import read
import operations
import write


print("\n")
print("-----------------------------------------------------------------------")
print("\t\t\tWelcome to Nakarmi Shop")
print("-----------------------------------------------------------------------")
print("\n")
print("Dear User, Please Selected One Option To continue")
print("\n")

loop=True
while loop == True:

    try: # Using try except
     
     print("Press 1 to show the details of laptop.")
     print("Press 2 to sale the laptop to customer.")
     print("Press 3 to purchase from Manufacturer.")
     print("Press 4 to Exit from the system.")
     
     Choice_Of_User = int(input("Enter the option to continue: "))

     print("\n")
    except:
        operations.Exception_Hanndling() # Calling the function from operation.py

        continue # It is used so that the program doesnt end after the exception

 

    if Choice_Of_User == 1:
            print("We have following Laptops available:\n ")

            operations.Design()
            read.Laptop_Display()
            print("\n")
            

    elif Choice_Of_User  == 2:
        
            operations.Design()
           
            read.Laptop_Display()

            print("\n")
            

            loopSale = True

            while loopSale == True:

                checkingId = operations.Checking_Id()
                print("\n")
               

                QuantityCheck = operations.Quantity_For_Sale(checkingId) # Passing the id given by checkingId as parameter
                print("\n")
                
                

                Updated  = write.Writing_Updated_Value_For_Sale(checkingId,QuantityCheck) # getting the id and quantity given the user as a parameter
                

                if operations.Hello():
                    continue
                else:
                    loopSale = False # Loop Ends

                    
                

                Bill = write.Bill_Printing(checkingId,QuantityCheck)
                

           
                   
                   
    elif Choice_Of_User  == 3:

            operations.Design()

           
           
            read.Laptop_Display()
            print("\n")
        

            loopPurchase = True

            while loopPurchase == True:

                checkingId =operations.Checking_Id()
                print("\n")
              

                QuantityCheck = operations.Quantity_For_Purchase(checkingId)
                print("\n")

                Updated  = write.Writing_Updated_Value_For_Purchasee(checkingId,QuantityCheck)
                

                if operations.Hello1():
                    continue
                else:
                    loopPurchase = False

                    

                Bill = write.Bill_Printing_For_Purchasee(checkingId,QuantityCheck)
                

           
           
    elif Choice_Of_User  == 4:
            loop = False
            
            print("Thank you for using the system, have a good day Admin!")
            print("\n")

    else:
            print("Your option",Choice_Of_User,"does not seem to match as per our requirement. Please look at the provided option. Only From(1-4)")
            print("\n")
