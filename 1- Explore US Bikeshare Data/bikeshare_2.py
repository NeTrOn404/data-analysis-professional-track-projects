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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid      inputs
    city = input('\n Enter which city from (chicago, new york city, washington):\n')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ('Make sure that you entered one of the above msg ').lower()


    # get user input for month (all, january, february, ... , june)
    month = input('\n Enter which month from(january :: december):\n')
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Make sure that you entered one of the above msg ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\n Enter which day from (saturday :: thrusday) \n').lower()


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
    # load data
    df = pd.read_csv(CITY_DATA[city])

    # convert the start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('common month :', df['month'].mode()[0])


    # display the most common day of week
    print('common week : ', df['day_of_week'].mode()[0])


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('common hour : ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('common S.station : ', df ['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('common E.station : ', df['End Station'].value_counts().idxmax())


    # display most frequent combination of start station and end station trip
    print('repeated combination of S.station and E.station trip')
    print('common_start_and_end_stations :',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Tot_T_T = sum(df['Trip Duration'])
    print('total travel time:', Tot_T_T/86400, " Days")

    # display mean travel time
    Mean_T_T = df['Trip Duration'].mean()
    print('mean travel time:', Mean_T_T/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
                
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)

    # Display earliest, most recent, and most common year of birth
    earliest_y = int(df['Birth Year'].min())
    recent_y = int(df['Birth Year'].max())
    common_y = int(df['Birth Year'].value_counts().idxmax())
    print("the earliest year of birth is:",earliest_y,", most recent one is:",recent_y,"and the most common       one is: ",common_y)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data (df):
    """Displays the data """
    print('press enter to see raw data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
