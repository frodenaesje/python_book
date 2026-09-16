# file: snippet_block_scope.py
# if and for blocks do not create a new scope.
# Variables defined in these blocks remain accessible afterwards.

if True:
    y = 10
print(y)  # 10 - y is accessible here

for i in range(5):
    pass
print(i)  # 4 - i lives on after the loop
