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
    return mkdsdb.query(q)

def pr_standards():
    q = """ SELECT pts, standard, COUNT(1) FROM PR GROUP BY pts, standard ORDER BY pts"""
    return mkdsdb.query(q)

def graph():
    # Query data
    pr_stds = pr_standards()

    # Convert to pandas df
    df = pd.DataFrame(  data = [[ij for ij in i] for i in pr_stds], 
                        columns = ('pts','standard','count'))

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
    #ax.set_yticks(np.arange(0, max(df['count']), 1))

    plt.grid(axis='x', b=False)

    plt.show()
