class Item:
    """item from sari sari store inventory"""
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def update_quantity(self, new_quantity):
        """Updates the quantity"""
        self.quantity = new_quantity
        print(f" Updated {self.name} quantity to {new_quantity}")
    
    def get_total_price(self):
        """Calculate total price for this item based on quantity and price"""
        return self.quantity * self.price
    
    def __str__(self):
        """String representation of the item"""
        return f"{self.name} - Qty: {self.quantity} @ ₱{self.price:.2f} each = ₱{self.get_total_price():.2f}"


class SariSariStore:
    """Manages the inventory of a sari-sari store"""
    
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = []
    
    def add_item(self, name, quantity, price):
        """Add a new item to the inventory"""
        # Check if item already exists
        for item in self.inventory:
            if item.name.lower() == name.lower():
                print(f"⚠ {name} already exists. Use update_quantity() instead.")
                return
        
        new_item = Item(name, quantity, price)
        self.inventory.append(new_item)
        print(f"✓ Added {name} to inventory")
    
    def update_quantity(self, name, new_quantity):
        """Update the quantity of an existing item"""
        for item in self.inventory:
            if item.name.lower() == name.lower():
                item.update_quantity(new_quantity)
                return
        print(f"✗ Item '{name}' not found in inventory")
    
    def display_items(self):
        """Display all items in the inventory"""
        if not self.inventory:
            print("No items in inventory.")
            return
        
        print(f"\n{'='*60}")
        print(f"{self.store_name.upper()} - INVENTORY")
        print(f"{'='*60}")
        print(f"{'Item Name':<25} {'Qty':<8} {'Price':<12} {'Total':<12}")
        print(f"{'-'*60}")
        
        for item in self.inventory:
            print(f"{item.name:<25} {item.quantity:<8} ₱{item.price:<10.2f} ₱{item.get_total_price():<10.2f}")
        
        print(f"{'='*60}\n")
    
    def calculate_total_inventory_value(self):
        """Calculate the total value of all items in inventory"""
        total = sum(item.get_total_price() for item in self.inventory)
        return total
    
    def show_summary(self):
        """Display inventory summary with total value"""
        self.display_items()
        total_value = self.calculate_total_inventory_value()
        print(f"TOTAL INVENTORY VALUE: ₱{total_value:.2f}")
        print(f"{'='*60}\n")


# Main program
def main():
    # Create a sari-sari store
    store = SariSariStore("Aling Maria's Sari-Sari Store")
    
    print("=" * 60)
    print(f"Welcome to {store.store_name}!")
    print("=" * 60)
    
    # Add common sari-sari store items
    print("\n📦 Adding items to inventory...\n")
    store.add_item("Lucky Me Instant Pancit Canton", 50, 15.00)
    store.add_item("C2 Green Tea", 30, 20.00)
    store.add_item("Sky Flakes Crackers", 25, 8.50)
    store.add_item("Argentina Corned Beef", 15, 35.00)
    store.add_item("Bear Brand Milk", 40, 18.00)
    store.add_item("Egg (per piece)", 60, 7.00)
    store.add_item("Alaska Condensada", 20, 45.00)
    store.add_item("Chippy", 35, 10.00)
    store.add_item("Magic Sarap 8g", 100, 3.00)
    store.add_item("Tide Detergent Powder 35g", 45, 12.00)
    
    # Display all items
    print("\n📋 Current Inventory:")
    store.show_summary()
    
    # Update quantities after sales
    print("🔄 Updating quantities after sales...\n")
    store.update_quantity("Lucky Me Instant Pancit Canton", 35)
    store.update_quantity("C2 Green Tea", 22)
    store.update_quantity("Egg (per piece)", 48)
    
    # Display updated inventory
    print("\n📋 Updated Inventory:")
    store.show_summary()
    
    # Try to add duplicate item
    print("🔄 Attempting to add duplicate item...\n")
    store.add_item("Chippy", 10, 10.00)
    
    # Try to update non-existent item
    print("\n🔄 Attempting to update non-existent item...\n")
    store.update_quantity("Coca-Cola", 50)


if __name__ == "__main__":
    main()