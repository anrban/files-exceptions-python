def write_to_file(filename):
    """Function to take user input and write it to a file."""
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + "\n")
    print(f"Data written to {filename}")

def append_to_file(filename):
    """Function to take user input and append it to the file."""
    user_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(user_input + "\n")
    print(f"Data appended to {filename}")

def read_file(filename):
    """Function to read and display the content of the file."""
    print("\nFinal Content of the File:")
    with open(filename, 'r') as file:
        print(file.read())


filename = "output.txt"


write_to_file(filename)
append_to_file(filename)
read_file(filename)
