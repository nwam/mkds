import MySQLdb
import datetime

def query(q):
    with cursor as MySQLdb.connect(user='root', db='mkds').cursor():
        cursor.execute(q)
        return cursor.fetchall()

    print("Error: Failed to access mkds database".format(q))
    exit()

# commits after query, returns number of rows changed
def transact(q):
    with cursor as MySQLdb.connect(user='root', db='mkds').cursor():
        rows_changed = cursor.execute(q)
        cursor.commit()
        return rows_changed

    print("Error: Failed to access mkds database".format(q))
    exit()
