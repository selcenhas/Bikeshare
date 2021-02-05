import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()

    while city not in CITY_DATA:
 
        print('Sorry that is not a valid input. Please try again.')
        city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month_responses = ["january", "february", "march", "april", "may", "june", "all"]
    month = input('Which month would you like to view data for? Please enter: january, february, march, april, may, june or all.\n').lower()

    while month not in valid_month_responses:
        print('Sorry that is not a valid input. Please Try again.')
        month = input('Which month would you like to view data for? Please enter: january, february, march, april, may, june or all.\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day_responses = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    day = input('Which day would you like to view data for? Please enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.\n').lower()

    while day not in valid_day_responses:
        print('Sorry that is not a valid input. Please Try again.')
        day = input('Which day would you like to view data for? Please enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.\n').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("Most Common Month:", common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print("Most Common day of week:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Start hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start= df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    common_end= df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['comb_station'] = df['Start Station'] + df['End Station']
    frequent_comb = df['comb_station'].mode()[0]

    print('The most popular start station is : ' + common_start)
    print('The most popular end station is : ' + common_end)
    print('The most frequent station trip is : ' + frequent_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = str((df['Trip Duration'].sum()) / 60)
    print('Total travel time: ' + total_travel)

    # TO DO: display mean travel time
    mean_travel = str((df['Trip Duration'].mean()) / 60)
    print('Mean travel time: ' + mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count= str(df['User Type'].value_counts().to_frame())
    print('Total user types: ' + user_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = str(df['Gender'].value_counts().to_frame())
        print('Total gender count: '+ gender_count)
    else:
        print("No gender data to share.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        common_birth = str(df['Birth Year'].mode()[0])
        earliest_birth = str(df['Birth Year'].min())
        recent_birth = str(df['Birth Year'].max())
        print('Common year of birth: ' + common_birth)
        print('Earliest year of birth: ' + earliest_birth)
        print('Most recent year of birth: ' + recent_birth)
    except:
        print('No such data available. Try another input')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows
    
    print_line = lambda char: print(char[0] * 90)
    
    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows
            print_line('.')
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
