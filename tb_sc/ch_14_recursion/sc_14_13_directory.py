# file: sc_14_13_directory.py
# Example of using recursion to calculate the total size
# of a directory (including subdirectories)
from pathlib import Path

def get_size(path):
	if path.is_file():
		# stat().st_size gets the file size in bytes.
		return path.stat().st_size

	# is_dir() checks whether the path points to a directory.
	if not path.is_dir():
		raise FileNotFoundError(path)

	# iterdir() yields each _immediate_ child
    # (files and folders) in the directory
	return sum(get_size(child) for child in path.iterdir())

def main():
	# Input format: absolute or relative path to a file or directory.
	raw = input("Enter a file or directory path: ").strip()
	path = Path(raw)

	try:
		size = get_size(path)
	except (FileNotFoundError, PermissionError):
		print("Directory or file does not exist or is not accessible")
		return

	print(path)
	print(f"{size} bytes")

if __name__ == "__main__":
	main()