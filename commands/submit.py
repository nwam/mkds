import MySQLdb
import datetime


# Data gathering function
def get_date():
    date = input("Date: ")
    today = datetime.datetime.now()

    # current date
    if date == "":
        date = "{}-{}-{} {}:{}:{}".format(today.year, today.month, today.day, today.hour, today.minute, today.second)

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

# return (time,standard,pts,date) of the requested PR
def get_pr(course, t):
    query_pr = ("SELECT time, standard, pts, date FROM PR WHERE course=%s AND type=%s")
    data_pr = (course, t)

    db = MySQLdb.connect(user="root", db="mkds")
    c = db.cursor()
    c.execute(query_pr, data_pr)

    return c.fetchone()

# return (name, time) of requested standard
def get_standard(course, t, pts):
    query_standard = ("SELECT name, time FROM standard NATURAL JOIN standard_name WHERE course=%s AND type=%s AND pts=%s")
    data_standard = (course, t, pts)

    db = MySQLdb.connect(user="root", db="mkds")
    c = db.cursor()
    c.execute(query_standard, data_standard)

    return c.fetchone()

##################################
def submit():
    # gather data
    query_add_submission = ("INSERT INTO submission (date, course, type, time, comment) "
                      "VALUES (%s, %s, %s, %s, %s)")

    date =          get_date()
    course =        get_course()
    record_type =   get_type()
    time =          get_time()
    comment =       get_comment()
    data_submission = (date, course, record_type, time, comment)

    # get old PR data
    old_pr = get_pr(course, record_type)

    # perform insert query
    db = MySQLdb.connect(user="root", db="mkds")
    c = db.cursor()
    c.execute(query_add_submission, data_submission)
    db.commit()

    # get new PR data
    new_pr = get_pr(course, record_type)
    pts = new_pr[2]

    # get standard data
    standard0 = get_standard(course, record_type, pts)
    standard1 = get_standard(course, record_type, pts-1)
    standard2 = get_standard(course, record_type, pts-2)
    standard3 = get_standard(course, record_type, pts-3)

    # print infos
    print("**\n")
    print("Old PR: {}\t{}\t{}\t{}\n".format(old_pr[0], old_pr[1], old_pr[2], old_pr[3]))
    print("New PR: {}\t{}\t{}\t{}\n".format(new_pr[0], new_pr[1], new_pr[2], new_pr[3]))
    print("**\n")

    print("{}:\t{}".format(standard0[0], standard0[1]))
    print("{}:\t{}".format(standard1[0], standard1[1]))
    print("{}:\t{}".format(standard2[0], standard2[1]))
    print("{}:\t{}".format(standard3[0], standard3[1]))

