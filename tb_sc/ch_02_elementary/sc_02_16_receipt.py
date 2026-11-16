# file: sc_02_16_receipt.py
VAT_RATE = 0.25

item1 = "USB-C cable"
price1 = 149.00
item2 = "Wireless mouse"
price2 = 399.50
item3 = "Screen cleaner"
price3 = 89.90
shipping = 79.00

total = price1 + price2 + price3 + shipping
# Extract VAT from a total that already includes VAT.
vat = total * VAT_RATE / (1 + VAT_RATE)

print(f"{'RECEIPT':^32}")
print("-" * 32)
print(f"{item1:<20}{price1:>12,.2f}")
print(f"{item2:<20}{price2:>12,.2f}")
print(f"{item3:<20}{price3:>12,.2f}")
print(f"{'Shipping':<20}{shipping:>12,.2f}")
print("-" * 32)
print(f"{'Total (NOK)':<20}{total:>12,.2f}")
vat_label = f"Incl. VAT {VAT_RATE:.0%}"
print(f"{vat_label:<20}{vat:>12,.2f}")
