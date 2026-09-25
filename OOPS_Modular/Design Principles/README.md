# Refactoring Bad Code

## What this task is about
This task takes deliberately bad code (`before/bad_code.py`) and refactors
it into cleaner code (`after/`), then explains what was wrong and how it
was fixed.

## Problems found in the bad code

1. **Single Responsibility problem**
   The `OrderManager` class did everything by itself: checking the order,
   calculating the discount, saving to a file, printing a receipt, AND
   sending an email. One class had too many jobs.

2. **DRY problem (code duplication)**
   The discount calculation (`total - total * 0.1` if total > 1000) was
   written twice — once to save the order, and again just to print the
   receipt. If the discount rule changed, it would need to be changed in
   two places, and it's easy to forget one.

3. **Tight coupling problem**
   Sending the email was hardcoded directly inside `create_order`. If we
   wanted to send an SMS instead of email, or just print to the console
   for testing, we would have to edit the `OrderManager` class itself.

## How it was fixed (after/)

| File | Responsibility |
|------|-----------------|
| `discount.py` | Calculates the discount. Only ONE place now (fixes DRY). |
| `order_repository.py` | Only saves orders to a file. |
| `receipt_printer.py` | Only prints the receipt. |
| `notifier.py` | A `Notifier` interface with `EmailNotifier` and `ConsoleNotifier`. `OrderService` depends on this interface, not a specific class (fixes tight coupling / dependency inversion). |
| `order_service.py` | Coordinates the whole order process using the pieces above. Each piece has one clear job now (fixes Single Responsibility). |
| `main.py` | Creates all the pieces and connects them together. |

## How to run
```
cd before
python3 bad_code.py
```
```
cd after
python3 main.py
```
Both give the same result, but the `after` version is much easier to
change and test, because each class only does one thing.
