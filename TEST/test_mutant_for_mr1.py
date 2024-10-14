import sys
import os
import importlib
from tabulate import tabulate
from test_cases_mr1 import test_cases

# directory of the mutants file
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MUTANTS'))
sys.path.insert(0, mutant_dir)

#same test case with MR1
test_cases = test_cases

def import_mutant(mutant_name):
    """
    Dynamically import the odd_even_sort function from the mutant module.
    :param mutant_name: The name of the mutant file (e.g., 'm1', 'm2').
    :return: The odd_even_sort function from the mutant.
    """
    mutant_module = importlib.import_module(mutant_name)
    return mutant_module.odd_even_sort

def run_tests_for_mutant(mutant_name, test_cases):
    """ Run all test cases for a given mutant and return the detailed result """
    results = []  # Store results for each test case

    try:
        # Import the odd_even_sort function for this mutant
        odd_even_sort = import_mutant(mutant_name)

        # Loop through all test cases
        for case in test_cases:
            source_input, follow_up_input = case

            # Step 1: Sort the source input (SI)
            source_output = odd_even_sort(source_input[:])  # Sort SI

            # Step 2: Sort the follow-up input (FI) which is a reordered SI
            follow_up_output = odd_even_sort(follow_up_input[:])  # Sort reordered FI

            # Step 3: The relation we are testing: sorted SI == sorted FI
            result = "Survived" if source_output == follow_up_output else "Killed"

            results.append([
                mutant_name,
                source_input,          # Source Input
                follow_up_input,       # Follow-up Input
                follow_up_output,     # Follow-up Output
                source_output,        # Source Output
                result
            ])
    except Exception as e:
        # In case of error, it is killed mutant
        for case in test_cases:
            source_input, follow_up_input = case
            results.append([mutant_name, source_input, follow_up_input, "Error", "Error", "Killed"])

    return results

if __name__ == "__main__":
    # Collect results in a list for all mutants
    all_results = []

    # Loop over each mutant file (1 to 30)
    for i in range(1, 31):
        mutant_name = f"m{i}"
        results = run_tests_for_mutant(mutant_name, test_cases)
        all_results.extend(results)

    # Display the results as a table
    headers = ["Mutant", "Source Input", "Follow-up Input", "Follow-up Output", "Source Output", "Result"]
    print(tabulate(all_results, headers, tablefmt="grid"))
