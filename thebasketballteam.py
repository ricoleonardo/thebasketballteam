import sqlite3

conn =sqlite3.connect('thebasketballteam.db')
cursor = conn.cursor()

#print('Open databse successfully')

#create_table_query = "CREATE TABLE EMPLOYEES"

# Create Tables
cursor.execute(''' CREATE TABLE IF NOT EXISTS country (id INTEGER PRIMARY KEY, name varchar)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS city (id INTEGER PRIMARY KEY, city varchar, country_id INTEGER)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name varchar, teams_id INTEGER)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name varchar, city_id INTEGERS)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS coaches (id INTEGER PRIMARY KEY, name varchar, teams_id INTEGERS, country_ID INTEGERS)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS coach_types (id INTEGER PRIMARY KEY, type varchar)''' )
cursor.execute(''' CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, seasons_id INTEGERS, home_id INTEGERS, visitors_ID INTEGERS)''')


quit = False

while not quit :
    print ("The Basketball Team")
    while True:
        choosetable = input('Please choose a table to add entry: Type (c) for country, (ct) for city, (v) to view entry and (q) to exit: ')
        if choosetable.lower() == "c":
            name = input("Country: ")
            cursor.execute('INSERT INTO country (name) VALUES (?)', [name])
            conn.commit()
            continue
        elif choosetable.lower() == "ct":
            name = input("City: ")
            country_id = input("Country ID: ")
            cursor.execute('INSERT INTO city (city, country_id) VALUES (?, ?)', (name, country_id))
            conn.commit()
            continue

        elif choosetable.lower() == "v":
            whattoview = int(input("Choose (1) for Country List or (2) for city: "))
            if whattoview == 1:
                cursor.execute('SELECT * FROM country')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            elif whattoview == 2:
                cursor.execute('SELECT * FROM city')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        
        elif choosetable.lower() == "q":
            quit = True
            break


        else:
            print("Invalid Input")
            continue
            




