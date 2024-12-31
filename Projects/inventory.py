inventory = {
    "cpu": 20,
    "gpu": 20,
    "ram": 40,
    "display": 20
}

def add_or_update_item(item, quantity):
    try:
        inventory[item] = inventory.get(item, 0) + quantity
        if inventory[item] < 0:
            raise ValueError("PLEASE CHECK THE QUANTITY OF THE ITEM")
        display_inventory()
    except ValueError as e:
        print(f"Value Error: {e}")

def remove_item(item):
    try:
        if item not in inventory:
            raise KeyError("Item not found, check the list")
        inventory.pop(item)
        print(f"Item {item} was succesfully removed")
        display_inventory()
    # return f"Item{item} succesfully removed."
    except KeyError as e:
        print(f"Error: {e}")
        display_inventory()


def display_inventory():
    try:
        if not inventory:
            raise RuntimeError("Empty inventory")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    except RuntimeError as e:
        print(f"Error: {e}")

# display_inventory()

# add_or_update_item("cpu", 68)

# add_or_update_item("gpu", 93)

remove_item("gpu")
# display_inventory()
