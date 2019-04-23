import pandas as pd
#taking a clean data
weather = pd.read_csv("weather_data_nyc_centralpark_2016(1).csv")
#prints initial few rows
weather.head()

#shows the number of rows & columns
weather.shape

#to initialize the shape with rows & columns
rows, columns = weather.shape

#prints rows
rows

#prints columns 
print(columns)

#prints last n rows
weather.tail(2)

#prints the range
weather[12:17]
#prints 12th row but not 17th

#prints number of columns
weather.columns

#printing the column details
weather.date.head()

#printing the columns details having indentation in therir names
weather['snow fall'].head()

#types of the columns in the dataset is generally of pandas series
type(weather['minimum temperature'])

#prints only a few columns
weather[['date','maximum temperature']].head()


