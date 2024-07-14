import read


def Exception_Hanndling():
    # This function is used to print out for exception of the integer value
    print("\n")
    print("Dear User, Please Enter a valid input. (Only Integers Are Allowed)")
    print("\n")

    
def Design():
     #This function is used for the design of the heading of the table
     print("|----------------------------------------------------------------------------------------|")
     print("|S.N  Laptop Name         Company Name    Price     Quantity    RAM           Graphics   |")
     print("|----------------------------------------------------------------------------------------|")

def for_Yes_No():
    #This function is used for the expection for yes or no
    print("\n")
    print("\t\tDear User, Only y and n are allowed")
    print("\n")
    
def for_alpha():
    #This function is used fot the handling exception for alphabet
    print("\n")
    print("\t\tInvalid Input. Only Alphabet Allowed")
    print("\n")


    
def Checking_Id():
    """This function checks if the user given id is correct or not if not it asks until the user have given the correct id and returns the id"""
    
    Available_Laptops = read.Reading_File()
    while True:
        try:
            given_id = int(input("Please provide the ID number of the laptop you want available from our shop: "))
   
            if given_id <= 0 or given_id > len( Available_Laptops):
                    print("\n")
                    print("Dear User, Your input does not match from the laptop Id that we have, Please Provide Valid Id from (1-5)")
                    print("\n")
            else:
                return given_id
        except:
            Exception_Hanndling()

    return given_id
        
        



def Quantity_For_Sale(given_id):
    """This function checks if the user given quantity is available or not and it takes given_id as parameter to get the value of it and returns quantity"""
    Available_Laptops = read.Reading_File()
   
    while True:
        try:
            wanted_amount_of_laptop = int(input("Dear User,Please provide the number of quantity of the laptop:"))
            print("\n")

            Quantity_Available_From_Shop =  Available_Laptops[given_id][3]
            if wanted_amount_of_laptop <= 0 or wanted_amount_of_laptop > int(Quantity_Available_From_Shop):
                print("\n")
                print("Dear User, The quantity you are looking for is not available in out shop ")
                print("\n")
                if int(Quantity_Available_From_Shop) == 0:
                    print("Sorry! We are out of stock.")
                    print("\n")
                    break
            
            else:
                return wanted_amount_of_laptop
        except:
            Exception_Hanndling()
        
           

    return wanted_amount_of_laptop
   

           

        

def Hello():
    # This function is used to one user to buy multiple laptops this is inner loop there is also outer loop in main.py
    while True:
        try:
            Ask = input("Do You want to sale more laptop?(Y/N)")
            if Ask.lower()=="y":
                return True
            elif Ask.lower()=="n":
                return False
            else:
                raise ValueError
        except ValueError:
            for_Yes_No()
            



def Quantity_For_Purchase(given_id):
    #This function only take quantity from rhe user and it takes id as a paramter to get the value of it
    Available_Laptops = read.Reading_File()
    while True:
        try:
            wanted_amount_of_laptop = int(input("Please provide the number of quantity of the laptop you want to buy: "))
            print("\n")
            
            return wanted_amount_of_laptop
        except ValueError:
            Exception_Hanndling()
    return wanted_amount_of_laptop



def Hello1():
    # This function is used to one user to buy multiple laptops this is inner loop there is also outer loop in main.py
    while True:
        try:
            Ask = input("Do You want to buy more laptop?(Y/N)")
            if Ask.lower()=="y":
                return True
            elif Ask.lower()=="n":
                return False
            else:
                raise ValueError
        except ValueError:
            for_Yes_No()

