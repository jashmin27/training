# Inheritance & Composition

This project shows **Notification**, **Payment** and **Reporting** examples using two approaches:

1. Inheritance
2. Composition

The code is written in Python.

## Files

| File | What it has |
|------|-------------|
| `inheritance_example.py` | Notification, Payment, Reporting using inheritance |
| `composition_example.py` | Notification, Payment, Reporting using composition |

## How to run

```
python inheritance_example.py
python composition_example.py
```

## Inheritance

Inheritance means a child class gets the features of a parent class (**is-a** relationship).

In `inheritance_example.py`:

- `Notification`, `Payment` and `Report` are the parent classes with a basic `send()` / `pay()` / `generate()` method.
- `EmailNotification`, `SMSNotification`, `CreditCardPayment`, `UpiPayment`, `PDFReport` and `ExcelReport` are child classes that extend the parent.
- **Overriding** is used in each child's method (like `UpiPayment.show_receipt()`), where the child writes its own version of the parent's method.

## Composition

Composition means a class keeps another object inside it and uses it (**has-a** relationship).

In `composition_example.py`:

- `Notification` has a sender (`EmailSender` or `SMSSender`).
- `Payment` has a payment method (`CreditCard` or `Upi`).
- `Report` has a format (`PDFFormat` or `ExcelFormat`).

## Inheritance vs Composition

| Inheritance | Composition |
|-------------|-------------|
| is-a relationship | has-a relationship |
| Child depends on the parent class | Classes are separate and independent |
| Behavior is fixed when the class is written | Behavior can be changed while the program runs |
| Good when classes are truly a type of the parent | Good when we just want to use another class's work |

## Why composition is often better

- Changing the parent class can break all child classes in inheritance, but composition keeps classes separate.
- In composition we can swap the object easily. For example, `n1.sender = SMSSender()` changes Email to SMS without writing a new class.
- We do not need a new class for every combination. With inheritance, "PDF report sent by Email" would need a new subclass, but with composition we just combine the objects.
- Inheritance is still useful when there is a real "is-a" relationship, like `EmailNotification` is a `Notification`.
