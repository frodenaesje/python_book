# file: sc_06_09_args_kwargs.py
def sum_all(*numbers):      # packs into a tuple
    total = 0
    for n in numbers:
        total += n
    return total

result = sum_all(1, 2, 3, 4, 5)
print(f"sum_all(1, 2, 3, 4, 5) = {result}")  # 15

numbers_list = [10, 20, 30]
result = sum_all(*numbers_list)  # unpacks the list as arguments
print(f"sum_all(*numbers_list) = {result}")   # 60

def create_profile(**attributes):  # packs into a dict
    profile = []
    for key, value in attributes.items():
        profile.append(f"{key}: {value}")
    return " | ".join(profile)

profile = create_profile(name="Anna", age=30, city="Oslo")
print(profile)

person_dict = {"name": "John", "age": 25, "hobby": "climbing"}
profile = create_profile(**person_dict)  # unpacks dict as kwargs
print(profile)

def print_data(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

print_data(1, 2, 3, name="John", age=29)

# Unpacking both list and dictionary:
data   = [100, 200, 300]
config = {"type": "test", "debug": True}
print_data(*data, **config)
