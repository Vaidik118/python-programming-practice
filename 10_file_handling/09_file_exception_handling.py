# 09_file_exception_handling.py

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: The file does not exist.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")

    except IsADirectoryError:
        print("Error: The path refers to a directory, not a file.")

    except UnicodeDecodeError:
        print("Error: The file contains text that is not valid UTF-8.")

    except OSError as error:
        print("File system error:", error)

    else:
        print("File read successfully!")
        print(content)

    finally:
        print("File operation finished.")


read_file("sample.txt")