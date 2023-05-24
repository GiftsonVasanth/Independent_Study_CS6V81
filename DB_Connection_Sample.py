import singlestoredb as db

conn = db.connect(host = 'svc-f2481299-63e2-4158-8a15-8faa9b5a70d7-dml.aws-oregon-4.svc.singlestore.com',
port = '3306',
user = 'admin',
password = 'sH5WX6dAozV9w6ISgUz6NHu3kAPQeIkL', 
database = 'chatGPT_data')

with conn:
    conn.autocommit(True)
    with conn.cursor() as cur:
        #cur.execute('UPDATE testID SET Code = "DanI" WHERE ID =3')
        cur.execute('SELECT * FROM offices')
        for row in cur.fetchall():
            print(row)

