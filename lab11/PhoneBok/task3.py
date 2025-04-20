import psycopg2
from config import load_config

def insert_multiple_users(user_list):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for user_name, phone_number in user_list:
                    cur.execute("CALL insert_multiple_users(%s, %s)", (user_name, phone_number))
                print("Insertion completed!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")



