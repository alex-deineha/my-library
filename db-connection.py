import pyodbc
import pandas as pd 

def connect_db():
    print('Data source: conecting to DB...')
    server = 'rapindustry.ai, 11433'
    database = 'rap_db'
    username = "Tupac"
    password = 'Shakur'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server + 
                          '; DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print('Data source: ...connected to DB.')
    return cnxn, cursor

def close_db(cnxn, cursor):
    cursor.close()
    cnxn.close()
    print('Data source: close connection.')
        
query = '''SELECT * FROM table'''
    
def get_data():
    cnxn, cursor = connect_db()
    data = pd.read_sql_query(sql=query, con=cnxn)
    close_db(cnxn, cursor)
    return data
