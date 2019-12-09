import pymysql

conn = pymysql.connect( host='localhost', user='root', password='3280', charset='utf8', db='ranking')

def db_query(db, sql, params):
    # Connect to MySQL
    #try: # create Dictionary Cursor
    with conn.cursor() as cursor:
        sql_query = sql
        # excute SQL
        cursor.execute(sql_query, params)
        # commit data
    conn.commit()
    #finally:
        #conn.close()

def insert_score(name,grade):
    sql='INSERT INTO info (name, score) VALUES (%s,%s)'
    params=(name,grade)
    db_query(db='ranking',sql=sql,params=params)

#select * from table_name order by xxx desc
def show_ranking():
    #try:
    with conn.cursor() as cursor:
        sql='SELECT * from info ORDER BY score DESC'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    #finally:
    #    conn.close()
