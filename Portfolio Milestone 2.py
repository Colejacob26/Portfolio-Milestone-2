#From Part #1
class ItemToPurchase:
    #Default constructor with attribute names
    def __init__(self, item_name = "", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity 
    
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(format(self.item_price,".2f")), "=", "$"+ str(format((self.item_price *self.item_quantity),".2f")))
    #Set up printing statement


#Part #2
class ShoppingCart:
    #Default Contructors
    def __init__(self, customer_name ='none', current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
    cart_item = []




    #adding item + option for description
    def add_item(itp):
        cart.cart_item.append(itp)
        print("Add Description? Enter: Yes or No")
        input1 = str(input())
        if input1 == "Yes":
            print("Enter Description:")
            dict1[itp.item_name] = str(input())
        elif input1 == "No":
            dict1[itp.item_name] = ""
        else:
            "Invalid"

    #removes item
    def remove_item(ItemName):
        for j in range(len(cart.cart_item)-1):
            if ItemName == cart.cart_item[j].item_name:
                #Remove description and item
                del dict1[cart.cart_item[j].item_name]
                del cart.cart_item[j]
                

    #to modify description, price, quantity, does not work with default items
    def modify_item(itp):
        count2 = 0
        for j in range(len(cart.cart_item)):
            if ipt.item_name == cart.cart_item[j].item_name:
                count2 += 1
                if dict1[itp.item_name] == "" and itp.item_price == 0 and item_quantity == 0:
                    print("Default Item")
                else:
                    print("Enter new description:")
                    dict1[itp.item_name] = str(input())
                    print("Enter new price:")
                    price2 = float(input())
                    print("Enter new quantity:")
                    quantity2 = int(input())
                    ItemToPurchase(itp.item_name, price2, quantity2)
            
        if count2 == 0:
            print("Item not found in cart")
    #To display no item in cart            


    #Total amount of items in cart
    def get_num_items_in_cart():
        total = 0
        for i in range(len(cart.cart_item)):
             total += cart.cart_item[i].item_quantity
        return total
        

    #Grand Total
    def get_cost_of_cart():
        total = 0
        for i in range(len(cart.cart_item)):
             total += cart.cart_item[i].item_price * cart.cart_item[i].item_quantity
        return total

    #prints all information besides description
    def print_total():
        #Check if shopping cart is empty
        if len(cart.cart_item) == 0:
            print("SHOPPING CART IS EMPTY")
            
        else:
            print(str(cart.customer_name) + "'s Shopping Cart", "-", cart.current_date)
            num = ShoppingCart.get_num_items_in_cart()
            print("Number of Items:", num)
            for i in range(len(cart.cart_item)):
                print(cart.cart_item[i].item_name, cart.cart_item[i].item_quantity, "@", "$" + str(format(cart.cart_item[i].item_price,".2f")), "=", "$" + str(format(cart.cart_item[i].item_price * cart.cart_item[i].item_quantity,".2f")))
                test = ShoppingCart.get_cost_of_cart()
            print("Total:", "$" + str(format(test,".2f")))
            

    #prints description
    def print_descriptions():
        print(str(cart.customer_name) + "'s Shopping Cart" , "-", cart.current_date)
        for i in range(len(cart.cart_item)):
            print(str(cart.cart_item[i].item_name) + ":", dict1[cart.cart_item[i].item_name])

#Menu
def print_menu(SC):
    print("MENU")
    print("Choose an option:")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
    option = input()




#Option A
    if option == "a":
        print("Enter the item name:")
        name1 = input()

        print("Enter the item price:")
        price1= float(input())

        print("Enter the item quantity:")
        quantity1= int(input())
        
        item1 = ItemToPurchase(name1, price1, quantity1)
        ShoppingCart.add_item(item1)

#Option r            
    elif option == "r":
        print ("What item are you deleting?")
        remove = str(input())
        count = 0
        
        for i in range(len(cart.cart_item)-1):
            if cart.cart_item[i].item_name == remove:
                count += 1
                ShoppingCart.remove_item(remove)

        if count == 0:
            print("Item not found in cart")


#Option c
    elif option =="c":
        print("Enter the item name:")
        count3 = 0
        name1 = input()
        for i in range(len(cart.cart_item)):
            if name1 == cart.cart_item[i].item_name:
                count3 +=1
                
                price2 = cart.cart_item[i].item_price
                
                print("Enter new item quantity:")
                
                quantity3= int(input())

                cart.cart_item[i] = ItemToPurchase(name1,price2,quantity3)
                    
        if count3 == 0:
            print("Item not found in cart")     
            

#Option i      
    elif option == "i":
        ShoppingCart.print_descriptions()

        
#option o
    elif option == "o":
        ShoppingCart.print_total()

            
#option q   
    elif option == "q":
        global quitCart
        quitCart = True


#Start of Main


#Collects Name and Date
print("Please enter your name:")
name = input()
print ("Please enter the date: (Example: January 1, 2020)")
date = input()

#Creates Shopping cart for the person who starts the code
cart = ShoppingCart(name,date)
dict1 = {} 

#Switch for the menu quitting 
quitCart = False
while quitCart == False:
    print_menu(cart)
