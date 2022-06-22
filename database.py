import psycopg2
from config import config
import datetime
from models import Order

def add_order(email, owner, phone_number):
    conn = None
    try:
        # read connection parameters
        params = config()
        return_item = {}
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
	    
        # create a cursor
        cur = conn.cursor()
        sql_query = """INSERT INTO orders (email, owner, phone_number, created_on)
             VALUES(%s, %s, %s, %s)
             RETURNING order_id, email, owner ,phone_number, created_on;"""
        now_str = str(datetime.datetime.now())
        cur.execute(sql_query, (email,owner,phone_number,now_str))
        added_object = cur.fetchone()

        return_item['order_id'] = Order(order_id=added_object[0],
         email=added_object[1],
         owner=added_object[2],
         phone_number=added_object[3],
         created_on=added_object[4]) 

        conn.commit()
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_item = {"message": str(error)}
    finally:
        if conn is not None:
            conn.close()
        return return_item

def get_orders(offset, limit):
    conn = None
    try:
        # read connection parameters
        params = config()
        return_item = {}
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
	    
        # create a cursor
        cur = conn.cursor()
        sql_query = """SELECT * FROM orders 
        OFFSET %s ROWS 
        FETCH FIRST %s ROW ONLY"""
        cur.execute(sql_query, (offset, limit))
        rows = cur.fetchall()
        for row in rows:
            return_item[row[0]]= Order(order_id=row[0],
                                       email=row[1],
                                       owner=row[2],
                                       phone_number=row[3],
                                       created_on=str(row[4]) )
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_item = {"message": str(error)}
    finally:
        if conn is not None:
            conn.close()
        return return_item

def get_order(order_id):
    conn = None
    try:
        # read connection parameters
        params = config()
        return_item = {}
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
	    
        # create a cursor
        cur = conn.cursor()
        sql_query = """SELECT * FROM orders 
        WHERE order_id = %s"""
        cur.execute(sql_query, (order_id,))
        fetched_object = cur.fetchone()
        if fetched_object is not None:
            return_item['order_id'] = Order(order_id=fetched_object[0],
            email=fetched_object[1],
            owner=fetched_object[2],
            phone_number=fetched_object[3],
            created_on=str(fetched_object[4]))
        else:
            return_item['message'] = "Order with such id was not found."
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_item = {"message": str(error)}
    finally:
        if conn is not None:
            conn.close()
        return return_item

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        return_message = ''
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
	    
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return_message = 'Database connection error'
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        if return_message == '':
            return_message = 'Database connection attempt succesfull'
        return return_message

if __name__ == '__main__':
    connect()
