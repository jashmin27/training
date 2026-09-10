#utility library
#learning: params, return values, defaults, kwargs, args, scope, pure functions

#---------------- inventory functions ----------------

def add_item(inventory, name, qty, price):
    #pure function - takes inventory in, returns a new updated dict, doesnt touch original
    new_inv = inventory.copy()

    if name in new_inv:
        new_inv[name]["qty"] = new_inv[name]["qty"] + qty
    else:
        new_inv[name] = {"qty":qty, "price":price}

    return new_inv


def sell_item(inventory, name, qty):
    new_inv = inventory.copy()

    if name in new_inv and new_inv[name]["qty"] >= qty:
        new_inv[name]["qty"] -= qty
    else:
        print("not enough stock for", name)

    return new_inv


def total_value(inventory):
    total = 0
    for item in inventory.values():
        total = total + item["qty"]*item["price"]
    return total


def low_stock(inventory, threshold=20):
    #threshold has a default value here
    result = []
    for name,data in inventory.items():
        if data["qty"] < threshold:
            result.append(name)
    return result


#---------------- employee functions ----------------

def get_departments(employees):
    depts = set()
    for emp in employees:
        depts.add(emp["dept"])
    return depts


def employees_by_dept(employees, dept):
    names = []
    for emp in employees:
        if emp["dept"] == dept:
            names.append(emp["name"])
    return names


def highest_paid(employees):
    top = employees[0]
    for emp in employees:
        if emp["salary"] > top["salary"]:
            top = emp
    return top


def avg_salary(employees, dept=None):
    #if dept not given it will calculate avg for all employees
    total = 0
    count = 0

    for emp in employees:
        if dept is None or emp["dept"] == dept:
            total = total + emp["salary"]
            count = count + 1

    if count == 0:
        return 0

    return total/count


#---------------- transaction functions ----------------

def total_by(transactions, key_index):
    #key_index = 1 for customer, 3 for category
    totals = {}
    for t in transactions:
        key = t[key_index]
        amt = t[2]
        if key in totals:
            totals[key] += amt
        else:
            totals[key] = amt
    return totals


def high_value_txns(transactions, limit=2000):
    res = []
    for t in transactions:
        if t[2] > limit:
            res.append(t)
    return res


def txns_of(transactions, customer):
    res = []
    for t in transactions:
        if t[1] == customer:
            res.append(t)
    return res


#---------------- generic helper functions (args/kwargs demo) ----------------

def total_of(*numbers):
    #args -> can take any number of values
    total = 0
    for n in numbers:
        total = total + n
    return total


def make_record(**fields):
    #kwargs -> can take any number of named fields, returns a dict
    record = {}
    for key in fields:
        record[key] = fields[key]
    return record


def summarize(data, label="Summary", show_count=True):
    #mixing normal params with default params
    print(label, ":")
    for k,v in data.items():
        print(" ", k, "->", v)
    if show_count:
        print("total entries:", len(data))


#---------------- scope demo ----------------

counter = 0   #global variable

def increment_counter():
    global counter
    counter = counter + 1
    return counter


def local_scope_demo():
    x = 10   #local variable, only exists inside this function
    x = x + 5
    return x


#---------------- quick test/demo when running this file directly ----------------

if __name__ == "__main__":

    inventory = {
        "laptop":{"qty":10,"price":55000},
        "mouse":{"qty":5,"price":500}
    }

    inventory = add_item(inventory, "keyboard", 15, 800)
    inventory = sell_item(inventory, "laptop", 2)

    print("inventory total value ->", total_value(inventory))
    print("low stock items ->", low_stock(inventory, threshold=10))

    employees = [
        {"id":1,"name":"Rahul","dept":"IT","salary":45000},
        {"id":2,"name":"Sneha","dept":"HR","salary":38000},
        {"id":3,"name":"Amit","dept":"IT","salary":52000},
    ]

    print()
    print("departments ->", get_departments(employees))
    print("IT employees ->", employees_by_dept(employees, "IT"))
    print("highest paid ->", highest_paid(employees)["name"])
    print("avg salary all ->", avg_salary(employees))
    print("avg salary IT ->", avg_salary(employees, dept="IT"))

    transactions = [
        ("T1","Ravi",1200,"grocery"),
        ("T2","Meena",3000,"electronics"),
        ("T3","Ravi",500,"grocery"),
    ]

    print()
    print("total by customer ->", total_by(transactions, 1))
    print("total by category ->", total_by(transactions, 3))
    print("high value txns ->", high_value_txns(transactions, limit=1000))

    print()
    print("total_of args demo ->", total_of(10,20,30,40))

    rec = make_record(name="Ravi", age=22, course="btech")
    print("make_record kwargs demo ->", rec)

    print()
    summarize(inventory, label="Inventory", show_count=True)

    print()
    print("counter ->", increment_counter())
    print("counter ->", increment_counter())
    print("local scope result ->", local_scope_demo())
    print("counter is still global, x from local_scope_demo doesnt exist here")
