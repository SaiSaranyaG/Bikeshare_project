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
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    cities_list = ('chicago', 'new york city', 'washington')
    while city not in cities_list:
        try:
            city = input("\nWould you like to see data for which of these countries," 
                            " Chicago, New York City or Washington?\n").lower()
            if not city or city not in cities_list:
                print("\nPlease choose any from the given three countries..")
        except:
            print("\nOops! Looks like the entered country name is not recognized. "
                  "Please try again..")

    # TO Do: get user input for type of filter required
    filter_choice = ''
    filter_list = ('month', 'day', 'both', 'none')

    while filter_choice not in filter_list:
        try:
            filter_choice = input("\nWould you like to filter the data by month, "
                                  "day, both or no filter? Type 'none'"
                                  "for no filter.\n")
            if not filter_choice or filter_choice not in filter_list:
                print("\nPlease choose any from the given filter options..")

        except:
            print("\nOops! Looks like the opted filter is not a valid one. Please "
                  "try again..")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'all'
    month_list = ["January", "February", "March", "April", "May", "June", "July"]
    if filter_choice in ('both', 'month'):
        while month not in month_list:
            try:
                month = input("\nWhich month? January, February, March, April, "
                              "May, June, or July.\n").title()
                if not month or month not in month_list:
                    print("\nPlease enter a valid month..")
            except:
                print("\nOops! Looks like the entered month is not a valid one. "
                      "Please try again..")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
                    "Saturday", "Sunday"]
    if filter_choice in ('both', 'day'):
        while day not in days_in_week:
            try:
                day = input("\nWhich day of the week? Monday, Tuesday, Wednesday, "
                            "Thursday, Friday, Saturday, Sunday.\n").title()

                if not day or day not in days_in_week:
                    print("\nPlease enter a valid weekday..")
            except:
                print("\nOops! Looks like the entered weekday is not valid. "
                      "Please try again..")

    if filter_choice is 'none':
        print("\nSeems like you want to analyze complete data...")

    print("\nThank you for providing your inputs.")
    print("Just a moment... loading the data...")
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ["January", "February", "March", "April", "May", "June", "July"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("Most Frequent Month : {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("Most Frequent Day_of_week : {}".format(popular_day_of_week))

    # TO DO: display the most common start hou
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    print("Most Frequent Start Hour: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("Most Popular Start Station: {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("Most Popular End Station: {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station'])['Trip Duration'].size().idxmax()
    print("\nMost popular trip is between")
    print("Start station: {}".format(popular_trip[0]))
    print("End Station: {}".format(popular_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time: {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Mean Travel Time: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("No gender data to share")

    print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        sorted_dob = df.sort_values('Birth Year')
        print("Earliest or oldest Birth Year: {}".\
        format(sorted_dob['Birth Year'].min()))

        print("Most recent or youngest Birth Year: {}".\
        format(sorted_dob['Birth Year'].max()))

        popular_dob = sorted_dob['Birth Year'].value_counts().idxmax()
        print("Most common year of birth: {}".format(popular_dob))
    else:
        print("No birth year to share")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, current_line):
    '''Displays Raw data is displayed upon request by the user.'''
    
    #TO DO: Display 5 lines of raw data based on user request
    user_req = ''
    req_choice = ['yes', 'no']
    while user_req not in req_choice:
        try:
            user_req = input("\nWould you like to view individual trip data?"
                             " Please type yes or no.\n").lower()
            if not user_req or user_req not in req_choice:
                print("\nPlease type yes or no..")
            
            if user_req != 'yes':
                break
            
            print("\nLoading requested data...\n")
            print(df.iloc[current_line:current_line+5])
            current_line += 5
            return display_data(df, current_line)
        except:
            print("I'm sorry, I'm not sure if you wanted to see more data or not. Please try again.")
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, 0)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nHope you had a great time analyzing {}'s bikeshare data... "
                  "Have a nice day!\n".format(city.title()))
            break


if __name__ == "__main__":
	main()
