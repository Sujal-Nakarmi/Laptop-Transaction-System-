import read
import operations
from datetime import datetime




def Invoice_Generate():
        #This function is used for the design before asking the details
        
        print("|-------------------------------------------------------------------------|")
        print("|Dear User For Bill Generation you will have to enter your details first! |")
        print("|-------------------------------------------------------------------------|")
        print("\n")


def Laptop_Shop():
        #This function is used for the design of the laptop shop and address and phone number
        print("\n")
        print("\t \t \t \t \t Nakarmi Laptop Shop Bill")
        print("\n")
        print("\t \t\t\t New Road, Kathmandu | Phone No: 9863526287")
        print("\n")
       
        print("Laptop details are : ")
        print("\n")
        
def Bill_Laptop_Specs():
        #This function is used for the design of the heading of the table while printing bill
        print("\n")
        print("Purchase Details are:")
        print("|--------------------------------------------------------------------|")
        print("|Laptop Name          Brand        Qauntity       Price         Total|")
        print("|--------------------------------------------------------------------|")

def Thanks():
        #This function is used for thank you message
        print("\t\tThank You For Purchasing!! Feel Free to Come Again!! Have a Good Day!")
        print("\t\t Bill has been printed in the txt file also!!")


        
        

               


Creating_List_For_Multiple_Laptops=[]

