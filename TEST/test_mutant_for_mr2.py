import sys
import os
import importlib
from tabulate import tabulate

# Add the directory where the mutants are located to the system path
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MUTANTS'))
sys.path.insert(0, mutant_dir)

# Import the function to get expected outputs from mr2
from test_mr2 import get_mr_outputs

# Get the expected outputs from MR2
expected_outputs = get_mr_outputs()

# Test cases: original list (no extra number added)
test_cases = [
    [9, 13, 3],
    [7, 3, 6, 5],
    [8, 23, 25, 5],
    [8, 13, 16, 23],
    [16, 25, 28],
]

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
    results = []  # Store results for each test case

    try:
        # Import the odd_even_sort function for this mutant
        odd_even_sort = import_mutant(mutant_name)

        # Loop through all test cases
        for case, expected_output in zip(test_cases, expected_outputs):
            source_list = case

            # Sort the original source list
            sorted_source = odd_even_sort(source_list[:])  # Sort the original list

            # Compare the mutant's output with the expected output
            result = "Survived" if sorted_source == expected_output else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,
                sorted_source,
                expected_output,
                result
            ])
    except Exception as e:
        # In case of error, treat the mutant as killed and add the error message
        for case, expected_output in zip(test_cases, expected_outputs):
            source_list = case
            results.append([
                mutant_name,
                source_list,          # Source list
                "Error",              # Sorted list marked as error
                expected_output,      # Expected output
                f"Killed"
            ])

    return results

if __name__ == "__main__":
    # Collect results in a list for all mutants
    all_results = []

    # Loop over each mutant file (from m1 to m30)
    for i in range(1, 31):
        mutant_name = f"m{i}"  # Mutant file names (m1, m2, ..., m30)

        # Run tests for each mutant and collect the results
        results = run_tests_for_mutant(mutant_name, test_cases, expected_outputs)
        all_results.extend(results)  # Append all results from this mutant

    # Define table headers
    headers = ["Mutant", "Source List", "Mutant Outputs", "Expected Output", "Result"]

    # Display the results as a table
    print(tabulate(all_results, headers, tablefmt="grid"))
