# Saydullaev Afruzbek N42 group
# 1-misol
from abc import ABC

import psycopg2
conn = psycopg2.connect(host='localhost',
                        database='postgres',
                        user='postgres',
                        password='2008',
                        port=5432
                         )
cur = conn.cursor()

create_table_product = """CREATE TABLE IF NOT EXISTS product
(       id serial PRIMARY KEY
        name varchar(255) NOT NULL,
        price integer NOT NULL,
        color varchar(255) NOT NULL,
        image_url varchar(255) NOT NULL    
);"""

cur.execute(create_table_product)
conn.commit()



# 2 -misol
def insert_product():
    insert_into_query = """INSERT INTO product (name, price, color, image_url) 
    VALUES (%s, %s, %s, %s);"""
    cur.execute(insert_into_query,)
    conn.commit()

    cur.close()
    conn.close()
def update_product():
    update_query = """UPDATE product set name = %s, price = %s, color = %s, image_url = %s;"""
    data = (name,price, color, )
    cur.execute(update_query, data)
    conn.commit()
    cur.close()
    conn.close()
def select_all_product():
    select_all_product = """SELECT * FROM product ;"""
    cur.execute(select_all_product)

def delete_product():
    delete_into_query = """DELETE FROM product where id = %s;"""

    cur.execute(delete_into_query)
    conn.commit()
    cur.close()
    conn.close()


# 3-misol
# class Alphabet:
#     def init(self, sequence):
#         self._sequence = sequence
#         self._index = 0
#
#     def iter(self):
#         return self
#
#     def next(self):
#         if self._index >= len(self._sequence):
#             raise StopIteration
#         else:
#             result = self._sequence[self._index]
#             self._index += 1
#             return result
#
#
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# sequences = Alphabet(abc)
#
# print(next(sequences))
# for n in sequences:
#     print(n)




















#4-misol
#def print_numbers(numbers):
#    print('numbers:


#print_numbers()










#5- misol
# import threading
#
# import time
#
#
# def print_numbers():
#     for n in range(5):
#         print(f"numbers {n}")
#         time.sleep(1.5)
#
#
# def print_letters():
#     for a in "ABCDE":
#         print(f"=====> {a}")
#         time.sleep(1.5)
#
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
#
# start = time.time()
# thread1.start()
#
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# end = time.time()
#
#
# print("finish", {end-start})




#6 -misol

class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
