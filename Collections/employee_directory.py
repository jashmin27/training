
employees = [
    {"id":1, "name":"Rahul", "dept":"IT", "salary":45000},
    {"id":2, "name":"Sneha", "dept":"HR", "salary":38000},
    {"id":3, "name":"Amit", "dept":"IT", "salary":52000},
    {"id":4, "name":"Priya", "dept":"Finance", "salary":60000},
    {"id":5, "name":"Karan", "dept":"IT", "salary":41000},
    {"id":6, "name":"Divya", "dept":"HR", "salary":39500},
]

def get_departments():
    depts = set()
    for emp in employees:
        depts.add(emp["dept"])
    return depts

def employees_by_dept(dept):
    names = []
    for emp in employees:
        if emp["dept"] == dept:
            names.append(emp["name"])
    return names

def group_by_dept():
    grouped = {}
    for emp in employees:
        d = emp["dept"]
        if d not in grouped:
            grouped[d] = []
        grouped[d].append(emp["name"])
    return grouped

def highest_paid():
    top = employees[0]
    for emp in employees:
        if emp["salary"] > top["salary"]:
            top = emp
    return top

def sort_by_salary():
    return sorted(employees, key = lambda e: e["salary"], reverse = True)

def avg_salary_by_dept():
    totals = {}
    counts = {}
    for emp in employees:
        d = emp["dept"]
        totals[d] = totals.get(d,0) + emp["salary"]
        counts[d] = counts.get(d,0) + 1

    avg = {}
    for d in totals:
        avg[d] = totals[d]/counts[d]
    return avg

contact_record = (1,"Rahul","rahul@company.com")   #tuple since this record shouldnt change


print("all depts ->" , get_departments())

print()
print("IT dept employees ->" , employees_by_dept("IT"))

print()
print("grouped by dept")
grouped = group_by_dept()
for d in grouped:
    print(d,":",grouped[d])

top_emp = highest_paid()
print()
print("highest paid ->" , top_emp["name"] , top_emp["salary"])

print()
print("sorted by salary desc")
for e in sort_by_salary():
    print(e["name"] , e["salary"])

print()
print("avg salary per dept ->" , avg_salary_by_dept())

print()
print("first 3 employees")
for e in employees[0:3]:
    print(e["name"])

dept_copy = employees.copy()  #shallow copy, inner dicts still same
dept_copy[0]["salary"] = 100000
print()
print("original salary after editing shallow copy ->" , employees[0]["salary"])

print()
print("contact record (tuple) ->" , contact_record)
