import sys
import os
import importlib
from tabulate import tabulate

# Add the directory where the mutants are located to the system path
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mutants'))
sys.path.insert(0, mutant_dir)

# Get the expected outputs from MR2 then initialize it in here
expected_outputs = (
    [3, 9, 13],
    [3, 6, 5, 7],
    [5, 8, 23, 25],
    [8, 13, 16, 23],
    [16, 25, 38]
)

# Test cases: original list and number to be added
test_cases = [
    ([7, 11, 1], 2),  # k = 2
    ([6, 2, 5, 4], 1),  # k = 1
    ([3, 18, 20, 0], 5),  # k = 5
    ([4, 9, 12, 19], 4),  # k = 4
    ([13, 22, 35], 3),  # k = 3
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
            source_list, add_number = case

            # First sort the original source list
            sorted_source = odd_even_sort(source_list[:])  # Sort the original list (source test case)

            # Prepare the follow-up list by adding 'add_number' to each element in the source input
            follow_up_list = [x + add_number for x in source_list]
            sorted_follow_up = odd_even_sort(follow_up_list.copy())  # Sort the modified list (follow-up test case)

            # Compare the mutant's output with the expected output
            result = "Survived" if sorted_follow_up == expected_output else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,
                add_number,
                sorted_follow_up,
                expected_output,
                result
            ])
    except Exception as e:
        # In case of error, treat the mutant as killed and add the error message
        for case, expected_output in zip(test_cases, expected_outputs):
            source_list, add_number = case
            results.append([
                mutant_name,
                source_list,          # Source list
                add_number,           # Added number
                "Error",              # Sorted follow-up marked as error
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
    headers = ["Mutant", "Source List", "Added Number", "Mutant Outputs", "Expected Output", "Result"]

    # Display the results as a table
    print(tabulate(all_results, headers, tablefmt="grid"))
