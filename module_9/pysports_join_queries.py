/*
  Author: Dylan
  Date: 7/28/23
  Description: Module 9.2 aggregate queries
/*

import pymysql

# Database connection 
db_host = "your_database_host"
db_user = "your_database_user"
db_password = "PassWord"
db_name = "pysports"

# Connect to the database
try:
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    print("Connected to the database successfully!")
except pymysql.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Create a cursor object to execute queries
cursor = connection.cursor()

try:
    # INNER JOIN query to combine player and team tables by team_id
    query = """
        SELECT player.player_id, player.first_name, player.last_name, team.team_name
        FROM player
        INNER JOIN team ON player.team_id = team.team_id;
    """
    cursor.execute(query)

    # Fetch rows from the result
    result = cursor.fetchall()

    # Display  results
    for row in result:
        player_id, first_name, last_name, team_name = row
        print(f"Player ID: {player_id} First Name: {first_name} Last Name: {last_name} Team Name: {team_name}")

except pymysql.Error as e:
    print(f"Error executing the query: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