def Writing_Updated_Value_For_Sale(given_id, wanted_amount_of_laptop):
    """This function is used to update out main text file which is laptop.txt and here also we created list so that all the items get
    added when one user purchase multiple laptops"""
    

    Available_Laptops = read.Reading_File()

    # Update the quantity of the specific laptop
    Available_Laptops[given_id][3] = int(Available_Laptops[given_id][3]) - int(wanted_amount_of_laptop)

    

    # Writing  the updated laptop details to the file laptop.txt it will print the subtracted value in the quantity
    with open("laptop.txt","w") as file:
            for values in Available_Laptops.values():
                file.write(str(values[0]+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
                file.write("\n")

    
    Laptopname_of_product=Available_Laptops[given_id][0]
    LaptopBrand = Available_Laptops[given_id][1]
    Laptopquantity = wanted_amount_of_laptop
    Laptopprice = Available_Laptops[given_id][2].replace("$","")
    total = wanted_amount_of_laptop * float(Laptopprice)
        
   

    


    #           (adding the intialized variable in the list which we created at the beiginning using append)
    
    Creating_List_For_Multiple_Laptops.append([Laptopname_of_product,LaptopBrand, Laptopquantity, Laptopprice,total])


    

   


                              

def Bill_Printing(given_id,wanted_amount_of_laptop):
        

        #This function is used to generate the bill in both shell and txt file after selling and id and quantity are passed as parameter to get value
        
        Available_Laptops = read.Reading_File()
        today_date_and_time = datetime.now()
       
        Invoice_Generate()

        
        while True: 
                try: # This is to check is the name is in alphabet or not
                        name = input("Please enter the name of the customer: ")
                        if not all(c.isalpha() or c.isspace() for c in name):
                                raise ValueError #(raise and ValueError are inbuilt function raise is used to raise an exception and valueerror to check datatype
                        break #loop ends
                except ValueError:
                        operations.for_alpha()
                        

        while True:
                try: #This is to check if the user have given integer value for phone or not
                        phone_number = int(input("Please enter the phone number of the customer: "))
                        break#loop ends
                
                except:
                        operations.Exception_Hanndling()
               

        while True:
                try: # This is to check is the address is in alphabet or not
                        address = input("Please enter your address: ")
                        if not all(c.isalpha() or c.isspace() for c in address):
                                raise ValueError 
                        break #loop ends
                except ValueError:
                        operations.for_alpha()
       
        while True:
           try:
        
                shipping_cost = input("Dear user, Do you want your laptop to be shipped? (Press Y for shipping Press N for not shipping)").upper()
        
        

                if shipping_cost=="Y":
                    shipping_cost = 250
                    break
                elif shipping_cost=="N":
                    shipping_cost = 0
                    break
                else:
                    raise ValueError
           except ValueError:
                
                operations.for_Yes_No()
                
        
        
        
        
            
         
        total_price = 0
        Laptop_Shop()

        print("Name of the Customer : "+str(name))
        print("Contact number : "+str(phone_number))
        print("Address : "+str(address))
        print("Date and time of purcahse : "+str(today_date_and_time))

       
        Bill_Laptop_Specs()

        for i in Creating_List_For_Multiple_Laptops:
           
            total_price += i[4]
            grand_total = total_price+shipping_cost
            today_date_and_time = datetime.now()
        
            print("|",str(i[0])," "*(14-len(str(i[0]))),
                  " ",str(i[1])," "*(13-len(str(i[1]))),
                  " ",str(i[2])," "*(9-len(str(i[2]))),
                  " ",str(i[3])," "*(9-len(str(i[3]))),
                  " ",str(i[4])," "*(9-len(str(i[4]))))
            
        if shipping_cost:
              print("\t\t\t\t\t\t\t Total : $"+str(total_price))
              print("\n")
              print("\t\t\tYour Shipping cost is :", shipping_cost)
              print("\t\t\t          Grand Total : $"+str(grand_total))
              print("\n")
              Thanks()
              
        else:
            print("\t\t\t\t\t\t\t Total : $"+str(total_price))
            print("\n")
            print("\n")
            print("\t\t\tGrand Total : $"+str(grand_total))
            Thanks()
            
        

        

        with open(str(name) + ".txt","w") as file:

         grand_total = total_price + shipping_cost
         today_date_and_time = datetime.now()
    
         
         file.write("\t \t \t \t Nakarmi Shop Bill")
         file.write("\n")
         
         file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255")
         file.write("\n")
         
       
         file.write("Laptop details are:")
         file.write("\n")
         file.write("\n")
       
         file.write("Name of the Customer:"+str(name))
         file.write("\n")
        
         file.write("Contact number:"+str(phone_number))
         file.write("\n")
        
         file.write("Address:"+str(address))
         file.write("\n")
         
         file.write("Date and time of sold Laptops: "+str(today_date_and_time)+"\n")
         file.write("\n")
       
       
         
         file.write("Purchase Details are:")

         file.write("\n")
         
         file.write("\n")
         file.write("|----------------------------------------------------------")
         file.write("\n")
         file.write("|Laptop Name     Brand      Qauntity     Price      Total")
         file.write("\n")
         file.write("|----------------------------------------------------------")
         file.write("\n")
         
         for i in Creating_List_For_Multiple_Laptops:
                    file.write("|"+str(i[0])+" "*(14-len(str(i[0])))+
                               " "+str(i[1])+" "*(14-len(str(i[1])))+
                               " "+str(i[2])+" "*(10-len(str(i[2])))+
                               " "+str(i[3])+" "*(10-len(str(i[3])))+
                               " "+str(i[4])+" "*(10-len(str(i[4])))+ "\n")
                    file.write("\n")
          
         
          
         if shipping_cost:
              file.write("\n")
              file.write("\t\t\t\t\t\t\t Total : $"+str(total_price))
              file.write("\n")
              file.write("Your Shipping cost is :" +str(shipping_cost))
              file.write("\n")
          
              file.write("Grand Total : $"+str(grand_total))
              file.write("\n")
              file.write("\t\tThank You For Purchasing!! Feel Free to Come Again!! Have a Good Day!")
              
         else:
              file.write("\n")
              file.write("Grand Total: $"+str(grand_total))
              file.write("\n")
              file.write("\t\tThank You For Purchasing!! Feel Free to Come Again!! Have a Good Day!")
              

             
         print("\n")

       
Creating_List_For_Multiple_Laptops=[]

def Writing_Updated_Value_For_Purchasee(given_id, wanted_amount_of_laptop):
    """This function is used to update out main text file which is laptop.txt and here also we created list so that all the items get
    added when one user purchase multiple laptops"""
    

    
    Available_Laptops = read.Reading_File()

    # Update the quantity of the specific laptop
    Available_Laptops[given_id][3] = int(Available_Laptops[given_id][3]) + int(wanted_amount_of_laptop)

    

    # Write the updated laptop details to the file
    with open("laptop.txt","w") as file:
            for values in Available_Laptops.values():
                file.write(str(values[0]+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
                file.write("\n")

    Laptopname_of_product = Available_Laptops[given_id][0]
    LaptopBrand = Available_Laptops[given_id][1]
    Laptopquantity = wanted_amount_of_laptop
    Laptopprice = Available_Laptops[given_id][2].replace("$","")
    total = wanted_amount_of_laptop * float(Laptopprice)



    
    Creating_List_For_Multiple_Laptops.append([Laptopname_of_product,LaptopBrand, Laptopquantity, Laptopprice,total])

   


    

def Bill_Printing_For_Purchasee(given_id,wanted_amount_of_laptop):
        #This function is used to generate the bill in both shell and txt file after selling and id and quantity are passed as parameter to get value
        
        Available_Laptops = read.Reading_File()
        today_date_and_time = datetime.now()
       
        Invoice_Generate()

        while True:
            try:

                Mname = input("Please enter the name of company")
                if not all(c.isalpha() or c.isspace() for c in Mname):
                    raise ValueError #(raise and ValueError are inbuilt function raise is used to raise an exception and valueerror to check datatype
                break #loop ends
            except ValueError:
                        operations.for_alpha()
        

        while True: 
                try: # This is to check is the name is in alphabet or not
                        name = input("Please enter the name of the customer: ")
                        if not all(c.isalpha() or c.isspace() for c in name):
                                raise ValueError #(raise and ValueError are inbuilt function raise is used to raise an exception and valueerror to check datatype
                        break #loop ends
                except ValueError:
                        operations.for_alpha()
                        

        while True:
                try: #This is to check if the user have given integer value for phone or not
                        phone_number = int(input("Please enter the phone number of the customer: "))
                        break#loop ends
                
                except:
                        operations.Exception_Hanndling()
               

        while True:
                try: # This is to check is the address is in alphabet or not
                        address = input("Please enter your address: ")
                        if not all(c.isalpha() or c.isspace() for c in address):
                                raise ValueError 
                        break #loop ends
                except ValueError:
                        operations.for_alpha()

                        
        net_amount = 0

        
            
                
        

        Laptop_Shop()
        

        print("Company Name :"+str(Mname))
        print("Name of the Customer:"+str(name))
        print("Contact number:"+str(phone_number))
        print("Adress:"+str(address))
        print("Date and time of purcahse: "+str(today_date_and_time))
       
       
        print("\n")
        print("Purchase Details are:")

        Bill_Laptop_Specs()


        
        for i in Creating_List_For_Multiple_Laptops:
            net_amount += int(i[4])
            vat=(13/100)*net_amount
            gross_amount = net_amount + vat
            today_date_and_time = datetime.now()
        
            print("|",str(i[0])," "*(14-len(str(i[0]))),
                   " ",str(i[1])," "*(13-len(str(i[1]))),
                   " ",str(i[2])," "*(9-len(str(i[2]))),
                   " ",str(i[3])," "*(9-len(str(i[3]))),
                   " ",str(i[4])," "*(9-len(str(i[4]))))
        print("\t\t\t\t\t\t\t Total : $"+str(net_amount))
        print("Your Vat is :", vat)
        print("Grand Total : $"+str(gross_amount))
        print("\n")
        Thanks()
              



        with open(str(name) + ".txt","w") as file:
         
         vat=(13/100)*net_amount
         gross_amount = net_amount + vat
         today_date_and_time = datetime.now()

                     
         file.write("\t \t \t \t Nakarmi Shop Bill")
         file.write("\n")
         
         file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255")
         file.write("\n")
         
       
         file.write("Laptop details are:")
         file.write("\n")
         file.write("\n")

         file.write("Name of the Company :"+str(Mname))
         file.write("\n")
       
         file.write("Name of the Customer :"+str(name))
         file.write("\n")
        
         file.write("Contact number :"+str(phone_number))
         file.write("\n")
        
         file.write("Address :"+str(address))
         file.write("\n")
         
         file.write("Date and time of sold Laptops : "+str(today_date_and_time)+"\n")
         file.write("\n")
       
       
         
         file.write("Purchase Details are:")

         file.write("\n")
         
         file.write("\n")
         file.write("|----------------------------------------------------------")
         file.write("\n")
         file.write("|Laptop Name     Brand      Qauntity     Price      Total")
         file.write("\n")
         file.write("|----------------------------------------------------------")
         file.write("\n")
         
         for i in Creating_List_For_Multiple_Laptops:
                    file.write("|"+str(i[0])+" "*(14-len(str(i[0])))+
                               " "+str(i[1])+" "*(14-len(str(i[1])))+
                               " "+str(i[2])+" "*(10-len(str(i[2])))+
                               " "+str(i[3])+" "*(10-len(str(i[3])))+
                               " "+str(i[4])+" "*(10-len(str(i[4])))+ "\n")
                    file.write("\n")
          
         file.write("\t\t\t\t\t\t\t Total : $"+str(net_amount))
         file.write("\n")
         file.write("Your Vat is:" +str(vat))
         file.write("\n")
         file.write("Grand Total: $"+str(gross_amount))
         file.write("\n")          
         file.write("\t\tThank You For Purchasing!! Feel Free to Come Again!! Have a Good Day!")

            

      
       
                

   
