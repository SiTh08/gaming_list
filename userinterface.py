from run import *

print('Welcome to games listing! What would you like to do?')

while True:
    print('Option 1: Add a game to the listing.')
    print('Option 2: View all games.')
    print('Option 3: View one game.')
    print ('Exit.')
    userinput = input('Which option would you like to choose? ').strip().lower()

    if userinput == 'option 1':
        gamename = input('What is your game called?').strip()
        genre = input('What is the genre of the game?').strip()
        platform = input('How can you play the game?').strip()
        price = input('How much does the game cost?').strip()
        phone = input('What is your phone number?').strip()
        location = input('What is your postcode?').strip()
        edprice = float(price)
        games.create("'{}'".format(gamename), "'{}'".format(genre), "'{}'".format(platform), "'{}'".format(edprice), "'{}'".format(phone), "'{}'".format(location))
        games.updatelongnlat2("'{}'".format(gamename))
        print(f'{gamename} has been added.')
        more = input('Would you like to do anything else? ').strip().lower()
        if more == 'yes':
            continue
        elif more == 'no':
            break
        else:
            print('Please annswer with yes or no.')
            more = input('Would you like to do anything else? ').strip().lower()
            if more == 'yes':
                continue
            elif more == 'no':
                break

    elif userinput == 'option 2':
        games.readall()
        more = input('Would you like to do anything else? ').strip().lower()
        if more == 'yes':
            continue
        elif more == 'no':
            break
        else:
            print('Please annswer with yes or no.')
            more = input('Would you like to do anything else? ').strip().lower()
            if more == 'yes':
                continue
            elif more == 'no':
                break


    elif userinput == 'option 3':
        pickID = input('What is the ID of the game you would like to view? ')
        games.readone(pickID)
        more = input('Would you like to do anything else? ').strip().lower()
        if more == 'yes':
            continue
        elif more == 'no':
            break
        else:
            print('Please annswer with yes or no.')
            more = input('Would you like to do anything else? ').strip().lower()
            if more == 'yes':
                continue
            elif more == 'no':
                break

    elif userinput == "exit":
        break

    else:
        print('Please answer with option 1 or option 2 or option 3.')
        continue