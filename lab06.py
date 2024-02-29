# 1. Name:
#      Gavin Hart
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program reads a list of sorted names from a JSON file and then uses an advanced search algorithm (binary search)
#      to determine if a specific name is in the list. It prompts the user for the filename and the name to search for,
#      then displays a message indicating whether the name was found.
# 4. Algorithmic Efficiency:
#      The algorithmic efficiency of the binary search implemented in this program is O(log n), where n is the number of items
#      in the list. This is because the search space is halved with each iteration, significantly reducing the number of
#      comparisons needed to find the target or conclude it is not in the list.
# 5. What was the hardest part? Be as specific as possible.
#      The most challenging part was ensuring that the binary search algorithm correctly handled all edge cases, such as
#      searching for the first or last element in the list and searching for an element not present in the list. Getting
#      the loop and index conditions right to avoid infinite loops or missing the target element took some trial and error.
# 6. How long did it take for you to complete the assignment?
#      -2.5hrs

import json

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def read_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data["array"]
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

def main():
    filename = input("What is the name of the file? ")
    contents = read_file_contents(filename)
    if contents is not None:
        search_name = input("What name are we looking for? ")
        found = binary_search(contents, search_name)
        if found:
            print(f"We found {search_name} in {filename}.")
        else:
            print(f"{search_name} was not found in {filename}.")

if __name__ == "__main__":
    main()
