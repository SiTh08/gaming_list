import pyodbc
import requests

class Functions():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_gdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_gdb.cursor()

    def execute(self, query):
        return self.cursor.execute(query)

    def con_gdb(self):
        return self.con_gdb()

# As a user, I can create one game.

    def create(self, name, genre, platform, price, phone, location):
        query = f'INSERT INTO Games([Name], Genre, Platforms, Price, Phone, [Location]) VALUES ({name}, {genre}, {platform}, {price}, {phone}, {location})'
        self.execute(query)
        self.conn_gdb.commit()


# As a user, I can read all games.

    def readall(self):
        query_rows = self.execute('SELECT * FROM Games')
        while True:
            row = query_rows.fetchone()
            if row is None:
                break
            print('ID:', str(row[0]) + ', ' + 'Game name:', row[1] + ', ' + 'Genre:', row[2] + ', ' + 'Platform:', row[3] + ', ' + 'Price:', str(row[4]) + ', ' + 'Phone:', row[5] + ', ' + 'Location:', row[6] + ', ' + 'Latitude:', str(row[7]) + ', ' + 'Longitude:', str(row[8]))

    def readone(self, ID):
        query = self.execute(f"SELECT * FROM Games WHERE ID = {ID}")
        onegame = query.fetchone()
        print(onegame)

# Update functions

# Update game

    def updategame(self, ID, column1, value1):
        self.execute(f"UPDATE Games SET {column1} = {value1} WHERE ID = {ID}")
        self.conn_gdb.commit()

# Update longitude and latitude for a location

    def updatelongnlat (self, ID):
        query = self.execute(f"select [Location] from Games where ID = {ID}")
        postcode = query.fetchone()
        pc = ' '.join([row for row in postcode])
        url = 'http://api.postcodes.io/postcodes/'
        request_postcode = requests.get(url + pc)
        post_code_dict = request_postcode.json()
        details = post_code_dict
        latitude = details['result']['longitude']
        longitude = details['result']['latitude']
        self.execute(f"UPDATE Games SET Latitude = {latitude}, Longitude = {longitude} WHERE ID = {ID}")
        self.conn_gdb.commit()

    def updatelongnlat2 (self, name):
        query = self.execute(f"select [Location] from Games where [Name] = {name}")
        postcode = query.fetchone()
        pc = ' '.join([row for row in postcode])
        url = 'http://api.postcodes.io/postcodes/'
        request_postcode = requests.get(url + pc)
        post_code_dict = request_postcode.json()
        details = post_code_dict
        latitude = details['result']['longitude']
        longitude = details['result']['latitude']
        self.execute(f"UPDATE Games SET Latitude = {latitude}, Longitude = {longitude} WHERE [Name] = {name}")
        self.conn_gdb.commit()

# Delete a game.

    def deleteagame (self, ID):
        self.execute(f"DELETE FROM Games WHERE ID = '{ID}'")
        self.conn_gdb.commit()

# Add game to a text file.

    def writegametotxt (self, ID):
        query = self.execute(f"SELECT * FROM Games WHERE ID = {ID}")
        string = str(query.fetchone())
        try:
            with open('games.txt', 'w') as opened_file:
                opened_file.write(string)
        except FileNotFoundError:
            print('File not found.')













