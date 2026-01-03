# This module contains the core logic for the todo application.
# It includes functions for adding, listing, updating, deleting,
# and toggling the status of todos.

def add_todo(todos, next_id, title, description):
    """
    Adds a new todo to the list.
    """
    new_todo = {
        'id': next_id,
        'title': title,
        'description': description,
        'status': 'incomplete'
    }
    todos.append(new_todo)
    return todos, next_id + 1

def list_todos(todos):
    """
    Lists all the todos.
    """
    if not todos:
        print("No todos found.")
    else:
        for todo in todos:
            print(f"ID: {todo['id']}, Title: {todo['title']}, "
                  f"Description: {todo['description']}, Status: {todo['status']}")

def update_todo(todos, todo_id, title, description):
    """
    Updates an existing todo.
    """
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = title
            todo['description'] = description
            return True
    return False

def delete_todo(todos, todo_id):
    """
    Deletes a todo from the list.
    """
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            del todos[i]
            return True
    return False

def toggle_todo_status(todos, todo_id):
    """
    Toggles the status of a todo between 'complete' and 'incomplete'.
    """
    for todo in todos:
        if todo['id'] == todo_id:
            if todo['status'] == 'incomplete':
                todo['status'] = 'complete'
            else:
                todo['status'] = 'incomplete'
            return True
    return False
