# sc_04_07_guard_clauses.py

is_registered = True
is_open       = True
valid_payment = True
duration_min  = 45

# Without guard clauses - 4 levels deep
if is_registered:
    if is_open:
        if valid_payment:
            if duration_min <= 15:
                price = 0
            elif duration_min <= 60:
                price = 30
            else:
                price = 60
            print(f'Price: {price} NOK')
        else:
            print('No valid payment method.')
    else:
        print('The car park is closed.')
else:
    print('Vehicle not registered.')

# With guard clauses - errors first, flat main logic
if not is_registered:
    print('Vehicle not registered.')
elif not is_open:
    print('The car park is closed.')
elif not valid_payment:
    print('No valid payment method.')
else:
    if duration_min <= 15:  price = 0
    elif duration_min <= 60: price = 30
    else:                   price = 60
    print(f'Price: {price} NOK')