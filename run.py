from functions import *

server = 'localhost,1433'
database = 'Gaming_list'
username = 'SA'
password = 'Passw0rd2018'

games = functions(server, database, username, password)

# games.create("'Metal Gear Solid 3'", "'Shooter'", "'PS2'", 15.99, "'07507364747'", "'HR5 3RU'" )

games.readall()

# games.readone(5)

# games.updategame(5, "Price", 20)

# games.updatelongnlat(7)

# games.updatelongnlat2("'God of War'")

# games.deleteagame(5)

# games.writegametotxt(1)
