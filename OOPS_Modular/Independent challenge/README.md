# Mini Order Management Service

Small challenge project - a simple order management system split into
3 layers (domain, service, repository) with a mock repo and unit tests.

## Why 3 layers?

- **domain.py** - the actual "things" in our system (Order, OrderItem)
  and the rules around them, like you can't confirm an order with no
  items. No storage, no dependencies, just plain objects.
- **repository.py** - handles storage. Right now it's just an
  `InMemoryOrderRepository` (a dict basically), but since it follows
  the `OrderRepository` interface, you could swap it for a real
  database later without touching the service or domain code.
- **service.py** - the layer in between. This is what you'd actually
  call to do things like "create an order" or "confirm an order". It
  uses the repository to save/load and the domain objects to enforce
  the rules.

Basically the idea is: domain doesn't know about repository, service
doesn't care what kind of repository it's given (real db or mock),
and that's what makes it easy to test.

## Files

```
domain.py               - Order, OrderItem, OrderStatus, validation errors
repository.py            - OrderRepository interface + InMemoryOrderRepository (mock)
service.py                - OrderService, business logic
test_order_service.py  - unit tests for all 3 layers
```

## How to run the tests

```
python -m unittest test_order_service.py -v
```

20 tests, all passing right now.

## Quick example

```python
from repository import InMemoryOrderRepository
from service import OrderService

repo = InMemoryOrderRepository()
service = OrderService(repo)

service.create_order("101", "Priya")
service.add_item_to_order("101", "Keyboard", 2, 25.0)
service.add_item_to_order("101", "Mouse", 1, 15.0)

order = service.confirm_order("101")
print(order.status)             # OrderStatus.CONFIRMED
print(service.get_order_total("101"))   # 65.0
```

## Validation rules (in case it's not obvious from the code)

- customer_name and order_id can't be empty
- item quantity has to be > 0
- item price can't be negative
- can't confirm an order that has no items
- can't add items to an order once it's confirmed
- can't confirm a cancelled order, and can't cancel a confirmed one

## Notes / what I'd do differently with more time

- Right now order_id is just whatever string you pass in, in a real
  app this would probably be auto generated (uuid or auto-increment
  from the db).
- No persistence obviously, everything resets once the program stops
  since it's all in memory.
- Didn't add an API layer (Flask/FastAPI) since the task was about the
  architecture, not exposing it over HTTP, but the service layer is
  basically already what you'd hook up to routes.
