# file: ap_use_C_code_existing_library.py
import ctypes
import ctypes.util
import sys

# Find the correct C library for the platform
if sys.platform == "win32":
    libc = ctypes.CDLL("msvcrt.dll")      # always available on Windows
else:
    libc_name = ctypes.util.find_library("c")  # "libc.so.6" etc.
    libc = ctypes.CDLL(libc_name)

# Specify return type - the function returns int
libc.abs.restype  = ctypes.c_int
libc.abs.argtypes = [ctypes.c_int]

print(libc.abs(-42))    # 42
print(libc.abs(17))     # 17
