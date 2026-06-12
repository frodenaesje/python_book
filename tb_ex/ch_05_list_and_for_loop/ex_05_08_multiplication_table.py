# file: ex_05_08_multiplication_table.py

print(f"{'':3}", end="")
for i in range(1, 11):
    print(f"{i:5}", end="")
print()

for row in range(1, 11):
    print(f"{row:3}", end="")
    for col in range(1, 11):
        print(f"{row * col:5}", end="")
    print()
