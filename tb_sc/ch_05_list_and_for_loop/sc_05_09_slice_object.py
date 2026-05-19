# file: sc_05_09_slice_object.py

# Demonstration of slice objects and how None provides default values

text = "Hello there"

# Create slice objects
slice1 = slice(2, None)      # From index 2 to the end
slice2 = slice(None, 5)      # From start to index 5
slice3 = slice(None, None)   # Entire string
slice4 = slice(2, 8, 2)      # From 2 to 8, step 2

# Use the slice objects
print("text[2:None] =>", text[slice1])
print("text[:5] =>", text[slice2])
print("text[:] =>", text[slice3])
print("text[2:8:2] =>", text[slice4])

# Check what None gives as default values
print("slice1.start:", slice1.start, "slice1.stop:", slice1.stop, "slice1.step:", slice1.step)
print("slice2.start:", slice2.start, "slice2.stop:", slice2.stop, "slice2.step:", slice2.step)
print("slice3.start:", slice3.start, "slice3.stop:", slice3.stop, "slice3.step:", slice3.step)
print("slice4.start:", slice4.start, "slice4.stop:", slice4.stop, "slice4.step:", slice4.step)

# Explanation:
# When start, stop or step is None, Python uses:
# - start=None: from the start
# - stop=None: to the end
# - step=None: step 1
