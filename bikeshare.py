import time
import pandas as pd
import numpy as np

"""
*** Global variables ***
    Ths section declares global variables that will be used
    for the whole scope of the program.
"""
#this global variable will be used to keep a global scope variable with the city filtered by.
selected_city = ''

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#building MONTH dictionary to convert month numbers into month names
MONTH_DATA = { '1': 'January',
               '2': 'February',
               '3': 'March',
               '4': 'April',
               '5': 'May',
               '6': 'June'}

#building DAY dictionary to convert day numbers into day of the week names
DAY_DATA = { '1': 'Monday',
             '2': 'Tuesday',
             '3': 'Wednesday',
             '4': 'Thursday',
             '5': 'Friday',
             '6': 'Saturday',
             '7': 'Sunday'}

HOUR_DATA = {'1': '1 am', '2': '2 am', '3': '3 am', '4': '4 am',
             '5': '5 am', '6': '6 am', '7': '7 am', '8': '8 am',
             '9': '9 am', '10': '10 am', '11': '11 am', '12': '12 pm',
             '13': '1 pm', '14': '2 pm', '15': '3 pm', '16': '4 pm',
             '17': '5 pm', '18': '6 pm', '19': '7 pm', '20': '8 pm',
             '21': '9 pm', '22': '10 pm', '23': '11 pm', '0': '12 am'}

def validate_city(city):
    """
    Validates that the city entered by the user is one of the 6 valid options.
    Valid options: 'chicago', 'new york city', 'washington', 'chi', 'nyc', 'wha'

    Returns:
        TRUE if the user input is one of the 6 valid options
        FALSE if the user input is NOT one of the 6 valid options
    """
    if city in ['chicago', 'new york city', 'washington', 'chi', 'nyc', 'was']:
        return True
    else:
        return False

def convert_city(city):
    """
    Converts the city entered by the user into the final city name

    Returns:
        Chicago, New York City OR Washington
    """
    if city in ['chicago', 'chi']:
        return 'chicago'
    elif city in ['new york city', 'nyc']:
        return 'new york city'
    else:
        return 'washington'

def get_month_name(month):
    """
    This function takes a month number (1-6) as a parameter and
    returns the full name of the month

    Returns:
        (str) month - full name of the month
    """
    #Returns the name of the month by getting the value from the MONTH_DATA    dictionary
    for item in MONTH_DATA:
        if int(item) == month:
            return MONTH_DATA[item]

def get_hour_ampm(hour):
    """
    This function takes an hour number (0-23) as a parameter and
    returns the hour equivalent in a am/pm format

    Returns:
        (str) hour - am/pm format of hour
    """
    #Returns the name of the month by getting the value from the MONTH_DATA    dictionary
    for item in HOUR_DATA:
        if int(item) == hour:
            return HOUR_DATA[item]

def ask_month():
    """
    This function captures the month that the user wants to filter by.
    Also, this function validates that the input is a valid entry

    Returns:
        (str) month - month to filter by
    """

    #validating if the month entry is valid
    while True:
        month = input('\nEnter the number of the month you would like to filter by (1=January, 2=February, 3=March, 4=April, 5=May or 6=June): ')

        if month in ['1','2','3','4','5','6']:
            break

    return month

def ask_day():
    """
    This function captures the day that the user wants to filter by.
    Also, this function validates that the input is a valid entry

    Returns:
        (str) day - month to filter by
    """
    #validating if the day entry is valid
    while True:
        day = input('\nEnter the number of the day you would like to filter by (1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 7=Sun): ')

        if day in ['1','2','3','4','5','6','7']:
            break

    return day

