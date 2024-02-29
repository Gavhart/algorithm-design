import json

def read_json(filename):
    """Reads a JSON file and returns the list of items or None if file not found."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            assert "array" in data, "JSON format error: 'array' key not found."
            return data["array"]
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None  # Return None to indicate the file was not found

def sort_list(unsorted_list):
    """Sorts the list using a simple sorting algorithm and returns the sorted list."""
    for i in range(len(unsorted_list)):
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                # Swapping
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list

def display_sorted_list(sorted_list):
    """Displays the sorted list."""
    for item in sorted_list:
        print(f"\t{item}")

def process_file(filename):
    """Process a single file: read, sort, and display."""
    print(f"Processing file: {filename}")
    unsorted_list = read_json(filename)
    if unsorted_list is None:  # Check if the file was not found
        print(f"Skipping file: {filename} due to error.\n")
        return  # Skip this file and continue with the next one
    
    assert isinstance(unsorted_list, list), "Error: Data is not a list."
    assert all(isinstance(item, str) for item in unsorted_list), "Error: List items must be strings."
    
    sorted_list = sort_list(unsorted_list)
    print("The values in", filename, "are:")
    display_sorted_list(sorted_list)
    print("\n")  # Add a newline for better readability between files

if __name__ == "__main__":
    # List of files to process
    files_to_process = [
        "Lab08.empty.json",
        "Lab08.trivial.json",
        "Lab08.languages.json",
        "Lab08.states.json",
        "Lab08.cities.json"
    ]

    for filename in files_to_process:
        process_file(filename)
