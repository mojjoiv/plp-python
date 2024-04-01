try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("Line 2: 12345\n")
        file.write("Another line: Python is awesome!\n")
        print("File 'my_file.txt' created successfully and data written.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File creation process completed.\n")

try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process completed.\n")

try:
    with open("my_file.txt", "a") as file:
        file.write("Appended line 1\n")
        file.write("Line 6: 67890\n")
        file.write("Another appended line: Python is powerful!\n")
        print("Data appended to 'my_file.txt'.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process completed.")
