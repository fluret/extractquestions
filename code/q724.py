class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
 
class PhoneStore:
    def __init__(self):
        self.inventory = []
 
    def add_phone(self, phone):
        self.inventory.append(phone)
 
    def remove_phone(self, brand, model):
        for phone in self.inventory:
            if phone.brand == brand and phone.model == model:
                self.inventory.remove(phone)
                print(f"Removed {brand} {model} from inventory.")
                return
        print(f"{brand} {model} not found in inventory.")
 
    def find_phone(self, brand, model):
        for phone in self.inventory:
            if phone.brand == brand and phone.model == model:
                return phone
        return None
 
    def display_inventory(self):
        print("Phone Store Inventory :")
        for phone in self.inventory:
            print(f"Brand : {phone.brand}, Model : {phone.model}, Price : ${phone.price:.2f}")
 
 
phone_store = PhoneStore()
 
print("1. Add Phone to Inventory")
print("2. Remove Phone from Inventory")
print("3. Find Phone in Inventory")
print("4. Display Inventory")
print("5. Quit")
 
while True:
    choice = input("\nEnter your Choice : ")
 
    if choice == "1":
        brand = input("Enter Phone Brand : ")
        model = input("Enter Phone Model : ")
        price = float(input("Enter Phone Price : "))
        phone = Phone(brand.capitalize(), model.capitalize(), price)
        phone_store.add_phone(phone)
        print(f"Added {brand} {model} to inventory.")
    elif choice == "2":
        brand = input("Enter Phone Brand to Remove : ")
        model = input("Enter Phone Model to Remove : ")
        phone_store.remove_phone(brand.capitalize(), model.capitalize())
    elif choice == "3":
        brand = input("Enter Phone Brand to Find : ")
        model = input("Enter Phone Model to Find : ")
        found_phone = phone_store.find_phone(brand.capitalize(), model.capitalize())
        if found_phone:
            print(f"Found {brand} {model} in inventory. Price : ${found_phone.price:.2f}")
        else:
            print(f"{brand} {model} not found in inventory.")
    elif choice == "4":
        phone_store.display_inventory()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")