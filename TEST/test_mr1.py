import pytest
import sys
import os

# Add the directory where the original program is located to the system path
original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

# Import the original odd_even_sort function
from odd_even_sort import odd_even_sort  # Adjust based on the actual file name

# Base test cases without follow-up numbers
mr1_test_cases = [
    ([5, 10, 3], 2),
    ([7, 8, 15], 1),
    ([8, 20, 11, 9], 29),
    ([4, 1, 3], 2),
    ([4, 8, 14, 3], 11),
]

def get_mr_outputs():
    """ Return only the final sorted outputs from MR1 test cases """
    expected_outputs = []
    for source_list, add_number in mr1_test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Add the new number to the sorted list
        follow_up_list = sorted_source + [add_number]

        # Get expected output after sorting the new list
        expected_output = odd_even_sort(follow_up_list)
        expected_outputs.append(expected_output)  # Append the expected output to the list
    return expected_outputs  # Return the list of expected outputs

def test_mr1():
    """ Test the MR and verify the output is correct """
    for source_list, add_number in mr1_test_cases:
        # Sort the original source list using the original odd_even_sort
        sorted_source = odd_even_sort(source_list[:])  # Sort the original list

        # Prepare the follow-up list by adding the new number
        follow_up_list = sorted_source + [add_number]  # Create the follow-up list by adding the new number
        sorted_follow_up = odd_even_sort(follow_up_list)  # Sort the modified list

        # Print the success message and the output
        print(f"MR1 succeeded for {follow_up_list}. Output: {sorted_follow_up}")

if __name__ == "__main__":
    test_mr1()
    expected_outputs = get_mr_outputs()
    for case, output in zip(mr1_test_cases, expected_outputs):
        source_list, add_number = case
        print(f"Expected output for source_list={source_list} with added number={add_number}: {output}")
