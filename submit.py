import MySQLdb
import datetime


# Data gathering function
def get_date():
    date = input("Date: ")
    today = datetime.datetime.now()

    # current date
    if date == "":
        date = formatted_date(today.year, today.month, today.day)

    # relative date
    if date[0] == "-":
        yester = today - datetime.timedelta(days = int(date[1:]))
        date = formatted_date(yester.year, yester.month, yester.day)

    return date
        
def formatted_date(yyyy,mm,dd):
    return '{}-{}-{}'.format(yyyy,mm,dd)


def get_course():
    course = input('Course: ')

    cursor = MySQLdb.connect(user='root', db='mkds').cursor()
    cursor.execute("""SELECT course FROM course""")
    courses = [item[0] for item in cursor.fetchall()]

    if course not in courses:
        print("Error: invalid course {}".format(course))
        exit()

    return course


def get_type():
    t = input('Type: ')

    if t != '3lap' and t != 'flap':
        print('Error: invalid type {}'.format(t))
        exit()

    return t


def get_time():
    time = input('Time: ')

    if len(time) != 8 or time[1] != ':' or time[4] != ':':
        print('Error: invalid time {}'.format(time))
        exit()

    return time


def get_comment():
    return input('Comment: ')



# Data
add_submission = ("INSERT INTO submission (date, course, type, time, comment) "
                  "VALUES (%s, %s, %s, %s, %s)")

data_submission = (get_date(), get_course(), get_type(), get_time(), get_comment())

# Insert new submission
db = MySQLdb.connect(user="root", db="mkds")
c = db.cursor()
c.execute(add_submission, data_submission)
db.commit()
