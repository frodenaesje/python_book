# file: sc_03_05_hex_to_bin.py
# Hex to binary
def hex_to_bin_builtin(hex_str):
    return bin(int(hex_str, 16))[2:]  # [2:] removes '0b'

# Hex to binary (without built-in conversion functions)
def hex_to_bin_table(hex_str):
    # Remove optional '0x' or '0X' prefix from hex_str
    hex_str = hex_str.upper().replace("0X", "")
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return ''.join(hex_to_bin_map[ch] for ch in hex_str)

# Test
print(hex_to_bin_builtin("2F"))    # 101111
print(hex_to_bin_table("2F"))    # 00101111