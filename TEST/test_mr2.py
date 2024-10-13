import pytest
import sys
import os
from test_cases_mr2 import test_cases

original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

from odd_even_sort import odd_even_sort

def test_mr2():
    """ Test MR2: Verify that follow-up output equals source output plus k """
    for source_list, add_number in test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Prepare the follow-up list by adding 'add_number' to each element in the source input
        follow_up_list = [x + add_number for x in source_list]

        # Sort the follow-up list
        sorted_follow_up = odd_even_sort(follow_up_list)

        # Calculate expected follow-up output (SO + k)
        expected_follow_up = [x + add_number for x in sorted_source]

        # Check if follow-up output matches expected output
        assert sorted_follow_up == expected_follow_up, (
            f"MR2 failed for source_list={source_list}. "
            f"Sorted follow-up values: {sorted_follow_up}, "
            f"Expected values: {expected_follow_up}"
        )
        print(f"MR2 succeeded for source_list={source_list}.")

def get_mr_outputs():
    """ Return expected outputs for MR2 test cases """
    expected_outputs = []
    for source_list, add_number in test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Calculate expected follow-up output (SO + k)
        expected_follow_up = [x + add_number for x in sorted_source]

        expected_outputs.append(expected_follow_up)
    return expected_outputs

if __name__ == "__main__":
    test_mr2()

    # Print expected outputs for MR2
    expected_outputs = get_mr_outputs()
    for case, output in zip(test_cases, expected_outputs):
        source_list, add_number = case
        print(f"Expected output for source_list={source_list} with k={add_number}: {output}")
