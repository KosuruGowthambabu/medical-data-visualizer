import pandas as pd

def calculate_demographic_data(print_data=True):
    # Column names
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "salary"
    ]

    # Load dataset
    df = pd.read_csv("adult.data.csv", header=None, names=columns)

    # Strip whitespace from string columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Convert numeric columns
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["hours-per-week"] = pd.to_numeric(df["hours-per-week"], errors="coerce")

    # 1. Count of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Higher vs Lower education rich
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round((higher_education["salary"] == ">50K").mean() * 100, 1)
    lower_education_rich = round((lower_education["salary"] == ">50K").mean() * 100, 1)

    # 5. Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # 6. Percentage of rich among minimum hour workers
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers["salary"] == ">50K").mean() * 100, 1) if not min_workers.empty else 0

    # 7. Highest earning country
    country_salary = (
        df[df["salary"] == ">50K"]["native-country"].value_counts()
        / df["native-country"].value_counts()
        * 100
    )
    if not country_salary.empty:
        highest_earning_country = country_salary.idxmax()
        highest_earning_country_percentage = round(country_salary.max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0

    # 8. Top occupation in India among >50K earners
    india_high_earners = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"]
    if india_high_earners.empty:
        top_IN_occupation = None
    else:
        mode_series = india_high_earners.mode()
        top_IN_occupation = mode_series.iloc[0] if not mode_series.empty else None

    # Print results
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Minimum work hours per week:", min_work_hours)
        print("Rich % (min hours):", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }


if __name__ == "__main__":
    calculate_demographic_data()
