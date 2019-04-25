#writing to an excel file
co.to_excel("Documents/AI/Pandas/new.xlsx", sheet_name="Main Data")

#removing indices
co.to_excel("Documents/AI/Pandas/new.xlsx", sheet_name="Main Data", index=False)

#customise staring rows & columns
co.to_excel("Documents/AI/Pandas/new.xlsx", sheet_name="Main Data", index=False, startrow=2, startcol=2)

#stock dataset via list
df_stocks = pd.DataFrame({
    'tickets': ['GOOGLE', 'WMT', 'MSFT'],
    'price': [346, 54, 90],
    'pe': [90.23,92.39, 44.42],
    'esp': [56.56, 65.90, 44.0]
})
df_stocks.head()

#weather dataset via list
df_weather = pd.DataFrame({
    'day': ['1/1/19', '1/2/19', '1/3/19'],
    'temperature': [38,35,29],
    'event': ['Rain', 'Sunny', 'Snow']
})
df_weather.head()

#write stock dataset & weather dataset in same excel sheet on different sheets
with pd.ExcelWriter('stock_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name='stocks')
    df_weather.to_excel(writer, sheet_name='weather')

