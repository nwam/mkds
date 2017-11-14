import MySQLdb

def query(q):
    cursor = MySQLdb.connect(user='root', db='mkds').cursor()

    cursor.execute(q)
    return cursor.fetchall()

# commits after query, returns number of rows changed
def transact(q):
    cursor = MySQLdb.connect(user='root', db='mkds').cursor()

    rows_changed = cursor.execute(q)
    cursor.commit()
    return rows_changed
