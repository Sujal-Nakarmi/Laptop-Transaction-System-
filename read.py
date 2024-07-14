def Reading_File():
   """ This function creates a dictionary and
      sets the laptop id to 1 and reads the data from file laptop.txt and for loop is used to iterate over each line from the file
      and Update the dictionary with key,value pair where key is laptop id and laptop specs are value which is split by “,”
      which at last returns laptop dictionary"""

   
   Available_Laptops = {}
   laptop_id = 1
   with open("laptop.txt","r") as file:
       for line in file:
           line  = line.replace("\n","")
           Available_Laptops.update({laptop_id: line.split(",")})  #(Puts IN the form of List)
           laptop_id += 1
           
   return Available_Laptops

def Laptop_Display():
   """ This function is used design the data that we get from reading the file laptop.txt in a tabular form by assuming the space we need and
         subtracting it with the len of the word which is defined by items index """


   
   with open("laptop.txt","r") as file:
    myList = file.readlines()
    nestedList = [[x] for x in myList]
    newList = []
    for i in range(len(nestedList)):
        newList.append(nestedList[i][0].split(","))
    

   
    a = 1
    for item in newList:
        print("|",a," |",item[0]," "*(14-len(item[0])),"|",item[1]," "*(13-len(item[1])),"|",item[2]," "*(6-len(item[2])),"| ",item[3]," "*(6-len(item[3])),"|",item[4]," ","|",item[5].strip()," |")
        a += 1
