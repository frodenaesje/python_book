# file: sc_04_13_shipping_cost.py
FREE_SHIPPING_LIMIT = 500
MAX_WEIGHT_KG = 35
MAX_MAILBOX_KG = 2

order_total = float(input("Order total (NOK): "))
weight_kg = float(input("Package weight (kg): "))
method = input("Delivery (pickup/mailbox/home): ").strip().lower()

match method:
    case "pickup":
        delivery_fee = 0
    case "mailbox":
        delivery_fee = 10
    case "home":
        delivery_fee = 99
    case _:
        delivery_fee = None

if delivery_fee is None:
    print(f"Unknown delivery method: '{method}'")
elif order_total < 0:
    print("Order total cannot be negative.")
elif not 0 < weight_kg <= MAX_WEIGHT_KG:
    print(f"Weight must be more than 0 and at most {MAX_WEIGHT_KG} kg.")
elif method == "mailbox" and weight_kg > MAX_MAILBOX_KG:
    print(f"Too heavy for the mailbox (max {MAX_MAILBOX_KG} kg).")
elif order_total >= FREE_SHIPPING_LIMIT:
    print("Free shipping!")
else:
    if weight_kg <= 1:
        base_price = 49
    elif weight_kg <= 5:
        base_price = 79
    elif weight_kg <= 10:
        base_price = 119
    else:
        base_price = 199

    shipping = base_price + delivery_fee
    missing = FREE_SHIPPING_LIMIT - order_total
    print(f"Shipping: {shipping} NOK")
    print(f"Spend {missing:.2f} NOK more to get free shipping.")
