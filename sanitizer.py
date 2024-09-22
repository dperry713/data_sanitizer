class UsernameError(Exception):
    def __init__(self, message="Invalid username"):
        super().__init__(message)

def process_data_entries(data_list):
    parsed_data = []
    for entry in data_list:
        try:
            parsed_value = int(entry)
            parsed_data.append(parsed_value)
        except ValueError:
            print(f"Warning: Unable to convert '{entry}' to an integer. Skipping.")

    return parsed_data

def main():
    try:
        # Example data list (you can replace this with your own data)
        data_list = ["42", "hello", "123", "world", "567"]

        parsed_data = process_data_entries(data_list)
        print("Parsed data (integers):", parsed_data)
    except UsernameError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
