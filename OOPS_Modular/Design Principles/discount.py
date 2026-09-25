# This class has ONE job: calculate the discount.
# Fixes the DRY problem - the discount logic now exists in only one place.

class DiscountCalculator:

    def calculate_total(self, price, quantity):
        total = price * quantity
        if total > 1000:
            total = total - (total * 0.1)
        return total
