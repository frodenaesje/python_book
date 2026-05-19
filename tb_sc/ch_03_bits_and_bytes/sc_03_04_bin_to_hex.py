# file: sc_03_04_bin_to_hex.py

# Binary to hex
def bin_to_hex_builtin(bin_str):
    return hex(int(bin_str, 2))[2:].upper() # [2:] removes '0x'

# Binary to hex (without built-in conversion functions)
def bin_to_hex_table(bin_str):
    bin_str = bin_str.replace("0b", "")
    # Pad binary string to a length divisible by 4
    while len(bin_str) % 4 != 0:
        bin_str = '0' + bin_str
    bin_to_hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    return ''.join(bin_to_hex_map[bin_str[i:i+4]] for i in range(0, len(bin_str), 4))

# Test
print(bin_to_hex_builtin("101111"))    # 2F
print(bin_to_hex_table("101111"))    # 2F