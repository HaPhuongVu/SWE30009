import pytest
import sys
import os
from test_cases_mr2 import test_cases

original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

from odd_even_sort import odd_even_sort

def test_mr2():
    """ Test MR2: Verify sorting the follow-up list produces the expected output """
    for source_list, follow_up_list in test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Sort the follow-up list
        sorted_follow_up = odd_even_sort(follow_up_list)

        # Add to the original sorted source list the difference (follow-up case logic)
        sorted_source_with_k = [x + (y - x) for x, y in zip(source_list, follow_up_list)]

        # Check if both sorted lists match
        assert sorted_follow_up == sorted_source_with_k, (
            f"MR2 failed for source_list={source_list}. "
            f"Sorted follow-up values: {sorted_follow_up}, "
            f"Sorted source + k: {sorted_source_with_k}"
        )
        print(f"MR2 succeeded for source_list={source_list}.")

def get_mr_outputs():
    """ Return expected outputs for MR2 test cases """
    expected_outputs = []
    for source_list, follow_up_list in test_cases:
        # Sort the original list
        sorted_source = odd_even_sort(source_list)

        # Add to the original sorted source list the difference (follow-up case logic)
        sorted_source_with_k = [x + (y - x) for x, y in zip(source_list, follow_up_list)]

        expected_outputs.append(sorted_source_with_k)
    return expected_outputs

if __name__ == "__main__":
    test_mr2()

    # Print expected outputs for MR2
    expected_outputs = get_mr_outputs()
    for case, output in zip(test_cases, expected_outputs):
        source_list, follow_up_list = case
        print(f"Expected output for source_list={source_list}: {output}")
