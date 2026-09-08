inventory = {
    "laptop" : {"qty":10, "price":55000},
    "mouse" : {"qty":50, "price":500},
    "keyboard" : {"qty":30, "price":800},
    "monitor" : {"qty":15, "price":9000},
    "pendrive" : {"qty":100, "price":400}
}

def add_item(name, qty, price):
    if name in inventory:
        inventory[name]["qty"] = inventory[name]["qty"] + qty
    else:
        inventory[name] = {"qty":qty, "price":price}

def remove_item(name):
    if name in inventory:
        del inventory[name]
    else:
        print(name , "not found")

def sell_item(name, qty):
    if name in inventory and inventory[name]["qty"] >= qty:
        inventory[name]["qty"] -= qty
    else:
        print("not enough stock for" , name)

def total_value():
    total = 0
    for i in inventory:
        total = total + inventory[i]["qty"]*inventory[i]["price"]
    return total

def low_stock(threshold = 20):
    result = []
    for name,data in inventory.items():
        if data["qty"] < threshold:
            result.append(name)
    return result

item_names = list(inventory.keys())

item_ids = (101,102,103,104,105)   #tuple bcoz ids fixed

def copy_demo():
    ref_copy = inventory   #not a real copy, same memory
    shallow_copy = inventory.copy()

    ref_copy["mouse"]["qty"] = 999
    print("mouse qty in original after ref_copy edit:" , inventory["mouse"]["qty"])

    shallow_copy["keyboard"]["qty"] = 0
    print("keyboard qty in original after shallow_copy edit:" , inventory["keyboard"]["qty"])


print("Initial Inventory")
for i in inventory:
    print(i , "->" , inventory[i])

add_item("webcam", 25, 1500)
sell_item("laptop", 3)
remove_item("pendrive")

print()
print("After some operations")
for i in inventory:
    print(i , "->" , inventory[i])

print()
print("total value = " , total_value())
print("low stock items = " , low_stock())

print()
print("first 3 items" , item_names[0:3])
print("last 2 items" , item_names[-2:])
print("ids tuple" , item_ids)

print()
print("copy vs mutation demo")
copy_demo()
