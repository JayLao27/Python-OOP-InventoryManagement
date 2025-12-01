class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def get_total_price(self):
        return self.quantity * self.price
    
    def __str__(self):
        return (f"{self.name:<30} | Qty: {self.quantity:<5} | "
                f"Price: ₱{self.price:>7.2f} | Total: ₱{self.get_total_price():>8.2f}")


class InventoryManagement:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, quantity, price):
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"\n'{name}' already exists! Use update_quantity() instead.")
                return
        
        self.items.append(Item(name, quantity, price))
        print(f"\nAdded: {name} (Qty: {quantity}, Price: ₱{price:.2f})")
    
    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                old_q = item.quantity
                item.quantity = new_quantity
                print(f"\nUpdated '{name}' quantity: {old_q} → {new_quantity}")
                return
        
        print(f"\nItem '{name}' not found.")
    
    def display_items(self):
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
        return sum(item.get_total_price() for item in self.items)


def print_menu():
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
    inventory = InventoryManagement()
    
    print("\n" + "*"*25)
    print("WELCOME TO ALING ROSA'S SARI-SARI STORE")
    print("*"*25)
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n--- ADD NEW ITEM ---")
            name = input("Enter the name of the item: ").strip()
            try:
                quantity = int(input("How many: "))
                price = float(input("Enter price (₱): "))
                inventory.add_item(name, quantity, price)
            except ValueError:
                print("\nInvalid input.")
        
        elif choice == '2':
            print("\n--- UPDATE ITEM QUANTITY ---")
            name = input("Enter item name: ").strip()
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(name, new_quantity)
            except ValueError:
                print("\nInvalid input.")
        
        elif choice == '3':
            inventory.display_items()
        
        elif choice == '4':
            total_value = inventory.calculate_total_inventory_value()
            print("\n" + "="*50)
            print(f"TOTAL INVENTORY VALUE: ₱{total_value:,.2f}")
            print("="*50)
        
        elif choice == '5':
            print("\nThank you for using the Inventory System.")
            break
        
        else:
            print("\nInvalid choice.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
