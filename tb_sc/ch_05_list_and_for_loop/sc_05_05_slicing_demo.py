# file: sc_05_05_slicing_demo.py
s = "Helloworld"

print(s[0:5])             # "Hello" – from index 0 to 4
print(s[:])               # "Helloworld" – entire string
print(s[::])              # "Helloworld" – entire string
print(s[None:])           # "Helloworld" – None is interpreted as
                          # default value, i.e. 0
print(s[0:len(s)])        # "Helloworld" – entire string
print(s[:None])           # "Helloworld" – None is interpreted as
                          # default value, i.e. len(s)

print(s[0:5:2])           # "Hlo" – every other character from
                          # index 0 to 4
print(s[::-1])            # "dlrowolleH" – reverses the entire
                          # string, default values used
print(s[None:None:-1])    # "dlrowolleH" – reverses the entire
                          # string, default values used
print(s[5:0:-1])          # "wolle" – backwards from index 5
                          # to 1
print(s[5::-1])           # "olleH" – backwards from index 5
                          # to the start

# slicing on a list, same rules as for strings
list1 = ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(list1[::-1])  # ['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'H']
