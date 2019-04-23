import pandas as pd
#taking a clean data
weather = pd.read_csv("weather_data_nyc_centralpark_2016(1).csv")
#prints initial few rows
weather.head()

#finds the maximum of 'maximum temperature'
weather['maximum temperature'].max()

#finds the minimum of 'maximum temperature'
weather['maximum temperature'].min()

#describes statistical data in the dataset
weather.describe()

#data where the average temperature is greater than 50
weather[weather['average temperature']>50]

#give me the data-row where average temperature is maximum
weather[weather['average temperature'] == weather['average temperature'].max()]

#print specific column in conditional statement
weather['date'][weather['minimum temperature'] == weather['minimum temperature'].min()]

#conditional statement with multiple columns
weather[['date', 'minimum temperature', 'snow fall']][weather['minimum temperature'] == weather['minimum temperature'].min()]

#prints the range of the index
weather.index

#sets the index to date
weather.set_index('date').head()

#sets the index to date permanently
weather.set_index('date', inplace=True)

#Access a group of rows and columns by label(s) or a boolean array.
weather.loc['5-1-2016']

#restoring the previous index
weather.reset_index(inplace=True)
weather.head()
