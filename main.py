

from demographic_data_analyzer import calculate_demographic_data
import test_module

# Run analysis
results = calculate_demographic_data(print_data=True)

# Access individual values
print("\nAverage age of men:", results['average_age_men'])
print("Top occupation in India:", results['top_IN_occupation'])

# Run automated tests
print("\nRunning unit tests...")
test_module.run_tests()







