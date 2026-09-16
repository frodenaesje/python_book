# file: sc_05_05_slicing_demo.py
s = "Helloworld"

print(s[0:5])          # "Hello" – index 0 up to (not incl.) 5
print(s[:])            # "Helloworld" – both ends omitted:
                       # entire string
print(s[::])           # "Helloworld" – same, step omitted too
print(s[None:])        # "Helloworld" – None as start goes to
                       # the edge: the beginning (index 0 here)
print(s[0:len(s)])     # "Helloworld" – index 0 up to len(s):
                       # entire string
print(s[:None])        # "Helloworld" – None as stop goes to
                       # the edge: the end (len(s) here)
print(s[0:5:2])        # "Hlo" – index 0 up to 5 in steps of 2
print(s[::-1])         # "dlrowolleH" – step -1, both ends
                       # omitted, so each goes to its edge:
                       # whole string reversed
print(s[None:None:-1]) # "dlrowolleH" – same as above, written
                       # with None
print(s[0::-1])        # "H" – start 0 included; going back
                       # there is nothing before index 0, so
                       # only 0 is visited
print(s[0:0:-1])       # "" – stop 0 is excluded and equals the
                       # start, so no index is visited
print(s[5:0:-1])       # "wolle" – index 5 back to 0, not incl.
print(s[5::-1])        # "wolleH" – index 5 back to the start,
                       # 0 incl.

# slicing on a list, same rules as for strings
list1 = ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(list1[::-1])  # ['d', 'l', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'H']

original = [1, 2, 3, 4, 5]
copy = original[1:4]
copy[0] = 99
print(original)  # [1, 2, 3, 4, 5]
print(copy)      # [99, 3, 4]
