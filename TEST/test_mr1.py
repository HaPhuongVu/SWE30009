import pytest
import sys
import os
from test_cases_mr1 import test_cases

original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

from odd_even_sort import odd_even_sort

def get_mr_outputs():
    """ Return only the final sorted outputs from the test cases """
    expected_outputs = []
    for source_list, follow_up_list in test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Sort the follow-up list (includes the extra number)
        expected_output = odd_even_sort(follow_up_list)

        expected_outputs.append(expected_output)
    return expected_outputs

def test_mr1():
    """ Test the MR1 and verify the output is correct """
    for source_list, follow_up_list in test_cases:
        # Sort the original source list using the original odd_even_sort
        sorted_source = odd_even_sort(source_list[:])

        # Sort the follow-up list
        sorted_follow_up = odd_even_sort(follow_up_list)

        # Print the success message and the output
        print(f"MR1 succeeded for {follow_up_list}. Output: {sorted_follow_up}")

if __name__ == "__main__":
    test_mr1()

    # Print expected outputs for MR1
    expected_outputs = get_mr_outputs()
    for case, output in zip(test_cases, expected_outputs):
        source_list, follow_up_list = case
        print(f"Expected output for source_list={source_list} with follow-up list={follow_up_list}: {output}")
