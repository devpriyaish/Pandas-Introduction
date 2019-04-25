#simple reading
import pandas as pd
weather = pd.read_csv("nyc_weather.csv")
weather.head()

#Writing back to CSV File
#the data of nyc_weather is been transferred to new along with index
weather.to_csv('new.csv')

#Writing back to CSV File
#the data of nyc_weather is been transferred to new along without index
weather.to_csv('new.csv', index=False)

#returnes first column
weather.columns

#printing customised number of rows
weather.to_csv("new.csv", columns=['EST', 'Temperature', 'Events'])

#removing the headder from the file
weather.to_csv("new.csv", header=False)
