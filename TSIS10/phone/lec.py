import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'Kassi'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur =  conn.cursor()

    creat_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id            int PRIMARY KEY,
                            first_name    varchar(40) NOT NULL,
                            second_name   varchar(40) NOT NULL,
                            salary        int,
                            dept_id       varchar(40))
    '''
    cur.execute(creat_script)
    
    insert_script = '''INSERT INTO employee (id,first_name,second_name,salary,dept_id) VALUES (%s,%s,%s,%s,%s)'''
    insert_values = (1, 'Ali','Sher', 12000,'B1') 
    cur.execute(insert_script,insert_values)
    
    conn.commit()
except Exception as error:
    print (error)
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()