import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        try:
            city=input("Would you like to see data for Chicago, New York, or Washington?\n").title()
            city_list=["Chicago", "New York", "Washington"]
            if city in city_list:
                print("Thanks for selecting "+city)
                break
            else:
                print("You did not type the city name as shown in the list!")    
        except:
            print("\nYour input is invalid, please try again")
          
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            filter_selected=input("Would you like to filter the data by [month, day, or not at all]\n").lower()
            if filter_selected in ["month","day","not at all"]:
                print("Thanks for selecting "+filter_selected)
                break
            else:
                print("You did not type the correct filter as shown in the list!")    
        except:
            print("Your input is invalid, please try again")
   
            
    month_list=["January","February","March","April","May","June"]
    while filter_selected=="month":
        try:
            month=input("Which month? [January, February, March, April, May, or June]\n").title()
            if month in month_list:
                print("Thanks for selecting "+month)
                break
            else:
                print("You did not type the month name as shown in the list!")    
        except:
            print("\nYour input is invalid, please try again")
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    while filter_selected=="day":
        try:
            # day=input("Which day of the week? [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday]\n").title()
            if day in day_list:
                print("Thanks for selecting "+day)
                break
            else:
                print("You did not type the day name as shown in the list!")    
        except:
            print("\nYour input is invalid, please try again")

    if filter_selected=="month":
        day="all"
    elif filter_selected=="day":
        month="all"   
    elif filter_selected=="not at all":
        month="all" 
        day="all"
        print("Understanding you do not need a filter")
        
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
        months = ['January', 'February', 'March', 'April', 'May', 'June']
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

    # TO DO: display the most common month
    df['month']=df['Start Time'].dt.month
    most_common_month= df['month'].mode()[0]
    print("The most common month is: "+str(most_common_month))
   
    # TO DO: display the most common day of week
    df['day']=df['Start Time'].dt.day
    most_common_day= df['day'].mode()[0]
    print("The most common day is: "+str(most_common_day))
   
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_start_hour= df['hour'].mode()[0]
    print("The most common start hour is: "+str(most_common_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("The most common start station is: "+most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("The most common end station is: "+most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination']=df['Start Station']+"   to   "+df['End Station']
    most_common_combination_station=df['Station Combination'].mode()[0]
    print("The most common combination of start and end station trip is: "+ most_common_combination_station)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("The total travel time in seconds is: ",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("The mean travel time in seconds is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df["User Type"].value_counts()
    print("The counts of user types is:\n",user_type)
    print("\n")
    # TO DO: Display counts of gender
    if city!="Washington":
        gender_type=df["Gender"].value_counts()
        print("The counts of gender types is:\n",gender_type)
    # TO DO: Display earliest, most recent, and most common year of birth
        print("\n")
        earliest_birth_year=int(df["Birth Year"].min())
        print("The earliest year of birth is: ",earliest_birth_year)
        most_recent_birth_year=int(df["Birth Year"].max())
        print("The most recent year of birth is: ",most_recent_birth_year)
        most_common_birth_year=int(df["Birth Year"].mode()[0])
        print("The most common year of birth is: ",most_common_birth_year) 
    else:
        print("There are no gender or birth year data")
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data(df):
    """Display 5 rows of the data at a time"""
    
    answer=input("Would you like to see 5 lines of raw data? Enter yes or no:\n").lower()
    if answer == "yes":
        print("\nHere are the first 5 lines:\n", df.head())
       
        count_first_line=0
        count_fifth_line=4
        while True:
            answer_again=input("\nWould you like to see next 5 lines of raw data? Enter yes or no:\n").lower()
            if answer_again == "yes":
                count_first_line+=5
                count_fifth_line+=5
                print("\nHere are the next 5 lines:\n", df[count_first_line:count_fifth_line+1])  
            else:
                break
                    
        
def main():
    """restart the program"""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no:\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()