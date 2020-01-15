import datetime
print("MINI PROJECT :ONLINE RETAIL SHOPPING ")
print("------------------------------------")
stock = {}
k='y'
while(1 and k!='n'):
 print("MENU")
 print("WELCOME TO ADMIN MODULE")
 print("Press 1 to Add product in stock")
 print("Press 2 to Update the price of product in stock")
 print("Press 3 to Remove product from stock")
 print("Press 4 to View all products in stock")
 print("Press 5 to Logout Admin")
 a=int(input("Enter your choice : "))


 if(a==1):
    productname=input("enter product name")
    unitprice=int(input("Enter your unit price : "))
    stock[productname] = unitprice
    print("Do you want to enter more")
    a=int(input("Enter any number to continue"))

 elif(a==2):
    productname= input("enter product name whose price is to be updated")
    unitprice = int(input("Enter new unit price : "))
    stock[productname]=unitprice
    print("Do you want to enter more")
    a = int(input("Enter any number to continue"))
 elif(a==3):
    productname = input("enter product name to be deleted")
    del stock[productname]
    print("Do you want to enter more")
    a = int(input("Enter any number to continue"))
 elif(a==4):
    print(stock.items())
    print("Do you want to enter more")
    a = int(input("Enter any number to continue"))
 elif(a==5):
    print("Admin has logout successfully ")
    print("Welcome to consumer module")
    basket={}
    while(1):
     print("MENU")
     print("Press 1 to view all the products in the stock")
     print("Press 2 to add products in the basket")
     print("Press 3 to view all products  in the basket")
     print("Press 4 to search products in the stock")
     print("Press 5 to remove product from basket")
     print("Press 6 to print invoice")
     print("Press 7 to signout")
     a = int(input("Enter your choice : "))
     if(a==1):
         print(stock.items())
         print("Do you want to enter more")
         a = int(input("Enter any number to continue"))
     elif(a==2):
         productname=input("enter the product to be added in basket")
         quantity=int(input("enter the quantity"))
         basket[productname]=quantity

         print("Do you want to enter more")
         a = int(input("Enter any number to continue"))
     elif(a==3):
         print(basket.items())
         print("Do you want to enter more")
         a = int(input("Enter any number to continue"))
     elif(a==4):
         b=input("enter the product to be searched")
         print(stock.get(b,"Not Found"))
         print("Do you want to enter more")
         a = int(input("Enter any number to continue"))
     elif(a==5):
          c=input("enter the product name to be deleted")
          z=basket.get(c)
          del [z]
          print("Do you want to enter more")
          a = int(input("Enter any number to continue"))

     elif(a==6):

           print("Billing invoice")
           print("---------------")
           now =datetime.datetime.now()
           print("billing date:",now.day,"-",now.month,"-",now.year)
           print("Product name   Unit Price   Quantity   Total")
           t=0
           for j,m in sorted(list(basket.items())):
               for o, p in stock.items():
                  if(j==o):
                   #from operator import itemgetter
                   print(j,"          ",p,"            ",m,"      ",(m*p))
                   t=t+(m*p)

           print("----------------------------\nGrand Total :",t,"Thank you for shopping with us\n visit again")

     if(a==7):
          k=input("Do you wish to shop again? \n Enter y or n : ")
          if(k=='y'):
               basket={}

          else:
              print("Software shutting down")
              print("Developed by:Shaily Goyal,Lakshmi Srivastava,Aunkita Mandal,Anushka Singh Bhardwaj")
              break
              break












