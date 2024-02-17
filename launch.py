from userInput.user_input import get_option as get_op


def run_file(file_name):
    try:
        exec(open(file_name).read())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


def main():
    user_file_choice = get_op()
    run_file(user_file_choice)


if __name__ == "__main__":
    main()