def convert_seconds_to_hours(seconds):
    """
    NOTE: the main idea of this function was copied from "Geeks For Geeks" website
    URL: 'https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/'

    This function converts a given number of seconds and returns.
    the equivalent in Hours:Minutes:seconds

    Parameter: (int) seconds
    Returns:
        (str) hours:minutes:seconds
    """
    seconds = seconds % (24 * 3600)
    hour = seconds//3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def ask_restart():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        restart = input('\nWould you like to perform another calculation? (Y/N) ')

        if restart in ['Y','y','N','n']:
            break

    if restart in ['Y', 'y']:
        return 'y'
    else:
        return 'n'

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n')
    print('*'*44)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('*'*44)


    # Asking user to enter a city to filter by. This while loops makes sure that user enters a valid city
    while True:
        city_entry = input('\nPlease select the city you would like to see data from (Chicago/chi, New York City /nyc, Washington/was): ')

        if validate_city(city_entry.lower()):
            break

    #converting city entry name into the final city name (Chicago, New York City, Washington)
    city = convert_city(city_entry.lower())

    #changing the value of the global variable selected city
    global selected_city
    selected_city = city


    #Giving the user a choice to select a time filter in general
    #This while loop makes sure that the user enters either Y or N.
    while  True:
        time_filter = input('\nWould you like to apply any type of time filter? (Y/N): ')

        if time_filter in ['Y','y','N','n']:
            break


    if time_filter in ['Y', 'y']:

        #Once we know the user wants a time filter, ask the specific type (month, day or both)
        #This while loop make sure that the user enters the correct option for the time filter
        while True:
            type_filter = input('\nWhat type of filter would you like? (Please select a number  1 = Month, 2 = Day, 3 = Both): ')

            if type_filter in ['1', '2', '3']:
                break

        #If User selected filtering JUST filtering by Month
        if type_filter == '1':

            month = ask_month()
            #assigning day='-' to indicate that user does NOT want to filter by day
            day = 0

        #if user selected filtering JUST by Day
        elif type_filter == '2':

            #assigning month='-' to indicate that user does NOT want to filter by month
            month = 0
            day = DAY_DATA[ask_day()]

        #If user selected filtering by BOTH Month and Day
        else:
            month = ask_month()
            day = DAY_DATA[ask_day()]

    #if user selecs NO TIME FILTER, assign the null value to the variables month and day
    else:
        month = 0
        day = 0

    #print('-'*40)
    #print("City: {}, Month: {}, Day: {}".format(city, month, day))

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
    #Loading the correct data file, based on the city selected.
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour_of_day'] =  df['Start Time'].dt.hour


    #print(df['Start Time'].dt.month)
    #print(df['Start Time'].dt.weekday_name)

     # filter by month if applicable
    if month != 0:

        # filter by month to create the new dataframe
        df = df[df['month'] == int(month)]
        #print(df)

    # filter by day of week if applicable
    if day != 0:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\n')
    print('*'*48)
    print('Calculating The Most Frequent Times of Travel...')
    print('*'*48)

    start_time = time.time()

    ### Calculates the most common month
    common_month = df['month'].mode()

    month = get_month_name(common_month[0])

    print('\nThe most common month is: {}'.format(month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print("\nThe most common day is: {}".format(common_day[0]))

    # TO DO: display the most common start hour
    common_hour = df['hour_of_day'].mode()

    hour = get_hour_ampm(common_hour[0])
    print("\nThe most common hour is: {}".format(hour))


    print('\n')
    print('-'*34)
    print("This calculation took %s seconds." % round((time.time() - start_time),1))
    print('-'*34)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n')
    print('*'*49)
    print('Calculating The Most Popular Stations and Trip...')
    print('*'*49)
    start_time = time.time()

    # Displays most commonly used start station
    common_start_station = df['Start Station'].mode()

    print("\nThe most common start station is: {}".format(common_start_station[0]))


    # Displays most commonly used end station
    common_end_station = df['End Station'].mode()

    print("\nThe most common end station is: {}".format(common_end_station[0]))


    #Displays most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + ' TO: ' + df['End Station']).mode()

    print ('\nThe most frequent combination of start and end station is FROM: {}'.format(common_start_end_station[0]))
    #print (df['End Station'])


    print('\n')
    print('-'*34)
    print("This calculation took %s seconds." % round((time.time() - start_time),1))
    print('-'*34)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n')
    print('*'*28)
    print('Calculating Trip Duration...')
    print('*'*28)
    start_time = time.time()

    # Displays total travel time and converts total seconds into hh:mm:ss
    seconds = df.sum(axis=0)[2]
    formated_time = convert_seconds_to_hours(seconds)
    print("\nThe total travel time is: {} (hh:mm:ss). ({} seconds)".format(formated_time, round(seconds,1)))


    # Displays mean travel time and converts total seconds into hh:mm:ss
    mean_travel_time = df['Trip Duration'].mean()
    mean_converted = convert_seconds_to_hours(mean_travel_time)
    print("\nThe mean travel time is: {} (hh:mm:ss). ({} seconds)".format(mean_converted, round(mean_travel_time,1)))


    print('\n')
    print('-'*34)
    print("This calculation took %s seconds." % round((time.time() - start_time),1))
    print('-'*34)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n')
    print('*'*25)
    print('Calculating User Stats...')
    print('*'*25)
    start_time = time.time()

    #Displays summary of user types

    user_types = df['User Type'].value_counts()

    print('\nUser Type Summary:')
    for user_type, count in user_types.items():
        print('- {}   |   Total: {}'.format(user_type, count))


    #Validates that the city is either chicago or NYC... don't run this section for Washington
    if selected_city in ['chicago', 'new york city']:
        user_gender = df['Gender'].value_counts()

        #Displays the summary of Gender data
        print('\nUser Gender Summary:')
        for user_gender_idx, count in user_gender.items():
            print('- {}   |   Total: {}'.format(user_gender_idx, count))

        #Displays earliest, most recent, and most common year of birth
        print ('\nThe oldest birth year is: {}'.format(int(df['Birth Year'].min())))

        print ('\nThe most recent birth year is: {}'.format(int(df['Birth Year'].max())))

        print ('\nThe most common birth year is: {}'.format(int(df['Birth Year'].mode())))

    #This section is for when the city selected is Washington
    else:
        print ('\nNOTE: Gender and birth year information is not available for Washigton users.')


    print('\n')
    print('-'*34)
    print("This calculation took %s seconds." % round((time.time() - start_time),1))
    print('-'*34)

def display_raw_data(df):

    """ Your docstring here """
    i = 0

    # TO DO: convert the user input to lower case using lower() function
    while True:

         raw = input("\nWould you like to see raw data? (y/n)").lower()

         if raw in ['y', 'n']:
            break

    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'n':
            break
        elif raw == 'y':
            #slices the dataframe in chunks of 5 rows to display next five rows
            df_5_rows = df.iloc[i:i+5]

            print('\n')
            for index, row in df_5_rows.iterrows():
                print('Index: {}'.format(row[0]))
                print('Start Time: {}'.format(row['Start Time']))
                print('End Time: {}'.format(row['End Time']))
                print('Trip duration: {}'.format(row['Trip Duration']))
                print('Start Station: {}'.format(row['Start Station']))
                print('End Station: {}'.format(row['End Station']))
                print('User Type: {}'.format(row['User Type']))
                if (selected_city != 'washington'):
                    print('Gender: ', row['Gender'])
                    print('Birth Year', row['Birth Year'])
                print('\n')

            #asks user if another 5 rows are needed
            raw = input("Would you like to see 5 more rows? (y/n)").lower()

            #Increases the counter to 5 more rows
            i += 5
        else:
            raw = input("\nInvalid entry. Please enter (y/n)").lower()


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        #The following section makes the calls for all functions  that perform all calculations and data raw display
        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        display_raw_data(df)

        restart = ask_restart()
        if restart == 'n':
            break



if __name__ == "__main__":
	main()
