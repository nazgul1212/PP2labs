import psycopg2
from config import load_config

def get_phonebook_page(limit, offset):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
                result = cur.fetchall()
                return result
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return None

# Example usage: get first 10 records
limit = 10
offset = 0  # Change this to get next pages
result = get_phonebook_page(limit, offset)
print(result)
