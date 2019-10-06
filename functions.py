import pyodbc
import requests

class functions():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_rdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_rdb.cursor()

    def execute(self, query):
        return self.cursor.execute(query)

# As a user, I can create one game.

    def create(self, name, genre, platform, price, phone, location):
        query = f'INSERT INTO Games([Name], Genre, Platforms, Price, Phone, [Location]) VALUES ({name}, {genre}, {platform}, {price}, {phone}, {location})'
        self.execute(query)
        self.conn_rdb.commit()


# As a user, I can read all games.

    def readall(self):
        query_rows = self.execute('SELECT * FROM Games')
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print('ID:', str(row[0]) + ', ' + 'Game name:', row[1] + ', ' + 'Genre:', row[2] + ', ' + 'Platform:', row[3] + ', ' + 'Price:', str(row[4]) + ',  ' + 'Phone:', row[5] +  'Location:', row[6] + ', ' + 'Latitude:', row[7] + ', ' + 'Longitude:', row[8])


    


