import psycopg2
from scr.config import load_config
from read_json import load_all_data
data_list = load_all_data()
def insert_many():
    sql = """
           INSERT INTO product_1 (id, name, url_key, price, description, images)
           VALUES (%s, %s, %s, %s, %s, %s)
           ON CONFLICT (id) DO NOTHING;
       """
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                for data in data_list:
                    cur.execute(sql,(data["id"],data["name"],data["url_key"],data["price"],data["description"],data["images"]))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    config = load_config()
    insert_many()