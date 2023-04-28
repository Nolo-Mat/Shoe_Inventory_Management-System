#========The beginning of the class==========
#
# The Shoe class is a blueprint for creating objects.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        The function __init__() is a special method that is called when an object is created from a
        class
        
        :param country: The country where the order was placed
        :param code: the product code
        :param product: The name of the product
        :param cost: The cost of the product in the country
        :param quantity: the number of items to be sold
        """
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        
    def get_cost(self):
        '''
        A block of code to return the cost of the shoe in this method.
        '''
        return {self.cost} 
        
        
    def get_quantity(self):
        '''
        A block of code to return the quantity of the shoes.
        '''
        return {self.quantity.strip("\n")} 
        

    def __str__(self):
        '''
        A block of code to return a string representation of a class.
        '''
        return f"""\n    Country:  {self.country}
    Code:     {self.code}
    Product:  {self.product}
    Cost:     R{self.cost}
    Quantity: {self.quantity}"""
        
        
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. I use a try-except in this function
    for error handling.
    '''
    if len(shoe_list) == 0:
        with open("inventory.txt", "r", encoding='utf-8') as inventory:
            try:
                for line in inventory:
                    info = line.split(",")
                    
                    if info[0] == "Country":
                        pass
                    else:
                        obj = Shoe(info[0], info[1], info[2], info[3], info[4])
                        shoe_list.append(obj)
                    
            except Exception():
                return "An error occured. Please try again later.  :/ " 
    else:
        pass
        
    
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    while True:
        try:
            country = input("Enter the name of the country that the product is currently in: ")
            code = input("Enter the identification code (e.g. SKU76055) for the product: ")
            product = input("Enter the name of the product (e.g. Jordan 1): ")
            cost = int(input("Enter the cost of the product: "))
            quantity = int(input("Enter the quantity/amount of product currently in stock: "))
            
            new_obj = Shoe(country, code, product, cost, quantity)
            shoe_list.append(new_obj)
            
            print("\nProduct info has been added to the inventory! ")
            
        except ValueError():
            print("\nInvalid entry. Please try again. ")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    read_shoes_data()
    for i, obj in enumerate(shoe_list):
        print(f"\n==Shoe number {i + 1}==")
        print(obj)
    
    
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Then ask the user if they
    want to add this quantity of shoes and then update it on the file
    '''
    read_shoes_data()
    min_val = int(shoe_list[0].quantity)
    counter = 0
    
    for i, obj in enumerate(shoe_list):
        if int(obj.quantity) <= min_val:
            min_val = int(obj.quantity)
            counter = i
            
    print(f"\n==Shoe number {counter + 1}==")
    print(shoe_list[counter])
            
    while True:
        choice = input(f"Would you like to add to the quantity of {shoe_list[counter].product}'s, Yes or No? \n:").lower()
        if choice == "yes":
            num = int(input("Enter the number you want to change the quantity too: "))
            
            if num > int(shoe_list[counter].quantity):
                shoe_list[counter].quantity = str(num) + "\n"
                
                with open("Inventory.txt", "w", encoding='utf-8') as inventory:
                    inventory.write("Country,Code,Product,Cost,Quantity\n")
                    
                    for obj in shoe_list:
                        inventory.write(f"{obj.country},{obj.code},{obj.product},{obj.cost},{obj.quantity}")
                 
        elif choice == "no":
            break
        else:
            print("\nInvalid Entry. Please enter either yes or no.\n")
    
    
def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    read_shoes_data()
    counter = 0
    shoe_code = input("\nEnter the shoe code for the product you seek: ")
    
    for i, obj in enumerate(shoe_list):
        if obj.code == shoe_code:
            counter = i
            print(shoe_list[counter])
        
    
def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    read_shoes_data()
    
    for i, obj in enumerate(shoe_list):
        value = int(obj.cost) * int(obj.quantity)
        print(f"\nThe total value of all the {obj.product}'s in stock is: R{value}")
    
    
def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    read_shoes_data()
    max_val = int(shoe_list[0].quantity)
    counter = 0
    
    for i, obj in enumerate(shoe_list):
        if int(obj.quantity) >= max_val:
            max_val = int(obj.quantity)
            counter = i
    
    print("===FOR SALE===")
    print(shoe_list[counter])
    

#==========Main Menu=============
'''
This is the main menu that executes each function above.
This menu is inside a while loop.
'''

while True:
    
    menu = input("""\n====Select one of the options below====
    rd  - read the shoe data from the inventory
    as  - add new shoe data to the inventory
    va  - view details about all the shoes
    rs  - re-stock the shoes with the lowest quantity
    ss  - search for a specific shoe using the code
    vi  - view the total value for each shoe
    hq  - view the shoe with the highest quantity
    ex  - Exit
    
->  : """)
    
    if menu == "rd":
        read_shoes_data()
        print("Shoe data has been read successfully!!")
        
    elif menu == "as":
        capture_shoes()

    elif menu == "va":
        view_all()
        
    elif menu == "rs":
        re_stock()
        
    elif menu == "ss":
        search_shoe()
        
    elif menu == "vi":
        value_per_item()
        
    elif menu == "hq":
        highest_qty()
    
    elif menu == "ex":
        print("\nGOODBYE!!")
        exit()
        
    else:
        print("\nInvalid Entry. Please enter one of the options provided")