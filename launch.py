import sys


def run_file(file_name):
    try:
        exec(open(file_name).read())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


def main():
    print("Choose a file to run:")
    print("1. File1.py")
    print("2. File2.py")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        run_file("File1.py")
    elif choice == "2":
        run_file("File2.py")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
