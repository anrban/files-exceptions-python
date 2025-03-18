def read_file(filename):
    """Function to read a file and handle errors if the file does not exist."""
    try:
        with open(filename, 'r') as file:
            print("File Content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

read_file("sample.txt")
