# file: sc_11_12_basic_json.py
"""
Simple demonstration of JSON serialization with a Person class
Comparison with pickle: JSON is human-readable and language-independent
"""
import json


class Person:
    """Simple person class with name and age"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __str__(self):
        return f"{self._name} ({self._age} years)"
    
    def __repr__(self):
        return f"Person('{self._name}', {self._age})"
    
    # Convert to dictionary for JSON serialization
    def to_dict(self):
        """Convert person to dictionary"""
        return {
            "name": self._name,
            "age": self._age
        }
    
    # Create from dictionary
    @staticmethod
    def from_dict(data):
        """Create person from dictionary"""
        return Person(data["name"], data["age"])


# ========== SAVE (JSON) ==========

def save_persons(persons, filename):
    """Save a list of persons to a JSON file"""
    try:
        # Convert persons to list of dictionaries
        data = [person.to_dict() for person in persons]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(persons)} persons to {filename}")
    except IOError as e:
        print(f"✗ Error saving file: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


# ========== LOAD (JSON) ==========

def load_persons(filename):
    """Load a list of persons from a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert dictionaries back to Person objects
        persons = [Person.from_dict(item) for item in data]
        print(f"✓ Loaded {len(persons)} persons from {filename}")
        return persons
    except FileNotFoundError:
        print(f"✗ File {filename} not found")
        return []
    except json.JSONDecodeError:
        print(f"✗ Error: {filename} is corrupted or not a valid JSON file")
        return []
    except (KeyError, TypeError) as e:
        print(f"✗ Error: Invalid data structure in {filename}")
        return []
    except Exception as e:
        print(f"✗ Unexpected error loading file: {e}")
        return []


# ========== LIST PERSONS ==========

def list_persons(persons):
    """Display all persons with index"""
    if not persons:
        print("No persons in list")
        return
    
    print("\nPersons:")
    for i, person in enumerate(persons):
        print(f"  [{i}] {person}")


# ========== ADD PERSON ==========

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


# ========== DELETE PERSON ==========

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


# ========== VIEW RAW JSON ==========

def view_json_file(filename):
    """Display the raw JSON content of the file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"\nRaw JSON content of {filename}:")
        print(content)
    except FileNotFoundError:
        print(f"✗ File {filename} not found")


# ========== DEMO ==========

def demo():
    """Demonstrate JSON serialization"""
    print("=" * 60)
    print("JSON SERIALIZATION DEMO")
    print("=" * 60)
    
    # Create some persons
    print("\n1. Creating persons...")
    persons = [
        Person("Anna", 25),
        Person("Bjorn", 30),
        Person("Cecilie", 28)
    ]
    list_persons(persons)
    
    # Save to file
    print("\n2. Saving to JSON file...")
    filename = "persons.json"
    save_persons(persons, filename)
    
    # Show raw JSON (human-readable!)
    view_json_file(filename)
    
    # Load from file
    print("\n3. Loading from JSON file...")
    loaded_persons = load_persons(filename)
    list_persons(loaded_persons)
    
    # Add a new person
    print("\n4. Adding a new person...")
    loaded_persons.append(Person("David", 35))
    list_persons(loaded_persons)
    
    # Save again
    print("\n5. Saving updated list...")
    save_persons(loaded_persons, filename)
    
    # Delete a person
    print("\n6. Deleting person at index 1...")
    if len(loaded_persons) > 1:
        deleted = loaded_persons.pop(1)
        print(f"✓ Deleted {deleted}")
        list_persons(loaded_persons)
    
    # Save final version
    print("\n7. Saving final version...")
    save_persons(loaded_persons, filename)
    
    # Show final JSON
    view_json_file(filename)


# ========== INTERACTIVE MENU ==========

def interactive_menu():
    """Simple interactive menu"""
    filename = "persons.json"
    persons = load_persons(filename)
    
    print("\n" + "=" * 60)
    print("INTERACTIVE MENU")
    print("=" * 60)
    print("Commands: [l]ist, [a]dd, [d]elete, [s]ave, [v]iew, [q]uit")
    
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
            
            elif choice == 'v':
                view_json_file(filename)
            
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
    # Run demo
    demo()
    
    # Run interactive menu
    print("\n" + "=" * 60)
    run_menu = input("Run interactive menu? (y/n): ").strip().lower()
    if run_menu == 'y':
        interactive_menu()
