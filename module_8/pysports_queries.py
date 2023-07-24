/*

    Author: Dylan Cooper
    Date: 7-21-2023
    Description: Module 8.3 mysql pysports database with two select queries
*/
import mysql.connector

def display_team_records(cursor):
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    print("DISPLAYING TEAM RECORDS")
    for team in teams:
        print("Team ID: {}, Team Name: {}, Mascot: {}".format(team[0], team[1], team[2]))

def display_player_records(cursor):
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    print("\nDISPLAYING PLAYER RECORDS")
    for player in players:
        print("Player ID: {}, First Name: {}, Last Name: {}, Team ID: {}".format(player[0], player[1], player[2], player[3]))

try:
    # Establishing a connection to the mysql
    db = mysql.connector.connect(
        user="your_database_user",
        password="PassWord",
        host="test",
        database="pysports",
        raise_on_warnings=True
    )

    if db.is_connected():
        print("Connected to the database!")
        cursor = db.cursor()

        # team records
        display_team_records(cursor)

        # player records
        display_player_records(cursor)

except mysql.connector.Error as error:
    print(f"Error while connecting to MySQL: {error}")

finally:
    # Close final the connection to the database
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Connection to the database closed!")
