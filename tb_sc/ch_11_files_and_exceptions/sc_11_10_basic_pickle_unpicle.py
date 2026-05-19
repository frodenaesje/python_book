# file: sc_11_10_basic_pickle_unpicle.py
import pickle

class Person:
    """Simple person class with name and age"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __str__(self):
        return f"{self._name} ({self._age} years)"

# ========== SAVE (PICKLE) ==========
def save_persons(persons, filename):
    """Save a list of persons to a binary pickle file"""
    try:
        with open(filename, 'wb') as f:
            pickle.dump(persons, f)
        print(f"✓ Saved {len(persons)} persons to {filename}")
    except IOError as e:
        print(f"✗ Error saving file: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

# ========== LOAD (UNPICKLE) ==========
def load_persons(filename):
    """Load a list of persons from a binary pickle file"""
    try:
        with open(filename, 'rb') as f:
            persons = pickle.load(f)
        print(f"✓ Loaded {len(persons)} persons from {filename}")
        return persons
    except FileNotFoundError:
        print(f"✗ File {filename} not found")
        return []
    except (pickle.UnpicklingError, EOFError):
        print(f"✗ Error: {filename} is corrupted or not a valid pickle file")
        return []
    except Exception as e:
        print(f"✗ Unexpected error loading file: {e}")
        return []

def list_persons(persons):
    """Display all persons with index"""
    if not persons:
        print("No persons in list")
        return
    
    print("\nPersons:")
    for i, person in enumerate(persons):
        print(f"  [{i}] {person}")

def add_person(persons):
    """Add a new person to the list"""
    try:
        name = input("Name: ").strip()
        if not name:
            print("✗ Name cannot be empty")
            return
        age = int(input("Age: "))
        if age < 0 or age > 150:
            print("✗ Age must be between 0 and 150")
            return
        person = Person(name, age)
        persons.append(person)
        print(f"✓ Added {person}")
    except ValueError:
        print("✗ Age must be a number")
    except KeyboardInterrupt:
        print("\n✗ Cancelled")

def delete_person(persons):
    """Delete a person by index"""
    if not persons:
        print("✗ No persons to delete")
        return
    
    list_persons(persons)
    try:
        index = int(input("\nIndex to delete: "))
        if 0 <= index < len(persons):
            deleted = persons.pop(index)
            print(f"✓ Deleted {deleted}")
        else:
            print(f"✗ Index {index} out of range")
    except ValueError:
        print("✗ Invalid index")

def demo():

    # Create some persons
    persons = [
        Person("Anna", 25),
        Person("Bjorn", 30),
        Person("Cecilie", 28)
    ]
    list_persons(persons)
    
    # Save to file
    print("\n2. Saving them to file...")
    filename = "persons.pkl"
    save_persons(persons, filename)
    
    # Load from file
    print("\n3. Loading from file...")
    loaded_persons = load_persons(filename)
    list_persons(loaded_persons)
    
    # Add a new person
    print("\n4. Adding a new person...")
    loaded_persons.append(Person("David", 35))
    list_persons(loaded_persons)
    
    # Save again
    print("\n5. Saving updated list...")
    save_persons(loaded_persons, filename)
    

def interactive_menu():
    filename = "persons.pkl"
    persons = load_persons(filename)
    
    print("\n" + "=" * 60)
    print("INTERACTIVE MENU")
    print("=" * 60)
    print("Commands: [l]ist, [a]dd, [d]elete, [s]ave, [q]uit")
    
    while True:
        try:
            print("\n" + "-" * 60)
            choice = input("Choice: ").strip().lower()
            
            if choice == 'q':
                save_choice = input("Save before quitting? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_persons(persons, filename)
                print("Goodbye!")
                break
            
            elif choice == 'l':
                list_persons(persons)
            
            elif choice == 'a':
                add_person(persons)
            
            elif choice == 'd':
                delete_person(persons)
            
            elif choice == 's':
                save_persons(persons, filename)
            
            else:
                print("✗ Unknown command")
        
        except KeyboardInterrupt:
            print("\n✗ Interrupted. Exiting...")
            break
        except EOFError:
            print("\n✗ End of input. Exiting...")
            break
        except Exception as e:
            print(f"✗ Unexpected error: {e}")


# ========== MAIN ==========

if __name__ == "__main__":
    # Make some data and demonstrate pickle/unpickle
    demo()
    
    # Run interactive menu
    print("\n" + "=" * 60)
    run_menu = input("Run interactive menu? (y/n): ").strip().lower()
    if run_menu == 'y':
        interactive_menu()
