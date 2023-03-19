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
    letter =['a','b','c']
    city_selection = input('To View the available bikeshare data ,Kindly type:\n The letter (a) for Chicago\n The letter (b) for New York City\n The letter (c) for Washington:\n').lower()
    while city_selection not in letter:
         city_selection = input('\n that\'s invalide input . To View the available bikeshare data ,Kindly type:\n The letter (a) for Chicago\n The letter (b) for New York City\n The letter (c) for Washington:\n').lower() 
    print(city_selection)       
    city_selections ={"a":"chicago","b":"new york city","c":"washington"}
    if city_selection in city_selections.keys():
         city=city_selections[city_selection]
    print(city)     
        
    months=['junuary','february','march','april','may','june']    
    month = input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\nFebruary\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()
    while month not in months:
        month=input('that\'s invalid choice, please type a valid month name or all. \n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\nFebruary\n-March\n-April\n-May\n-June\n-All\n\n:').format(city.title()).lower() 
    print(month)       
    
    #get user input for day of week (all,monday ,tuesday,...sunday)    
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day =input('\n\nTo filter {}\'s data by a particular day, please type the month name or all for not filtering by day: \n-monday\ntuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n-All\n\n:'.format(city.title())).lower()
    while day not in days:
        day=input('that\'s invalid choice, please type a valid day name or all.\n\nTo filter {}\'s data by a particular day, please type the month name or all for not filtering by day: \n-monday\ntuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n-All\n\n:'.format(city.title())).lower()
    print(day)
         
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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour 
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name 
    
    if month !='all':
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1
         df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\n The most common month:',common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\n The most common day:',common_day)

    # TO DO: display the most common start hour
    common_hour= df['hour'].mode()
    print('\n The most common hour:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()
    print('\n Most commonly used start station:',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station =df['End Station'].mode()
    print('\n Most commonly used end station:',common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    combine = common_start_station.append(common_end_station) 
    print('\n Combination of start station and end station:',combine)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print('\n Total travel time:',total_travel)

    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    print('\n Mean travel time:',mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts=df['User Type'].count()
    print('\n Counts of user types:',counts)

    # TO DO: Display counts of gender
    gender=df['Gender'].count()
    print('\n Counts of gender:',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    print('\n Earliest year of birth:',earliest)
    recent=df['Birth Year'].max()
    print('\n Most recent year of birth:',recent)
    most=df['Birth Year'].mode()
    print('\n Most common year of birth:',most)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    
    print('\n Raw data is available to check ...\n')
    display_raw =input('May you want to have alook on more raw data?Type yes or no \n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city] , chunksize=5):
                print(chunk)
                
                display_raw = 'May youwant to have alook on more raw data? Type yes or no'
                if display_raw != 'yes':
                    print('Thank You')
                    break
                break
        except KeyboaedInterrupt:
            print('Thank You.')
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
