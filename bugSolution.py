def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write('some data')
    except Exception as e:
        print(f"An error occurred: {e}")

#Using a with statement ensures the file is closed, even if an exception occurs.