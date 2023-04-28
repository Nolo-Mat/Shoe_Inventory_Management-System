# Shoe_Inventory_Management-System
This is a Shoe Inventory Management System built with Python. This program helps to manage and keep track of shoes in an inventory. It can perform the following functions:

   * Read shoes data from a file
   * Add shoes to the inventory
   * View all the shoes in the inventory
   * Restock shoes
   * Search for a shoe from the inventory

## Installation

To use this program, follow the instructions below:

   * Install Python 3 or later.
   * Download the inventory.py file to your local machine.
   * Open the terminal and navigate to the directory where you saved the inventory.py file.
   * Run the command python3 inventory.py to start the program.

## Usage

The program will present a menu of options to choose from:

   * Press 1 to add shoes to the inventory
   * Press 2 to view all the shoes in the inventory
   * Press 3 to restock shoes
   * Press 4 to search for a shoe from the inventory
   * Press 5 to exit the program

### Adding Shoes to the Inventory

To add shoes to the inventory, select option 1 from the main menu. Then, enter the following information:

   * The name of the country that the product is currently in
   * The identification code (e.g. SKU76055) for the product
   * The name of the product (e.g. Jordan 1)
   * The cost of the product
   * The quantity/amount of product currently in stock

### Viewing All the Shoes in the Inventory

To view all the shoes in the inventory, select option 2 from the main menu. The program will display the details of all the shoes in the inventory.

### Restocking Shoes

To restock shoes, select option 3 from the main menu. The program will find the shoe object with the lowest quantity, which is the shoes that need to be restocked. Then, the program will ask the user if they want to add this quantity of shoes and then update it on the file.

### Searching for a Shoe from the Inventory

To search for a shoe from the inventory, select option 4 from the main menu. Then, enter the identification code (e.g. SKU76055) for the shoe that you want to search for. The program will search for the shoe in the inventory and return the details of the shoe.

### Exiting the Program

To exit the program, select option 5 from the main menu. The program will exit.
