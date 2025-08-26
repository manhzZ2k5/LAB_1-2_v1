import psycopg2
from scr.config import load_config
def create_tables():
    commands=(
        """
        CREATE TABLE IF NOT EXISTS product_1(
            id int primary key,
            name varchar,
            url_key varchar,
            price int,
            description text,
            images varchar)
        """
    )
    try:
        config=load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(commands)
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
if __name__== '__main__':
    create_tables()
