import sys
import os
import importlib
from tabulate import tabulate
from test_cases_mr2 import test_cases

# Add the directory where the mutants are located to the system path
mutant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mutants'))
sys.path.insert(0, mutant_dir)

# same test cases with mr2
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
    results = []

    try:
        # Import the odd_even_sort function for this mutant
        odd_even_sort = import_mutant(mutant_name)

        # Loop through all test cases
        for case in test_cases:
            source_list, add_number = case

            # Step 1: Sort the source input (SI)
            source_output = odd_even_sort(source_list[:])

            # Step 2: Prepare the follow-up list by adding 'add_number' to each element in the source input
            follow_up_input = [x + add_number for x in source_list]  # FI
            follow_up_output = odd_even_sort(follow_up_input.copy())  # FO

            # Step 3: Check if follow-up output equals source output + k for all elements
            is_survived = all(fo == so + add_number for fo, so in zip(follow_up_output, source_output))

            result = "Survived" if is_survived else "Killed"

            results.append([
                mutant_name,
                source_list,            # SI: Source input
                add_number,             # k: Number added to each element
                follow_up_input,        # FI: Follow-up input
                follow_up_output,       # Follow-up output
                [so + add_number for so in source_output],  # follow-up output (source output + k)
                result
            ])
    except Exception as e:
        # In case of error, it is killed mutant
        for case in test_cases:
            source_list, add_number = case
            follow_up_input = [x + add_number for x in source_list]  # Recalculate follow_up_input
            results.append([
                mutant_name,
                source_list,
                add_number,
                follow_up_input,
                "Error",
                "Error",
                "Killed"
            ])

    return results

if __name__ == "__main__":
    all_results = []

    for i in range(1, 31):
        mutant_name = f"m{i}"
        results = run_tests_for_mutant(mutant_name, test_cases)
        all_results.extend(results)

    # Display the results as a table
    headers = ["Mutant", "Source List", "Added Number", "Follow-up Input", "Follow-up Output", "Expected Output", "Result"]
    print(tabulate(all_results, headers, tablefmt="grid"))
