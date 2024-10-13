import sys
import os
from test_cases_mr1 import test_cases

# Add the path to the original odd_even_sort function
original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

from odd_even_sort import odd_even_sort

def get_mr_outputs():
    """ Return only the sorted outputs for the given test cases (SI and reordered FI) """
    expected_outputs = []
    for source_list, follow_up_list in test_cases:
        # Sort the original source list (SI)
        sorted_source = odd_even_sort(source_list[:])

        # Sort the reordered follow-up list (FI)
        sorted_follow_up = odd_even_sort(follow_up_list[:])

        # Append both sorted outputs for comparison
        expected_outputs.append((sorted_source, sorted_follow_up))

    return expected_outputs

def test_mr_reordering():
    """ Test the MR where the follow-up input (FI) is a reordered version of SI """
    for source_list, follow_up_list in test_cases:
        # Sort the original source list (SI)
        sorted_source = odd_even_sort(source_list[:])

        # Sort the reordered follow-up input (FI)
        sorted_follow_up = odd_even_sort(follow_up_list[:])

        # Assert that sorting SI and FI gives the same result
        assert sorted_source == sorted_follow_up, \
            f"Failed MR for SI={source_list} and FI={follow_up_list}. Expected: {sorted_source}, Got: {sorted_follow_up}"

        # Print success message for the test case
        print(f"MR succeeded for SI={source_list} and reordered FI={follow_up_list}. Output: {sorted_follow_up}")

if __name__ == "__main__":
    # Run the test for the MR of reordering
    test_mr_reordering()

    # Print expected outputs for the test cases
    expected_outputs = get_mr_outputs()
    for (sorted_source, sorted_follow_up) in expected_outputs:
        print(f"Expected output: SI sorted={sorted_source}, FI sorted={sorted_follow_up}")
