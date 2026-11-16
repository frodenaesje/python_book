# file: sc_03_06_image_storage.py

width = int(input("Image width in pixels: "))
height = int(input("Image height in pixels: "))

pixels = width * height
grayscale_bytes = pixels
rgb_bytes = pixels * 3
rgba_bytes = pixels * 4

BYTES_PER_MIB = 1024 ** 2

print(f"Pixels: {pixels:,}")
print(f"Grayscale: {grayscale_bytes:,} bytes "
      f"({grayscale_bytes / BYTES_PER_MIB:.2f} MiB)")
print(f"RGB:       {rgb_bytes:,} bytes "
      f"({rgb_bytes / BYTES_PER_MIB:.2f} MiB)")
print(f"RGBA:      {rgba_bytes:,} bytes "
      f"({rgba_bytes / BYTES_PER_MIB:.2f} MiB)")
