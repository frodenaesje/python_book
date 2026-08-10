# file: ex_11_05_json_contactsjson_contacts_start.py
import json


def load_contacts(filename: str) -> dict[str, dict[str, str]]:
    """Load contacts from a JSON file.

    Returns an empty dict if the file does not exist.

    Structure:
        {"Alice Johnson": {"phone": "...", "email": "...", "city": "..."}, ...}
    """
    # TODO: try to open and json.load() the file
    # TODO: catch FileNotFoundError and return {} instead
    pass


def save_contacts(contacts: dict[str, dict[str, str]], filename: str) -> None:
    """Save contacts dict to a JSON file with indent=2."""
    # TODO: open file for writing and use json.dump() with indent=2
    pass


def add_contact(contacts: dict[str, dict[str, str]],
                name: str, phone: str, email: str, city: str) -> None:
    """Add a contact. Raise ValueError if name already exists."""
    # TODO: check if name is already in contacts
    # TODO: add the new contact as a nested dict
    pass


def remove_contact(contacts: dict[str, dict[str, str]], name: str) -> None:
    """Remove a contact. Raise KeyError if name not found."""
    # TODO: check if name exists, raise KeyError if not
    # TODO: delete the contact
    pass


def search(contacts: dict[str, dict[str, str]],
           query: str) -> dict[str, dict[str, str]]:
    """Return contacts matching query in name or any field (case-insensitive)."""
    # TODO: return a filtered dict where query appears in the name
    #       or in any value of the contact's inner dict
    pass


if __name__ == "__main__":
    contacts = load_contacts("contacts.json")
    print(f"Loaded {len(contacts)} contacts.\n")

    add_contact(contacts, "David Park", "99988877", "david@example.com", "Stavanger")

    print("After adding David Park:")
    for name, info in contacts.items():
        print(f"  {name:<15}| {info['phone']} | {info['email']:<22} | {info['city']}")

    remove_contact(contacts, "David Park")

    print("\nSearch 'berg':")
    for name, info in search(contacts, "berg").items():
        print(f"  {name} | {info['city']}")

    save_contacts(contacts, "contacts.json")
    print(f"\nSaved {len(contacts)} contacts to contacts.json")
