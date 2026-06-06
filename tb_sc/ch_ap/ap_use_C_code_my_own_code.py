# file: ap_use_C_code_my_own_code.py
import ctypes
import sys

# Load the correct library file depending on platform
if sys.platform == "win32":
    lib = ctypes.CDLL("./ap_use_C_code_my_own_code.dll")
else:
    lib = ctypes.CDLL("./ap_use_C_code_my_own_code.so")

# Specify argument types and return type
lib.add.argtypes        = [ctypes.c_int, ctypes.c_int]
lib.add.restype         = ctypes.c_int
lib.absolute_value.argtypes = [ctypes.c_int]
lib.absolute_value.restype  = ctypes.c_int

# Call the C functions
print(lib.add(10, 32))       # 42
print(lib.absolute_value(-17))  # 17
