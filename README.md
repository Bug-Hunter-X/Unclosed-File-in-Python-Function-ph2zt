# Unclosed File Bug in Python
This example demonstrates a common error in Python: forgetting to close a file properly, leading to potential data loss or resource leaks.

The `bug.py` file contains a function that opens a file for writing but doesn't always close it.  If an exception occurs, the file is left open.

The `bugSolution.py` file shows how to use a `with` statement to ensure the file is always closed, even if exceptions occur.