

```markdown
# Contact Management System

A simple Contact Management System written in Python. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using lists and dictionaries.

## Features

1. **Add Contact**: Allows the user to add a new contact with details such as name, phone number, and email.
2. **View Contacts**: Displays all the contacts in the system.
3. **Update Contact**: Provides functionality to update existing contact details.
4. **Delete Contact**: Enables the user to delete a contact from the system.

## Data Structure

The application uses Python's built-in data structures:
- **List**: To store multiple contact dictionaries.
- **Dictionary**: To store individual contact details with keys such as `name`, `phone`, and `email`.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/contact-management-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd contact-management-system
    ```

## Example

Here is a brief example of how the Contact Management System works:

1. **Add Contact**:
    ```sh
    Enter name: John Doe
    Enter phone number: 123-456-7890
    Enter email: johndoe@example.com
    Contact added successfully!
    ```

2. **View Contacts**:
    ```sh
    Contacts List:
    1. Name: John Doe, Phone: 123-456-7890, Email: johndoe@example.com
    ```

3. **Update Contact**:
    ```sh
    Enter the contact name to update: John Doe
    Enter new phone number: 098-765-4321
    Enter new email: john.doe@newdomain.com
    Contact updated successfully!
    ```

4. **Delete Contact**:
    ```sh
    Enter the contact name to delete: John Doe
    Contact deleted successfully!
    ```