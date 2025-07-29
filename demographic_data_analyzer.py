import pandas as pd

def calculate_demographic_data():
    # Load data
    df = pd.read_csv("adult.csv")
    
    # Strip whitespace from all string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # 1. Number of each race represented in this dataset
    race_count = df['race'].value_counts()

    # 2. Average age of men
    men = df[df['sex'] == 'Male']
    average_age_men = men['age'].mean()

    # 3. Percentage with a Bachelor's degree
    bachelor_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = (bachelor_count / total_count) * 100

    # 4. Advanced education: Bachelors, Masters, Doctorate
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
    percentage_higher_edu_rich = (len(higher_edu_rich) / len(higher_edu)) * 100

    # 5. Without advanced education, percentage earning >50K
    lower_edu = df[~df['education'].isin(advanced_education)]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']
    percentage_lower_edu_rich = (len(lower_edu_rich) / len(lower_edu)) * 100

    # 6. Minimum hours per week
    min_hours = df['hours-per-week'].min()

    # 7. Percentage earning >50K among those who work minimum hours
    min_hour_workers = df[df['hours-per-week'] == min_hours]
    rich_min_hour_workers = min_hour_workers[min_hour_workers['salary'] == '>50K']
    percentage_rich_min_workers = (len(rich_min_hour_workers) / len(min_hour_workers)) * 100

    # 8. Country with highest % of people earning >50K
    country_earnings = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    highest_earning_country = country_earnings['>50K'].idxmax()
    highest_earning_percentage = country_earnings['>50K'].max() * 100

    # 9. Most common occupation in India for >50K earners
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_job_india = india_rich['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_higher_education': round(percentage_higher_edu_rich, 1),
        'percentage_lower_education': round(percentage_lower_edu_rich, 1),
        'min_work_hours': min_hours,
        'rich_percentage_min_hours': round(percentage_rich_min_workers, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_percentage, 1),
        'top_IN_occupation': top_job_india
    }

 













