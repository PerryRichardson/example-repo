# ==========================================
# Name: Perry Richardson
# Resubmission date: April 20, 2025
# Note: This code was based off the inventory.py code 
#       that was provided in the code files for the task. 
#       Now includes ammendments from reviewer feedback.
# ==========================================

# 1. Program Information
# Shoe Inventory Management System
#
# Purpose:
# This program helps manage a shoe store's inventory.
# It reads data from a file, lets users view, add, update,
# and search for shoes using object-oriented programming.
#
# Functionalities:
# - Read shoe data from inventory.txt
# - Add new shoes
# - View all inventory
# - Restock shoes with low quantity
# - Search for a shoe by code
# - Calculate total value per item (cost * quantity)
# - Identify the shoe with the highest quantity for sale
# ==========================================

# 2. Shoe Class Definition
class Shoe:
    """
    A class to represent a shoe in inventory.

    Attributes:
        country (str): The country where the shoe is stored.
        code (str): A unique code identifying the shoe.
        product (str): The name or type of shoe.
        cost (float): The price per shoe.
        quantity (int): Number of shoes available in inventory.

    This class aligns with the data structure found in the 'inventory.txt' file:
    Country,Code,Product,Cost,Quantity
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Initializes a new Shoe instance with the given attributes.
        Converts cost to float and quantity to int for calculations.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """
        Returns the cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoe in stock.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a nicely formatted string representation of the shoe.
        Useful for printing shoe details.
        """
        return (f"\n----------------------------------------\n"
                f"Product:        {self.product}\n"
                f"Code:           {self.code}\n"
                f"Country:        {self.country}\n"
                f"Cost:           R{self.cost:.2f}\n"
                f"Quantity:       {self.quantity}\n"
                f"----------------------------------------")


# 3. List to Store Shoe Objects
shoes_list = []


# 4. Read Shoe Data from File
def read_shoes_data():
    """
    Reads data from 'inventory.txt', skipping the header line.
    For each valid line, it creates a Shoe object and appends it to shoes_list.
    Handles missing file errors using try-except.
    """
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 5:
                        country, code, product, cost, quantity = parts
                        shoe = Shoe(country, code, product, cost, quantity)
                        shoes_list.append(shoe)
        print("Inventory loaded successfully.")  # <- Confirmation message
    except FileNotFoundError:
        print("Error: 'inventory.txt' not found.")


# 5. Capture New Shoe Entry
def capture_shoes():
    """
    Prompts the user to input new shoe details.
    Validates input and ensures fields are not empty.
    Creates a Shoe object and adds it to shoes_list.
    Appends the new shoe data to 'inventory.txt'.
    """
    try:
        # Step 1: Get and validate the country
        country = input("Enter the country: ").strip()
        if not country:
            print("Country cannot be empty.")
            return

        # Step 2: Get and validate the shoe code
        code = input("Enter the shoe code: ").strip()
        if not code:
            print("Shoe code cannot be empty.")
            return

        # Step 3: Get and validate the product name
        product = input("Enter the product name: ").strip()
        if not product:
            print("Product name cannot be empty.")
            return

        # Step 4: Get cost and quantity, validating input types
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))

        # Step 5: Create the shoe object and store it
        new_shoe = Shoe(country, code, product, cost, quantity)
        shoes_list.append(new_shoe)

        # Step 6: Append the new shoe to the inventory file
        with open("inventory.txt", "a") as file:
            file.write(f"{country},{code},{product},{cost},{quantity}")

        print("Shoe successfully added.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers for cost and quantity.")

# 6. Restock Lowest Quantity Shoe

def re_stock():
    """
    Finds the shoe with the lowest quantity.
    Asks the user if they want to restock it and updates the quantity.
    Reflects the update in the 'inventory.txt' file.
    """
    if not shoes_list:
        print("Inventory is empty. Load data first.")
        return

    lowest_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    print("Lowest stock item:")
    print(lowest_shoe)

    try:
        restock = input("Do you want to restock this shoe? (yes/no): ").strip().lower()
        if restock == "yes":
            additional_qty = int(input("Enter quantity to add: "))
            lowest_shoe.quantity += additional_qty
            print("Quantity updated.")

            # Step 6: Rewrite inventory file with updated quantity (Fix: preserve original header)
            header = "Country,Code,Product,Cost,Quantity"  # <- Fix: store and reuse header line
            with open("inventory.txt", "w") as file:
                file.write(header)  # <- Fix: use stored header instead of rewriting it manually
                for shoe in shoes_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
    except ValueError:
        print("Invalid input. Quantity must be a number.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers for cost and quantity.")
