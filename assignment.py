def read_file(priya):
    try:
        with open(priya,'r')as file:
            content=file.read()
            print("file content")
            print(content)
    except FileNotFoundError:
        print(f"Error:File'{priya}' not found.")
    except PermissionError:
        print(f"Error:Permission denied to access '{priya}'.")
    except IOError:
        print(f"Error:input/output error occurred while reading '{priya}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'.")
    except IOError:
        print(f"Error: Input/Output error occurred while writing to '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
            print(f"Content successfully appended to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}'.")
    except IOError:
        print(f"Error: Input/Output error occurred while appending to '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def main():
    try:
        filename = input("Enter filename: ")
        read_file(filename)

        content_to_write = input("Enter content to write to the file: ")
        write_to_file(filename, content_to_write)

        content_to_append = input("Enter content to append to the file: ")
        append_to_file(filename, content_to_append)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    main()
