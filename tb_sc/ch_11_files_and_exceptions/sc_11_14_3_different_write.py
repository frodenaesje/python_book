# file: sc_11_14_3_different_write.py
# Shows different ways to write to files in Python
# Includes a basic method, a context manager, and the Path object's write_text method


def main():
    # Often found in legacy code
    """Write presidents to file using basic open/write/close."""
    # Open file for output
    outputFile = open("Presidents.txt", "w")

    # Write data to the file
    outputFile.write("George Washington\n")
    outputFile.write("John Adams\n")
    outputFile.write("Thomas Jefferson\n") #Write Thomas Jefferson
    
    lines = ["Bill Clinton\n", "Barak Obama\n", "Donald Trump\n"]
    outputFile.writelines(lines) # Write a list of strings

    outputFile.close() # Close the output file

# More Pythonic version using context manager and exception handling
def main_pythonic():
    """Write presidents to file using context manager."""
    presidents = [
        "George Washington\n",
        "John Adams\n",
        "Thomas Jefferson\n",
        "Bill Clinton\n",
        "Barak Obama\n",
        "Donald Trump\n"
    ]
    
    try:
        with open("Presidents.txt", "w") as output_file:
            output_file.writelines(presidents)
        print("File written successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Using Path object's write_text method as an alternative
# The most concise and modern approach
def main_path_method():
    """Write presidents to file using Path object's write_text method."""
    from pathlib import Path
    
    presidents = "George Washington\nJohn Adams\nThomas Jefferson\nBill Clinton\nBarak Obama\nDonald Trump\n"
    
    try:
        Path("Presidents.txt").write_text(presidents)
        print("File written successfully using Path.write_text().")
    except IOError as e:
        print(f"Error writing to file: {e}")

main() # Call the main function
main_pythonic() # Call the Pythonic version
main_path_method() # Call the Path method version
