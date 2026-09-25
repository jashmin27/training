# This is the "before" version - deliberately written with bad design.
# Problems on purpose:
# 1. One class does everything (order validation, discount, saving, printing, email)
# 2. The discount logic is copied twice (not DRY)
# 3. Email sending is hardcoded inside the class (tightly coupled)


class OrderManager:

    def __init__(self):
        self.orders = []

    def create_order(self, item, price, quantity, customer_email):
        if price <= 0 or quantity <= 0:
            print("Invalid order")
            return

        # discount logic (first copy)
        total = price * quantity
        if total > 1000:
            total = total - (total * 0.1)

        order = {
            "item": item,
            "total": total,
            "email": customer_email
        }
        self.orders.append(order)

        # save to file
        with open("orders.txt", "a") as f:
            f.write(f"{item},{total}\n")

        # print receipt, but discount is calculated AGAIN here (second copy)
        raw_total = price * quantity
        if raw_total > 1000:
            raw_total = raw_total - (raw_total * 0.1)
        print("---- Receipt ----")
        print(f"Item: {item}")
        print(f"Total: {raw_total}")
        print("-----------------")

        # send email directly here, hardcoded
        print(f"Sending email to {customer_email}: Your order for {item} is confirmed.")


# main program
manager = OrderManager()
manager.create_order("Laptop", 500, 3, "test@example.com")
