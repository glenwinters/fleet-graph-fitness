import csv
import psycopg2
import psycopg2.extras

# Filename of activities from Strava data dump
STRAVA_ACTIVITIES_FILENAME = "activities.csv"

# TODO: read from config
DB_NAME = "fitness"
DB_USER = "postgres"
DB_PASSWORD = "fitness"
DB_HOST="localhost"
DB_PORT = 5011

def read_activities(filename):
    activities = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header
        for row in reader:
            # activities.append(
            #     source="Strava"
            #     source_id=row[0]
            #     start_timestamp=row[1]
            #     title=row[2]
            #     duration_seconds=row[5]
            # })
            activity = (row[2], row[5], row[1], "Strava", row[0])
            print(activity)
            activities.append(activity)
    return activities

def clear_db(db_cursor):
    db_cursor.execute("DELETE from workouts;")

def populate_db(db_cursor, activities):
    """Populates the fitness DB with activities
    
    activities must match the format of the INSERT statement
    """
    psycopg2.extras.execute_values(
        db_cursor,
        "INSERT INTO workouts (title, duration_seconds, start_timestamp, source, source_id) VALUES %s",
        activities[:5]
    )

if __name__ == "__main__":
    
    db_connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
    db_cursor = db_connection.cursor()


    activities = read_activities(STRAVA_ACTIVITIES_FILENAME)
    clear_db(db_cursor)
    populate_db(db_cursor, activities)
    
    db_connection.commit()

    db_cursor.execute("SELECT * from workouts;")
    result = db_cursor.fetchall()
    print(result)