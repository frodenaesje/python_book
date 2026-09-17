# sc_04_06_ternary.py
# Syntax: value_if_true  if  condition  else  value_if_false
num_hours = 1
price = 30

hours_text = "hour" if num_hours == 1 else "hours"
dollar_text = "dollar" if price == 1 else "dollars"

print(f"{num_hours} {hours_text} costs ${price} {dollar_text}.")
