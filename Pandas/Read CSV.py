#simple reading
import pandas as pd
weather = pd.read_csv("nyc_weather.csv")
weather.head()

#when csv file has an extra header
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv")
weather.head()

#skiping number of rows
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", skiprows=1)
weather.head()

#making random rows as header
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", header=1)
weather.head()

#when csv file has no header at all
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", header=None)
weather.head()

#Providing a meaningful name if known to us
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", header=None, names=['EST', 'Temperature', 'DewPoint', 'Humidity', 'SLP'])
weather.head()

#Providing a meaningful name if known to us
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", names=['EST', 'Temperature', 'DewPoint', 'Humidity', 'SLP', 'VM', 'WS-'])
weather.head()

#Operation on original file
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv")
weather.head()

#when we have to print only some number of rows
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", nrows=4)
weather

#working on na values 
#how to replace NaN Values
#useful in cleaning the data
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", na_values=["Not Available","n.a."])
weather.head()

#cleaning data with na values
#giving the na values as list
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", na_values= ["Not Available",'T'])
weather.head(11)

#giving the na values as dictionary
weather = pd.read_csv("Documents/AI/Pandas/nyc_weather.csv", na_values = {
    'PrecipitationIn': ['T'],
    "Events": ["Not Available"]
})
weather.head(11)


