# Todo Evolution – Phase 1: Core Functionality

## 1. Functional Requirements

The CLI application must support the following operations for managing todos.

### 1.1. Add a Todo

- The user can add a new todo item.
- Each new todo is assigned a unique ID.
- The user must provide a title for the todo.
- The user can optionally provide a longer description.
- New todos are created with a status of "incomplete" by default.

### 1.2. List Todos

- The user can view a list of all existing todos.
- The list should display the ID, title, and status of each todo.

### 1.3. Update a Todo

- The user can modify the title and/or description of an existing todo.
- The todo is identified by its ID.

### 1.4. Delete a Todo

- The user can remove a todo from the list.
- The todo is identified by its ID.

### 1.5. Mark Todo as Complete/Incomplete

- The user can change the status of a todo.
- The user can mark an "incomplete" todo as "complete".
- The user can mark a "complete" todo as "incomplete".
- The todo is identified by its ID.

## 2. Todo Item Structure

Each todo item will have the following attributes:

- **ID**: A unique identifier for the todo (e.g., an integer).
- **Title**: A short, descriptive title for the todo (required).
- **Description**: A more detailed description of the todo (optional).
- **Status**: The current state of the todo, which can be either "complete" or "incomplete".

## 3. Non-Functional Requirements

- **Storage**: All todos will be stored in-memory. Data will not persist after the application closes.
- **User Interface**: The application will be a command-line interface (CLI). All interactions will be through text commands and outputs.
- **Error Handling**: The application should handle errors gracefully (e.g., when trying to update a non-existent todo) and provide clear messages to the user.
- **Simplicity**: The code should be written in a clear, beginner-friendly manner, without using external libraries.
- **Language**: The application will be implemented in Python.
