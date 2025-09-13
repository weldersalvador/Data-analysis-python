import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = pd.Series(df['race'].value_counts())

    mask_age_men = df['sex'] == 'Male'

    average_age_men = round(df[mask_age_men]['age'].mean(),1)

    mask_bachelors = df['education'] == 'Bachelors'

    percentage_bachelors = round(((len(df[mask_bachelors]) / len(df))*100),1)

    mask_higher = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')

    mask_rich_higher = (df['salary'] == '>50K') & (mask_higher)

    mask3 = (df['salary'] == '>50K') & ~(mask_higher)

    higher_education_rich = round((100 * len(df[mask_rich_higher]) / len(df[mask_higher])),1)

    lower_education_rich = round((len(df[mask3]) * 100 / len(df[~mask_higher])),1)

    min_work_hours = df['hours-per-week'].min()

    mask_rich_fewer = df['hours-per-week'] == min_work_hours

    mask_rich_and_fewer = (df['salary'] == '>50K') & mask_rich_fewer

    rich_percentage = round((len(df[mask_rich_and_fewer]) * 100 / len(df[mask_rich_fewer])),1)

    highest_earning_countries = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)

    highest_earning_country = highest_earning_countries.idxmax()

    mask_richest_earning_country = df['native-country'] == highest_earning_country

    mask_rich_in_country = (df['salary'] == '>50K') & mask_richest_earning_country
    
    highest_earning_country_percentage = round((len(df[mask_rich_in_country]) * 100 / len(df[mask_richest_earning_country])),1)

    mask_india = (df['salary'] == '>50K') & (df['native-country'] == 'India')
    top_IN_occupation = (df[mask_india]['occupation'].value_counts().idxmax())


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
