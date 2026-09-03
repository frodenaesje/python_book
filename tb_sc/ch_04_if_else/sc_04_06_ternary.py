# sc_04_06_ternary.py
# Syntax: value_if_true  if  condition  else  value_if_false
num_hours = 1
price     = 30

# Regular if-else
if num_hours == 1:
    hours_text = 'hour'
else:
    hours_text = 'hours'

# Ternary version - same result
hours_text = 'hour' if num_hours == 1 else 'hours'

print(f'{num_hours} {hours_text} costs ${price}.')
# 1 hour costs $30.

# More examples
n = 4
status = 'even' if n % 2 == 0 else 'odd'
age = 20
label  = 'adult' if age >= 18 else 'minor'
print(status)   # even
print(label)    # adult