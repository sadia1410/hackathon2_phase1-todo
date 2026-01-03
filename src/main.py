# Your task is to develop a command-line todo application in Python.
#
# The application should allow users to:
# - Add a new todo
# - List all todos
# - Update an existing todo
# - Delete a todo
# - Mark a todo as complete or incomplete
#
# Each todo should have the following attributes:
# - ID (unique identifier)
# - Title (string)
# - Description (string, optional)
# - Status (complete or incomplete)
#
# The application should be interactive, with a main loop that prompts the user for commands.
# All data should be stored in memory and will not persist after the application is closed.
#
# Below is the basic structure of the `main.py` file.
# Please complete the code to implement the full functionality as described above.
# You will need to import the `logic.py` module to handle the business logic.
#
# The `logic.py` file will contain the core functions for managing the todos, such as:
# - `add_todo(todos, title, description)`
# - `list_todos(todos)`
# - `update_todo(todos, todo_id, title, description)`
# - `delete_todo(todos, todo_id)`
# - `toggle_todo_status(todos, todo_id)`
#
# Make sure to include error handling for invalid user input and edge cases.
# For example, if the user tries to update or delete a todo that does not exist,
# the application should display an appropriate error message.
#
# The user interface should be clear and easy to understand.
# Use print statements to display menus, prompts, and messages to the user.

import logic

def main():
    """
    Main function to run the todo application.
    """
    todos = []
    next_id = 1

    while True:
        print("\nTodo App Menu:")
        print("1. Add a new todo")
        print("2. List all todos")
        print("3. Update a todo")
        print("4. Delete a todo")
        print("5. Mark a todo as complete/incomplete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the todo: ")
            description = input("Enter the description (optional): ")
            todos, next_id = logic.add_todo(todos, next_id, title, description)
            print("Todo added successfully.")
        elif choice == '2':
            logic.list_todos(todos)
        elif choice == '3':
            try:
                todo_id = int(input("Enter the ID of the todo to update: "))
                title = input("Enter the new title: ")
                description = input("Enter the new description (optional): ")
                if logic.update_todo(todos, todo_id, title, description):
                    print("Todo updated successfully.")
                else:
                    print("Todo not found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                todo_id = int(input("Enter the ID of the todo to delete: "))
                if logic.delete_todo(todos, todo_id):
                    print("Todo deleted successfully.")
                else:
                    print("Todo not found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '5':
            try:
                todo_id = int(input("Enter the ID of the todo to toggle status: "))
                if logic.toggle_todo_status(todos, todo_id):
                    print("Todo status updated successfully.")
                else:
                    print("Todo not found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
