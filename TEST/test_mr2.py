import pytest
import sys
import os

# Add the directory where the original program is located to the system path
original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

# Import the original odd_even_sort function
from odd_even_sort import odd_even_sort  # Adjust based on the actual file name

# Test cases for MR2
mr2_test_cases = [
    ([7, 11, 1], 2),  # k = 2
    ([6, 2, 5, 4], 1),  # k = 1
    ([3, 18, 20, 0], 5),  # k = 5
    ([4, 9, 12, 19], 4),  # k = 4
    ([13, 22, 35], 3),  # k = 3
]

def test_mr2():
    """ Test MR2: Verify adding a constant value k produces consistent sorted output """
    for source_list, k in mr2_test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Add k to each element of the original list
        added_values = [x + k for x in source_list]

        # Sort the added values
        sorted_added_values = odd_even_sort(added_values)

        # Add k to each element of the sorted source list
        sorted_source_with_k = [x + k for x in sorted_source]

        # Check if both sorted lists are equal
        assert sorted_added_values == sorted_source_with_k, (
            f"MR2 failed for source_list={source_list} with k={k}. "
            f"Sorted added values: {sorted_added_values}, "
            f"Sorted source + k: {sorted_source_with_k}"
        )
        print(f"MR2 succeeded for source_list={source_list} with k={k}.")

def get_mr_outputs():
    """ Return expected outputs for MR2 test cases """
    expected_outputs = []
    for source_list, k in mr2_test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Add k to each element of the sorted source list
        sorted_source_with_k = [x + k for x in sorted_source]

        expected_outputs.append(sorted_source_with_k)  # Store expected output
    return expected_outputs  # Return the list of expected outputs

if __name__ == "__main__":
    test_mr2()  # Run MR2 tests

    # Print expected outputs for MR2
    expected_outputs = get_mr_outputs()
    for case, output in zip(mr2_test_cases, expected_outputs):
        source_list, k = case
        print(f"Expected output for source_list={source_list} with k={k}: {output}")
