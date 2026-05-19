## file: sc_05_02_list_initialization.py

number_list  = []      # empty list - simplest way
number_list2 = list()  # with constructor - same result

name_list  = ["anna", "bjorn", "clara"]    # literal with content
name_list2 = list(["john", "paul", "liam"]) # constructor with content

mixed_list = [1, "text", 3.14, True] # mixed content: OK

number_list.append(1) # add element to the end
number_list.append(2) # list is now [1, 2]

name_list[0] = "suzanne"   # Change 1st element, lists are mutable
mixed_list[1] = "new_text" # Change second element

text    = "python"
letters = list(text)   # ["p", "y", "t", "h", "o", "n"]
word    = [text]       # ["python"] - the string as a single element in the list
