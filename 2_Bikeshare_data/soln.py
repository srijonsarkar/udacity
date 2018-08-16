# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:12:44 2018

@author: srijon sarkar
"""

import pandas as pd
import time


def extract():
    '''
        This function takes the name of the city from the user
        and then extracts the data from the csv file from its location
        It then asks the user if they want to filter the database according
        to a particular day or month. It then returns the database to the
        main() along with the city name, month and day according to which it
        will be filtered
    
    '''
    while True:
        str1 = input("Enter the name of the city you'd like to get info about(Washington, New York, Chicago) : ")
        city = str1.lower()
        valid_city = ['washington', 'new york', 'chicago']
        if city in valid_city:
            break
        else:
            print('Invalid city name.....Please enter again!!')
            continue
        
    while True:
        str2 = input("Would you like the data to be filtered by single month(january-june) or not filtered at all(all)? : ")
        valid_month = ['january', 'february', 'march','april', 'may', 'june', 'july', 'all']
        month = str2.lower();
        if month in valid_month:
            break
        else:
            print("You have not entered the correct month/all as input, please try again")
            continue
            
    while True:
        str3 = input("Would you like the data to be filtered by day(Monday-Sunday) or no filter(all)? : ")
        valid_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = str3.lower()
        if day in valid_day:
            break
        else:
            print('Day mentioned is incorrect, please give corect input')
            continue
    
    if city == 'washington':
        df = pd.read_csv('washington.csv')            
                
    elif city == 'new york':
        df = pd.read_csv('new_york_city.csv')            
        
    else:
        df = pd.read_csv('chicago.csv')            
        
        
    df.dropna(axis=0, inplace=True)####to drop rows having NaN values
        
        
    #print(df.head(10))
    #print('*'*40)
    #print('*'*40)
    
    return df, day, month, city


def findDuration(x):    ####finds the trip time in terms of days, hours and minutes
    
    try:
        if x > 24*60*60:#####if trip was for multiple days
            u = int(x/(24*60*60))####no. of days
            v = int((x - u*24*60*60)/(60*60)) ####no. of hours
            w = int((x - u*24*60*60 - v*60*60)/60) #####no. of minutes
            return str(u)+" days "+str(v)+" hours " + str(w)+" minutes"
        elif x > 60*60:
            v = int((x)/(60*60)) ####no. of hours
            w = int((x - v*60*60)/60)####no. of minutes
            return str(v)+" hours " + str(w)+" minutes " + str(x - v*60*60 - w*60) + " seconds."
        else:
            w = int((x)/60)
            return str(w)+" minutes "+str(x-60*w)+" seconds."
    except TypeError:
        return ""
    
'''
def findDay(x):             ####find the day if city is chicago or new york, DD-MM-YYYY
    try:
        year = int(x.split('-')[2])
        month= int(x.split('-')[1])
        date = int(x.split('-')[0])
        t = datetime.date(year, month, date)
                
        return t.strftime("%A")
    
    except ValueError:
        return ""

def findDayW(x):       ####find the day if city is washington, since date format is different(YYYY-MM-DD)
    try:
        year = int(x.split('-')[0])
        month= int(x.split('-')[1])
        date = int(x.split('-')[2])
        t = datetime.date(year, month, date)
        return t.strftime("%A")
        
    
    except ValueError:
        return ""
'''
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    ####most common start station
    popularStart = df['Start Station'].mode()
    print("Most common start station is " + popularStart)
            
    ####most common end station
    popularEnd = df['End Station'].mode()
    print("Most common end station is " + popularEnd)
            
    ####most popular combination of start and end station    
    popular = pd.Series( df['Start Station'] + df['End Station'] ).mode();
    print("Common start and end station is : " + popular)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    ####total travel time
    totalTime = df['Trip Duration'].sum()
    print("Total travel time is "+ findDuration(totalTime))

    
    ####average travel time
    avgTime = df['Trip Duration'].mean()
    print("Average time is " + findDuration(avgTime))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    ####find count of type of user types
        
    print("Types of users is " + str(df['User Type'].value_counts()))
        
    try:
        print("Counts of gender is " + str(df['Gender'].value_counts()))
        
        print("Most common year of birth is " + str(int(df['Birth Year'].mode())))
        
        print("Earliest birth year is "+str(int(df['Birth Year'].min()))+" most recent birth year is " + str(int(df['Birth Year'].max())))
        
    
    except KeyError:
    
        print("No gender and birth year info available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    
    i=0
    j=5
    t = input("Would you like to view first 5 rows of the dataset?")
    while t.lower()=='yes':
        print(df.iloc[ i:j, :])
        t = input("Would you like to next 5 rows of the dataset?")
        i += 5
        j +=5
   
    

def main():
    
    while True:
    
        df, day, month, city = extract()
        
        if day!='all' and month!='all':
            print('Dataset is to be filtered by : '+ month +' and '+ day)
        elif month!='all':
            print('Dataset is to be filtered by : '+ month )
        elif day!='all':
            print('Dataset is to be filtered by : '+ day)
        
        
        #now we need to filter the dataset according to month and day, as specified
        #first split Start Time into date and time
        
        #print(df.head(10))
              
        df['Date'] = df['Start Time'].str.split(' ').str.get(0)
        df['Time'] = df['Start Time'].str.split(' ').str.get(1)
        
        #now extract the month number of the year from date
        df['Month'] = df['Date'].str.split('-').str.get(1)
        
        
               
        #now translate the month from number to name
        lmonths = pd.Series([ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        df['Month'].astype(str);
        df['Month'] = df['Month'].apply(lambda x : lmonths[int(x)-1])
        
        
        #create new column for exact duration in terms of days, hours and minutes
        #findDuration is the function
        #not required though :)
        df['Exact Duration'] = df['Trip Duration'].apply(findDuration)
        
        
        
        #create new column for day of the week
        #findDay returns the day of the week for any date
        
        df['Day'] = pd.to_datetime(df['Start Time'])
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        df['Day of Week'] = df['Day'].apply( lambda x : days[x.weekday()] )

        #if city!='chicago':   ####as chicago dataset has different format of date, we need a different function for extracting the day
        #    df['Day'] = df['Day'].apply( lambda x : day[x.weekday()] )
        #else:
        #    df['Day'] = df['Date'].apply(findDayW)
        
        
        print('After extracting day and month')
        
        print('*'*30)
        print(df.head(10))
        print('*'*30)
        
        print('In '+city+' most popular day is ' + df['Day of Week'].mode() + ' and popular month is ' + df['Month'].mode())
        
        #now apply the filters of day and month
        #first doing for the day
        if day!='all':
            df = df[ df['Day of Week'].apply( lambda x : x.lower() == day)]
                   
        if month!='all':
            df = df[ df['Month'].apply( lambda x : x.lower() == month)]
        
        print('*'*30)
        print(df.head(10))
        print('*'*30)
        
        ####most common hour
        popularHour = pd.Series(df['Time'].str.split(':').str.get(0)).mode()
        print("Most common hour is " + popularHour)
        
        
        station_stats(df)
        
        trip_duration_stats(df)
        
        user_stats(df)      
        
        display_data(df)
        
        ####last statement to be executed to be checked in while loop
        y = input('Would you like to try again? (Yes/No) ')
        if y.lower()=='yes':
            continue
        else:
            break
        
if __name__ == "__main__":
    main()
    
