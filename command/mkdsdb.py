import MySQLdb
import pandas as pd

# Returns the list obtained from the query if columns aren't specified
# Returns a pandas.DataFrame if columns are specified
def query(q, cols=None):
    cursor = MySQLdb.connect(user='root', db='mkds').cursor()

    cursor.execute(q)

    query_response = cursor.fetchall()

    if cols == None:
        return query_response

    return pd.DataFrame(  data = [[ij for ij in i] for i in query_response], 
                        columns = cols)



# commits after query, returns number of rows changed
def transact(q):
    cursor = MySQLdb.connect(user='root', db='mkds').cursor()

    rows_changed = cursor.execute(q)
    cursor.commit()
    return rows_changed
