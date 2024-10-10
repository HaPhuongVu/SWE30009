import sys
import os
import importlib
from tabulate import tabulate

mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MUTANTS'))
sys.path.insert(0, mutant_dir)

# Import the function to get expected outputs from mr2
from test_mr2 import get_mr_outputs
from test_cases_mr2 import test_cases

# Get the expected outputs from MR2
expected_outputs = get_mr_outputs()


def import_mutant(mutant_name):
    """
    Dynamically import the odd_even_sort function from the mutant module.
    :param mutant_name: The name of the mutant file (e.g., 'm1', 'm2').
    :return: The odd_even_sort function from the mutant.
    """
    mutant_module = importlib.import_module(mutant_name)
    return mutant_module.odd_even_sort

def run_tests_for_mutant(mutant_name, test_cases, expected_outputs):
    """ Run all test cases for a given mutant and return the detailed result """
    results = []

    try:
        odd_even_sort = import_mutant(mutant_name)

        for (source_list, follow_up_list), expected_output in zip(test_cases, expected_outputs):
            # Sort the original source list (source test case)
            sorted_source = odd_even_sort(source_list[:])  # Sort the original list

            # Sort the follow-up list (follow-up test case)
            sorted_follow_up = odd_even_sort(follow_up_list[:])

            # Compare the mutant's sorted follow-up output with the expected output
            result = "Survived" if sorted_follow_up == expected_output else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,        # Original source list
                follow_up_list,     # Original follow-up list
                sorted_follow_up,   # Sorted follow-up list by mutant
                expected_output,    # Expected output
                result              # Result of comparison
            ])
    except Exception as e:
        # In case of error, treat the mutant as killed
        for (source_list, follow_up_list), expected_output in zip(test_cases, expected_outputs):
            results.append([
                mutant_name,
                source_list,
                follow_up_list,
                "Error",
                expected_output,
                f"Killed"
            ])

    return results

if __name__ == "__main__":
    # Collect results in a list for all mutants
    all_results = []

    # Loop over each mutant file (from m1 to m30)
    for i in range(1, 31):
        mutant_name = f"m{i}"
        results = run_tests_for_mutant(mutant_name, test_cases, expected_outputs)
        all_results.extend(results)
    #Display the result as table
    headers = ["Mutant", "Source List", "Follow-up List", "Mutant Outputs", "Expected Output", "Result"]
    print(tabulate(all_results, headers, tablefmt="grid"))
