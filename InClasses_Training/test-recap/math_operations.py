def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


# adding an item on an ecommerce shopping cart
#
# - customer choose a product (S-XL)
# - click [add to cart]                 # backend: check inventory
# - they visit a payment page           # backend: checking with payment processor API
# - See a success page  make            # backend: show transaction details and shipping

# ==> e2e test (end to end test!)
