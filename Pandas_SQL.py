import sqlite3
import pandas as pd

con = sqlite3.connect('test.db')

# https://www.w3schools.com/html/html_tables.asp

data = pd.read_clipboard()
data.head()

data.to_sql('Test_table', con)

data.head()

data.to_sql('Test_table', con, if_exists='replace')

pd.read_html('https://www.w3schools.com/html/html_tables.asp')
