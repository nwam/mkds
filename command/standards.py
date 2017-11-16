import MySQLdb
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from command import mkdsdb

# pts,standard,count
def pr_standards_full():
    q = """ SELECT pts, standard, CAST(SUM(n) as UNSIGNED) AS count FROM \
                (SELECT       pts,standard,COUNT(1) as n FROM PR GROUP BY pts,standard \
                 UNION SELECT pts,name,0 FROM standard_name) AS q \
            GROUP BY pts,standard ORDER BY pts;"""
    return mkdsdb.query(q, ('pts', 'standard', 'count'))

def pr_standards():
    q = """ SELECT pts, standard, COUNT(1) FROM PR GROUP BY pts, standard ORDER BY pts"""
    return mkdsdb.query(q, ('pts', 'standard', 'count'))

def pr_at_date(d):
    q = """SELECT submissionID, date, courseID, course, type, time, standard, pts, comment FROM submission_plus INNER JOIN (SELECT MAX(submissionID) AS prIdAtDate FROM submission_plus WHERE date <= DATE('{}') GROUP BY course,type) AS q ON q.prIdAtDate = submission_plus.submissionID ORDER BY courseID, type""".format(d)
    return mkdsdb.query(q, ('submissionID', 'date', 'coourseID', 'course', 'type', 'time', 'standard', 'pts', 'comment'))

def graph():
    # Query data
    df = pr_standards()

    # Correct data types
    df['count'] = df['count'].astype(int) 

    # Plot
    plt.style.use('ggplot')
    plt.bar(df['pts'], df['count'], tick_label = df['standard'])

    plt.title('MKDS Standards')
    plt.ylabel('count')
    plt.xlabel('standard')
    plt.xticks(rotation=90)

    ax = plt.gca()
    ax.yaxis.set_major_locator(plticker.MultipleLocator(base=1))

    plt.grid(axis='x', b=False)

    plt.show()

#def graph_progression(start_date, end_date):
    # Query data

    # Convert to pandas df

    # Correct dataA
