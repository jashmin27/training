# This class has ONE job: print the receipt.

class ReceiptPrinter:

    def print_receipt(self, item, total):
        print("---- Receipt ----")
        print(f"Item: {item}")
        print(f"Total: {total}")
        print("-----------------")
