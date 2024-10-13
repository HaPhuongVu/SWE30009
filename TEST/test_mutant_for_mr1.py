import sys
import os
import importlib
from tabulate import tabulate

# Add the directory where the mutants are located to the system path
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MUTANTS'))
sys.path.insert(0, mutant_dir)

test_cases = [
    ([5, 10, 3], [10, 5, 3]),     # Reordered
    ([7, 8, 15], [15, 7, 8]),     # Reordered
    ([8, 20, 11, 9], [20, 11, 8, 9]),  # Reordered
    ([4, 1, 3], [3, 1, 4]),       # Reordered
    ([4, 8, 14, 3], [14, 3, 4, 8])  # Reordered
]

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
            source_list, follow_up_list = case

            # Step 1: Sort the source input (SI)
            source_output = odd_even_sort(source_list[:])  # Sort SI

            # Step 2: Sort the follow-up input (FI) which is a reordered SI
            follow_up_output = odd_even_sort(follow_up_list[:])  # Sort reordered FI

            # Step 3: The relation we are testing: sorted SI == sorted FI
            result = "Survived" if source_output == follow_up_output else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,          # Display original source input (SI)
                follow_up_list,       # FI before sorting (reordered SI)
                follow_up_output,     # FI after sorting
                source_output,        # Expected (same as sorted SI)
                result
            ])
    except Exception as e:
        # In case of error, treat the mutant as killed and add the error message
        for case in test_cases:
            source_list, follow_up_list = case
            results.append([mutant_name, source_list, follow_up_list, "Error", "Error", "Killed"])

    return results

if __name__ == "__main__":
    # Collect results in a list for all mutants
    all_results = []

    # Loop over each mutant file (from m1 to m30)
    for i in range(1, 31):
        mutant_name = f"m{i}"  # Mutant file names (m1, m2, ..., m30)

        # Run tests for each mutant and collect the results
        results = run_tests_for_mutant(mutant_name, test_cases)
        all_results.extend(results)  # Append all results from this mutant

    # Define table headers
    headers = ["Mutant", "Source Input", "Follow-up Input", "Follow-up Output", "Source Output", "Result"]

    # Display the results as a table
    print(tabulate(all_results, headers, tablefmt="grid"))
