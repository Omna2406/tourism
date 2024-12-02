import mysql.connector# Establish a connection to the database
cnx = mysql.connector.connect(
    user='root',
    password='admin',
    host='localhost',
    database='uttarakhand_tourism'
)
# Create a cursor object
cursor = cnx.cursor()
# Create tables
query1 = """
    CREATE TABLE IF NOT EXISTS destinations (
        destination_id INT AUTO_INCREMENT PRIMARY KEY,
        destination_name VARCHAR(255),
        description TEXT,
        location VARCHAR(255)
    )
"""
query2 = """
    CREATE TABLE IF NOT EXISTS hotels (
        hotel_id INT AUTO_INCREMENT PRIMARY KEY,
        hotel_name VARCHAR(255),
        destination_id INT,
        address VARCHAR(255),
        rating INT,
        FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
    )
"""

query3 = """
    CREATE TABLE IF NOT EXISTS restaurants (
        restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
        restaurant_name VARCHAR(255),
        destination_id INT,
        address VARCHAR(255),
        rating INT,
        FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
    )
"""

query4 = """
    CREATE TABLE IF NOT EXISTS activities (
        activity_id INT AUTO_INCREMENT PRIMARY KEY,
        activity_name VARCHAR(255),
        destination_id INT,
        description TEXT,
        FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
    )
"""

try:
    # Execute the queries
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    print("Tables created successfully!")
except mysql.connector.Error as err:
    print("Failed to create tables: {}".format(err))

# Insert data into tables
query_destinations = """
    INSERT INTO destinations (destination_name, description, location)
    VALUES ('Mussoorie', 'A hill station in the foothills of the Himalayas', 'Dehradun district'),
           ('Nainital', 'A hill station in the Kumaon foothills of the Himalayas', 'Nainital district'),
           ('Haridwar', 'A holy city on the banks of the Ganges River', 'Haridwar district'),
           ('Rishikesh', 'A holy city on the banks of the Ganges River', 'Dehradun district'),
           ('Auli', 'A ski resort town in the Chamoli district', 'Chamoli district')
"""

try:
    cursor.execute(query_destinations)
    cnx.commit()  # Commit the insert for destinations table
    print("Destinations data inserted successfully!")
except mysql.connector.Error as err:
    print("Failed to insert destinations data: {}".format(err))

# Now insert data into other tables (hotels, restaurants, activities)
query_hotels = """
    INSERT INTO hotels (hotel_name, destination_id, address, rating)
    VALUES ('Hotel Padmini Nivas', 1, 'The Mall, Mussoorie', 4),
           ('The Naini Retreat', 2, 'Ayarpatta Slopes, Nainital', 5),
           ('Hotel Ganga Kinare', 3, 'Rishikesh Road, Haridwar', 4),
           ('Hotel Shivpuri', 4, 'Rishikesh Road, Rishikesh', 4),
           ('The Royal Village', 5, 'Auli Road, Joshimath', 5)
"""

query_restaurants = """
    INSERT INTO restaurants (restaurant_name, destination_id, address, rating)
    VALUES ('Kalsang', 1, 'The Mall, Mussoorie', 4),
           ('Sakleys Restaurant', 2, 'The Mall, Nainital', 4),
           ('Haveli Hari Ganga', 3, 'Rishikesh Road, Haridwar', 4),
           ('The 60s Cafe', 4, 'Rishikesh Road, Rishikesh', 4),
           ('The Cliff Top Club', 5, 'Auli Road, Joshimath', 5)
"""

query_activities = """
    INSERT INTO activities (activity_name, destination_id, description)
    VALUES ('Trekking', 1, 'Trek to the top of Gun Hill for panoramic views of the Himalayas'),
           ('Boating', 2, 'Take a boat ride on Naini Lake for scenic views of the surrounding hills'),
           ('Rafting', 3, 'Go white-water rafting on the Ganges River for an adrenaline-packed adventure'),
           ('Yoga', 4, 'Practice yoga at one of the many ashrams and studios in Rishikesh'),
           ('Skiing', 5, 'Hit the slopes at the Auli Ski Resort for a fun-filled winter adventure')
"""

try:
    cursor.execute(query_hotels)
    cursor.execute(query_restaurants)
    cursor.execute(query_activities)
    cnx.commit()  # Commit the insertions for hotels, restaurants, and activities
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print("Failed to insert data: {}".format(err))

# Close the cursor and connection
cursor.close()
cnx.close()
