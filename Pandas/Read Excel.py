import pandas as pd

#reading excel file
co = pd.read_excel("Documents/AI/Pandas/cocubes data.xlsx", 'Sheet1')
co.head()

#working on functions & dictionary 
def convert_DiplomaBranch_cell(cell):
    if cell == 'n.a.':
        return 'Null Null'
    elif cell == 'not available':
        return 'Big Null'
    return cell

co = pd.read_excel("Documents/AI/Pandas/cocubes data.xlsx", "Sheet1", converters={
    'Diploma Branch' : convert_DiplomaBranch_cell
})
co.head()




