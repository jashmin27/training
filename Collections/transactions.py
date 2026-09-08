transactions = [
    ("T1","Ravi",1200,"grocery"),
    ("T2","Meena",3000,"electronics"),
    ("T3","Ravi",500,"grocery"),
    ("T4","Suresh",7000,"electronics"),
    ("T5","Meena",1500,"clothing"),
    ("T6","Ravi",2200,"clothing"),
    ("T7","Suresh",450,"grocery"),
    ("T8","Anjali",9000,"electronics"),
]

def total_by_category():
    totals = {}
    for txn in transactions:
        cat = txn[3]
        amt = txn[2]
        if cat in totals:
            totals[cat] += amt
        else:
            totals[cat] = amt
    return totals

def total_by_customer():
    totals = {}
    for t in transactions:
        cust = t[1]
        amt = t[2]
        if cust in totals:
            totals[cust] += amt
        else:
            totals[cust] = amt
    return totals

def unique_customers():
    s = set()
    for t in transactions:
        s.add(t[1])
    return s

def unique_categories():
    s = set()
    for t in transactions:
        s.add(t[3])
    return s

def high_value_txns(limit = 2000):
    res = []
    for t in transactions:
        if t[2] > limit:
            res.append(t)
    return res

def txns_of(customer):
    res = []
    for t in transactions:
        if t[1] == customer:
            res.append(t)
    return res

def sorted_by_amount():
    return sorted(transactions, key = lambda t: t[2], reverse = True)


print("total by category ->" , total_by_category())
print()
print("total by customer ->" , total_by_customer())
print()
print("unique customers ->" , unique_customers())
print("unique categories ->" , unique_categories())

print()
print("high value txns (>2000)")
for t in high_value_txns():
    print(t)

print()
print("ravi's txns ->" , txns_of("Ravi"))

print()
print("top 3 txns by amount")
top3 = sorted_by_amount()[0:3]
for t in top3:
    print(t)

txn_copy = transactions.copy()   #shallow copy but tuples are immutable so this is safe
txn_copy.append(("T9","New",100,"grocery"))
print()
print("original len after appending in copy ->" , len(transactions))
print("copy len ->" , len(txn_copy))
