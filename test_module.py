

import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

def run_tests():
    print("Running tests...\n")

    results = calculate_demographic_data(print_data=False)

    # 1. Race count test
    try:
        assert isinstance(results["race_count"], pd.Series)
        print("✔ Race count: PASSED")
    except AssertionError:
        print("✘ Race count: FAILED")

    # 2. Average age of men
    try:
        avg_age = results["average_age_men"]
        assert isinstance(avg_age, float) or isinstance(avg_age, int)
        print("✔ Average age of men: PASSED")
    except AssertionError:
        print("✘ Average age of men: FAILED")

    # 3. Percentage of people with Bachelors
    try:
        pct_bach = results["percentage_bachelors"]
        assert isinstance(pct_bach, float) or isinstance(pct_bach, int)
        print("✔ Percentage with Bachelors: PASSED")
    except AssertionError:
        print("✘ Percentage with Bachelors: FAILED")

    # 4. Higher education rich
    try:
        high_rich = results["higher_education_rich"]
        assert isinstance(high_rich, float) or isinstance(high_rich, int)
        print("✔ Higher education rich: PASSED")
    except AssertionError:
        print("✘ Higher education rich: FAILED")

    # 5. Lower education rich
    try:
        low_rich = results["lower_education_rich"]
        assert isinstance(low_rich, float) or isinstance(low_rich, int)
        print("✔ Lower education rich: PASSED")
    except AssertionError:
        print("✘ Lower education rich: FAILED")

    # 6. Minimum work hours
    try:
        min_hours = results["min_work_hours"]
        assert isinstance(min_hours, float) or isinstance(min_hours, int)
        print("✔ Minimum work hours: PASSED")
    except AssertionError:
        print("✘ Minimum work hours: FAILED")

    # 7. Rich percentage among min workers
    try:
        rich_pct = results["rich_percentage"]
        assert isinstance(rich_pct, float) or isinstance(rich_pct, int)
        print("✔ Rich % (minimum hours): PASSED")
    except AssertionError:
        print("✘ Rich % (minimum hours): FAILED")

    # 8. Highest earning country
    try:
        country = results["highest_earning_country"]
        pct_country = results["highest_earning_country_percentage"]
        assert isinstance(country, str) or country is None
        assert isinstance(pct_country, float) or isinstance(pct_country, int)
        print("✔ Highest earning country & percentage: PASSED")
    except AssertionError:
        print("✘ Highest earning country & percentage: FAILED")

    # 9. Top occupation in India
    try:
        occupation = results["top_IN_occupation"]
        assert isinstance(occupation, str) or occupation is None
        print("✔ Top occupation in India: PASSED")
    except AssertionError:
        print("✘ Top occupation in India: FAILED")

    print("\nAll tests completed.")

if __name__ == "__main__":
    run_tests()







