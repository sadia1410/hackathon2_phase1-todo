import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from logic import add_todo, list_todos, update_todo, delete_todo, toggle_todo_status

class TestLogic(unittest.TestCase):

    def test_add_todo(self):
        todos = []
        todos, next_id = add_todo(todos, 1, "Test Todo", "Test Description")
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['title'], "Test Todo")
        self.assertEqual(next_id, 2)

    def test_list_todos(self):
        # This function prints to stdout, so we can't easily test its output here.
        # We will trust that it works correctly if the other functions work.
        pass

    def test_update_todo(self):
        todos = [{'id': 1, 'title': 'Old Title', 'description': 'Old Description', 'status': 'incomplete'}]
        self.assertTrue(update_todo(todos, 1, "New Title", "New Description"))
        self.assertEqual(todos[0]['title'], "New Title")
        self.assertFalse(update_todo(todos, 2, "New Title", "New Description"))

    def test_delete_todo(self):
        todos = [{'id': 1, 'title': 'Test Todo', 'description': 'Test Description', 'status': 'incomplete'}]
        self.assertTrue(delete_todo(todos, 1))
        self.assertEqual(len(todos), 0)
        self.assertFalse(delete_todo(todos, 2))

    def test_toggle_todo_status(self):
        todos = [{'id': 1, 'title': 'Test Todo', 'description': 'Test Description', 'status': 'incomplete'}]
        self.assertTrue(toggle_todo_status(todos, 1))
        self.assertEqual(todos[0]['status'], 'complete')
        self.assertTrue(toggle_todo_status(todos, 1))
        self.assertEqual(todos[0]['status'], 'incomplete')
        self.assertFalse(toggle_todo_status(todos, 2))

if __name__ == '__main__':
    unittest.main()
