import sys
import os
import importlib
from tabulate import tabulate
from test_cases_mr1 import test_cases

mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MUTANTS'))
sys.path.insert(0, mutant_dir)

from test_mr1 import get_mr_outputs

# Get the expected outputs from MR1
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
            # First sort the original source list
            sorted_source = odd_even_sort(source_list[:])  # Sort the original list (source test case)

            # Then sort the follow-up list
            sorted_follow_up = odd_even_sort(follow_up_list[:])  # Sort the follow-up list

            # Compare the mutant's output with the expected output
            result = "Survived" if sorted_follow_up == expected_output else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,  # Source list
                follow_up_list,  # Follow-up list
                sorted_follow_up,  # Mutant's output
                expected_output,  # Expected output
                result  # Result
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
    all_results = []

    # Loop over each mutant file (from m1 to m30)
    for i in range(1, 31):
        mutant_name = f"m{i}"
        results = run_tests_for_mutant(mutant_name, test_cases, expected_outputs)
        all_results.extend(results)  # Append all results from this mutant

    # Display result as table
    headers = ["Mutant", "Source List", "Follow-up List", "Mutant Outputs", "Expected Output", "Result"]
    print(tabulate(all_results, headers, tablefmt="grid"))
