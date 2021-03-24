import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def check_input(input_str,input_type):
    while True:
        input_read=input(input_str).lower()
        try:
            if input_read in ['chicago','new york city','washington'] and input_type==1:
                break
            elif input_read in ['january','february','march','april','may','june','all'] and input_type==2:
                break
            elif input_read in ['sunday','monday', 'tuesday','wednesday','thursday','friday','saturday','all'] and input_type==3:
                break
            else:
                if input_type==1:
                    print("Sorry we are not able to get user input for city, please input either chicago, new york city, washington")
                if input_type==2:
                    print("Sorry we were not able to get the name of the month to analyze data, Please input either 'all' to apply no month filter or january, february, ... , june")
                if input_type==3:
                    print("Sorry we were not able to get the name of the day to analyze data, Please input either 'all' to apply no day filter or saturday, sunday, ... , friday")

        except ValueError:
            print('Sorry Error Input')
    return input_read

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city chicago, new york city,and washington. HINT: Use a while loop to handle invalid inputs
    city=check_input("Would you like to see the data for chicago, new york city or washington?",1)
    month=check_input("Which Month (all, january, ... june)?",2)
    day=check_input("Which day? (all, monday, tuesday, ... sunday)",3)
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

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by (month) if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by (month) to create the new dataframe
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
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', popular_day_of_week)
    popular_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time=time.time()
    print(df['Start Station'].mode()[0])
    print(df['End Station'].mode()[0])
    group_field= df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)

    print('Most frequent combination of start station and end station trip:\n', popular_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print(df['Trip Duration'].sum())
    print(df['Trip Duration'].mean())

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(df['User Type'].value_counts())
    if city !='washington':
        print(df['Gender'].value_counts())
        print(df['Birth Year'].mode()[0])
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    def data(df):
        raw_data = 0
        while True:
            answer = input("Do you want to see the raw data? Yes or No").lower()
            if answer not in ['yes', 'no']:
                answer = input("You wrote the wrong word. Please type Yes or No.").lower()
            elif answer == 'yes':
                raw_data += 5
                print(df.iloc[raw_data : raw_data + 5])
                again = input("Do you want to see more? Yes or No").lower()
                if again == 'no':
                    break
                elif answer == 'no':
                    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
