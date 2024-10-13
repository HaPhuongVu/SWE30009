import sys
import os
import importlib
from tabulate import tabulate

# Add the directory where the mutants are located to the system path
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mutants'))
sys.path.insert(0, mutant_dir)

# Test cases: original list and number to be added (k)
test_cases = [
    ([7, 11, 1], 2),  # k = 2
    ([6, 2, 5, 4], 1),  # k = 1
    ([3, 18, 20, 0], 5),  # k = 5
    ([12,4,19,9], 4),  # k = 4
    ([35, 13, 22], 3),  # k = 3
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
            source_list, add_number = case

            # Step 1: Sort the source input (SI)
            source_output = odd_even_sort(source_list[:])  # Sort the original list (source test case)

            # Step 2: Prepare the follow-up list by adding 'add_number' to each element in the source input
            follow_up_input = [x + add_number for x in source_list]  # FI before sorting (modified source)
            follow_up_output = odd_even_sort(follow_up_input.copy())  # Sort the modified list (follow-up test case)

            # Step 3: Check if follow-up output equals source output + k for all elements
            is_survived = all(fo == so + add_number for fo, so in zip(follow_up_output, source_output))

            # Determine the result
            result = "Survived" if is_survived else "Killed"

            # Append detailed results to the list
            results.append([
                mutant_name,
                source_list,            # SI: Source input
                add_number,             # k: Number added to each element
                follow_up_input,        # FI: Follow-up input (before sorting)
                follow_up_output,       # Follow-up output (FI after sorting)
                [so + add_number for so in source_output],  # Expected follow-up output (source output + k)
                result
            ])
    except Exception as e:
        # In case of error, treat the mutant as killed and add the error message
        for case in test_cases:
            source_list, add_number = case
            follow_up_input = [x + add_number for x in source_list]  # Recalculate follow_up_input
            results.append([
                mutant_name,
                source_list,          # Source list
                add_number,           # Added number
                follow_up_input,      # Follow-up input (before sorting)
                "Error",              # Follow-up output marked as error
                "Error",              # Expected output marked as error
                "Killed"              # Mark as killed
            ])

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
    headers = ["Mutant", "Source List", "Added Number", "Follow-up Input", "Follow-up Output", "Expected Output", "Result"]

    # Display the results as a table
    print(tabulate(all_results, headers, tablefmt="grid"))
