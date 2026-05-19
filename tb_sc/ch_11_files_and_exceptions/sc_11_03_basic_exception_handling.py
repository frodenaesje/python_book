# File: sc_11_03_basic_exception_handling.py
"""
Exception handling progression for file operations
From basic catching to sophisticated error handling
"""

print("=== LEVEL 1: BASIC EXCEPTION HANDLING ===")
# Line 9-16: Most basic form - catches everything but gives no information
print("1. Catching all exceptions (not recommended):")
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except:  # Catches ANY exception - too broad!
    print("Something went wrong with the file!")

print("\n=== LEVEL 2: SPECIFIC EXCEPTION HANDLING ===")
# Line 18-26: Better - catches specific exception type
print("2. Catching specific exceptions:")
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file 'nonexistent.txt' was not found!")

print("\n=== LEVEL 3: MULTIPLE EXCEPTION TYPES ===")
# Line 28-40: Even better - handles different errors differently
print("3. Handling multiple exception types:")

# Alternative 1: Grouping related exceptions
try:
    filename = "sample.txt"  # Change this to test different scenarios
    file = open(filename, 'r')
    content = file.read()
    print(f"File content:\n{content}")
    file.close()
except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    print(f"File access error: {e}")

print("\n3b. Alternative - separate handling:")
# Alternative 2: Each exception handled separately (original approach)
try:
    filename = "sample.txt"  
    file = open(filename, 'r')
    content = file.read()
    print(f"File content:\n{content}")
    file.close()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
except PermissionError:
    print(f"Error: No permission to read '{filename}'!")
except IsADirectoryError:
    print(f"Error: '{filename}' is a directory, not a file!")

print("\n3c. Alternative - using exception hierarchy:")
# Alternative 3: Using exception hierarchy (OSError is parent)
try:
    filename = "sample.txt"
    file = open(filename, 'r')
    content = file.read()
    print(f"File content:\n{content}")
    file.close()
except OSError as e:
    print(f"Operating system error: {e}")
    print(f"Specific error type: {type(e).__name__}")

print("\n=== LEVEL 4: EXCEPTION WITH DETAILS ===")
# Line 42-54: Get exception details for better debugging
print("4. Getting exception details:")
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError as e:
    print(f"File error details: {e}")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")

print("\n=== LEVEL 5: HIERARCHICAL EXCEPTION HANDLING ===")
# Line 56-69: Using exception hierarchy - OSError is parent of FileNotFoundError
print("5. Using exception hierarchy:")
try:
    file = open('sample.txt', 'w')  # This should work
    file.write("Test content")
    file.close()
    
    # Simulate trying to write to a restricted location
    # file = open('/root/forbidden.txt', 'w')  # Uncomment to test permission error
    # file.write("This won't work")
    # file.close()
except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    print(f"Specific file error: {e}")
except OSError as e:  # Catches other OS-related errors
    print(f"General OS error: {e}")

print("\n=== LEVEL 6: COMPLETE EXCEPTION HANDLING ===")
# Line 71-88: Full try-except-else-finally structure
print("6. Complete exception handling structure:")
file = None
try:
    file = open('sample.txt', 'r')
    content = file.read()
    print(f"Successfully read: {content[:50]}...")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:  # Catch any other unexpected errors
    print(f"Unexpected error: {e}")
else:
    print("File operation completed successfully!")
finally:
    # This always runs, whether exception occurred or not
    if file and not file.closed:
        file.close()
        print("File closed in finally block")

print("\n=== LEVEL 7: INPUT VALIDATION WITH EXCEPTIONS ===")
# Line 90-108: Combining input validation with file handling
print("7. Input validation and file operations:")
def safe_file_operation(filename):
    """Safe file operation with input validation"""
    try:
        if not filename:  # Empty string
            raise ValueError("Filename cannot be empty!")
            
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string!")
            
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"File '{filename}' has {len(lines)} lines")
            return lines
            
    except ValueError as e:
        print(f"Input error: {e}")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"No permission to read '{filename}'.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test the function
safe_file_operation("sample.txt")
safe_file_operation("")  # Test empty string
safe_file_operation("nonexistent.txt")  # Test missing file

print("\n=== LEVEL 8: CREATING ROBUST FILE FUNCTIONS ===")
# Line 120-145: Professional-level error handling in functions
def read_file_safely(filename):
    """
    Safely read a file with comprehensive error handling.
    Returns tuple: (success: bool, content: str, error_message: str)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return True, content, ""
    
    except FileNotFoundError:
        return False, "", f"File '{filename}' not found"
    except PermissionError:
        return False, "", f"Permission denied for '{filename}'"
    except UnicodeDecodeError as e:
        return False, "", f"Text encoding error: {e}"
    except OSError as e:
        return False, "", f"System error: {e}"
    except Exception as e:
        return False, "", f"Unexpected error: {e}"

# Test the robust function
print("8. Testing robust file reading:")
test_files = ['sample.txt', 'nonexistent.txt']  # Regular file, missing file
for filename in test_files:
    success, content, error = read_file_safely(filename)
    if success:
        print(f"✓ '{filename}': Read {len(content)} characters")
    else:
        print(f"✗ '{filename}': {error}")

print("\n=== EXCEPTION HANDLING BEST PRACTICES ===")
print("1. Always catch specific exceptions when possible")
print("2. Use exception hierarchy to your advantage") 
print("3. Always clean up resources (use 'finally' or 'with')")
print("4. Log errors for debugging")
print("5. Provide meaningful error messages to users")
print("6. Don't catch exceptions you can't handle meaningfully")
print("7. Use 'else' clause for code that should run only if no exception occurred")
print("8. Use 'finally' for cleanup code that must always run")
