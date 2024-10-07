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
    while True:
       city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
       if city not in CITY_DATA.keys(): 
        print('You provided invalid city name')
       else:
          break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        
        month = input('Choose a month (or type "all" for all months): ').lower().strip()
    
        if month in months or month == 'all':
           break
        else:
            print('Try again.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days=['sunday' , 'monday'  , 'tuesday' , 'wednesday' , 'thursday' , 'friday' ,'saturday']
    while True:
        day=input('Choose a day (or type "all" for all day): ').lower().strip() #Using lower() converts input to lowercase to handle capital letters, strip() removes leading or trailing spaces to prevent errors if user write space before or after answer.
        
        if day in days or day == 'all':
          break
        else:
              print('try again')
                
    return city , month , day





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
    #convert city data to data frame 
    df=pd.read_csv(CITY_DATA[city])
    #convert start time to date type
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['month']=df['Start Time'].dt.month
    df['day name']=df['Start Time'].dt.day_name()
   

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 #Because Python uses zero-based indexing, adding +1 aligns month numbers with their corresponding values.
        
        df=df[df['month']==month]
    
    
    if day != 'all':
        df=df[df['day_of_week']== day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0] #added [0] with mode to return the the first most common value
    print('most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('most common day of week is: ', most_common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_c_hour=df['hour'].mode()[0]
    print('most common hour' , most_c_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_st = df['Start Station'].mode()[0]
    print("most commonly used start station", most_st)
    
    # TO DO: display most commonly used end station
    end_st = df['End Station'].mode()
    print("most commonly used end station", end_st)
    print('-'*40)
    # TO DO: display most frequent combination of start station and end station trip
    f_station = df['Start Station'] + ' to ' + df['End Station']
    popular_station=f_station.mode()[0]
    print('popular_station is:', popular_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    
    print("total travel time is:", total_travel_time)
    
    # TO DO: display mean travel time
    average_t_t=df['Trip Duration'].mean()
    print(f"Average of mean travel time is {average_t_t}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts()
    print(f"User Count is {user_counts}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: #Check if the gender column exists before accessing it to avoid errors while is not exist in the Washington data
          gender_counts=df[ 'Gender'].value_counts()
    print('gander count is : ' , gender_counts )

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
          year=df['Birth Year']
          earlist=year.min()
          recent=year.max()
          most=year.mode()[0]   
    print('earlist year of birth is: ' , earlist )
    print('recent year of birth is: ' , recent )
    print('common year of birth is: ' , most )

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def ask(df):
    current_inx=0
    user_input=input('do you want to return 5 rows? (yes or no): ').lower()
    while user_input == 'yes':
        rows = df.iloc[current_inx:current_inx + 5]  
        print(rows)
        current_inx += 5 
        for_next = input('Do you want the next 5 rows? (yes or no): ').lower()
        if for_next != 'yes':
            break
            

       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)  
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        user_stats(df)
        ask(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
