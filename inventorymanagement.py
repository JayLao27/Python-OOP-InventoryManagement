class Item:
    """Represents an item in the sari-sari store"""
    
    def __init__(self, name, quantity, price):
        """
        Initialize an Item object
        
        Parameters:
        - name (str): Name of the item
        - quantity (int): Quantity in stock
        - price (float): Price per unit
        """
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def get_total_price(self):
        """Calculate total price for this item (quantity × price)"""
        return self.quantity * self.price
    
    def __str__(self):
        """Return formatted string representation of the item"""
        return (f"{self.name:<30} | Qty: {self.quantity:<5} | "
                f"Price: ₱{self.price:>7.2f} | Total: ₱{self.get_total_price():>8.2f}")


class InventoryManagement:
    """Manages inventory for a sari-sari store"""
    
    def __init__(self):
        """Initialize empty inventory list"""
        self.items = []
    
    def add_item(self, name, quantity, price):
        """
        Add a new item to inventory
        
        Parameters:
        - name (str): Name of the item
        - quantity (int): Quantity to add
        - price (float): Price per unit
        """
        # Check if item already exists
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"\n'{name}' already exists! Use update_quantity() to modify it.")
                return
        
        # Create new item and add to inventory
        new_item = Item(name, quantity, price)
        self.items.append(new_item)
        print(f"\nSuccessfully added: {name} (Qty: {quantity}, Price: ₱{price:.2f})")
    
    def update_quantity(self, name, new_quantity):
        """
        Update the quantity of an existing item
        
        Parameters:
        - name (str): Name of the item to update
        - new_quantity (int): New quantity value
        """
        for item in self.items:
            if item.name.lower() == name.lower():
                old_quantity = item.quantity
                item.quantity = new_quantity
                print(f"\nUpdated '{name}' quantity: {old_quantity} → {new_quantity}")
                return
        
        print(f"\nItem '{name}' not found in inventory!")
    
    def display_items(self):
        """Display all items in inventory with their details"""
        if not self.items:
            print("\nInventory is empty.")
            return
        
        print("\n" + "="*80)
        print("SARI-SARI STORE INVENTORY")
        print("="*80)
        print(f"{'ITEM NAME':<30} | {'QUANTITY':<10} | {'PRICE':<14} | {'TOTAL PRICE':<12}")
        print("-"*80)
        
        for item in self.items:
            print(item)
        
        print("="*80)
    
    def calculate_total_inventory_value(self):
        """
        Calculate total value of all items in inventory
        
        Returns:
        - float: Total inventory value
        """
        total = sum(item.get_total_price() for item in self.items)
        return total


# ========================= MAIN PROGRAM =========================

def print_menu():
    """Display main menu options"""
    print("\n" + "="*50)
    print("SARI-SARI STORE INVENTORY SYSTEM")
    print("="*50)
    print("1. Add New Item")
    print("2. Update Item Quantity")
    print("3. Display All Items")
    print("4. Show Total Inventory Value")
    print("5. Exit")
    print("="*50)


def main():
    """Main program function"""
    inventory = InventoryManagement()
    
    print("\n" + "*"*25)
    print("WELCOME TO ALING ROSA'S SARI-SARI STORE")
    print("*"*25)
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Add new item
            print("\n--- ADD NEW ITEM ---")
            name = input("Enter the name of the item: ").strip()
            try:
                quantity = int(input("How many: "))
                price = float(input("Enter price (₱): "))
                inventory.add_item(name, quantity, price)
            except ValueError:
                print("\nInvalid input! Quantity must be an integer and price must be a number.")
        
        elif choice == '2':
            # Update quantity
            print("\n--- UPDATE ITEM QUANTITY ---")
            name = input("Enter item name: ").strip()
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(name, new_quantity)
            except ValueError:
                print("\nInvalid input! Quantity must be an integer.")
        
        elif choice == '3':
            # Display all items
            inventory.display_items()
        
        elif choice == '4':
            # Show total inventory value
            total_value = inventory.calculate_total_inventory_value()
            print("\n" + "="*50)
            print(f"TOTAL INVENTORY VALUE: ₱{total_value:,.2f}")
            print("="*50)
        
        elif choice == '5':
            # Exit program
            print("\nThank you for using the Inventory System.")
            print("Salamat po. Balik kayo ha.\n")
            break
        
        else:
            print("\nInvalid choice! Please enter 1-5.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


# Demo function (optional - comment out if not needed)
def demo():
    """Demonstration of the inventory system with sample data"""
    print("\n" + "*"*25)
    print("DEMO MODE - Sample Sari-Sari Store Inventory")
    print("*"*25)
    
    inventory = InventoryManagement()
    
    # Add sample items
    print("\nAdding sample items...")
    inventory.add_item("Lucky Me Pancit Canton", 50, 15.00)
    inventory.add_item("C2 Green Tea", 30, 20.00)
    inventory.add_item("Sky Flakes", 25, 8.50)
    inventory.add_item("Egg (per piece)", 60, 7.00)
    inventory.add_item("Bear Brand Milk", 40, 18.00)
    inventory.add_item("Magic Sarap 8g", 100, 3.00)
    
    # Display inventory
    inventory.display_items()
    
    # Update quantities
    print("\nSimulating sales - updating quantities...")
    inventory.update_quantity("Lucky Me Pancit Canton", 35)
    inventory.update_quantity("Egg (per piece)", 45)
    
    # Display updated inventory
    inventory.display_items()
    
    # Show total value
    total = inventory.calculate_total_inventory_value()
    print("\n" + "="*50)
    print(f"TOTAL INVENTORY VALUE: ₱{total:,.2f}")
    print("="*50)


# Runs the program
if __name__ == "__main__":
    main()
