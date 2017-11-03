# Given standards_in
# which is copied right from the mk play pages' websites,
# outputs a tab-separated-value representation to standards.tsv
def format_time(t):
    ft = ''

    # minute
    if '\'' in t:
        t = t.split('\'')
        ft += t[0]
        t = t[1]
    else:
        ft += '0'
    ft += ':'

    # second
    s = t.split('"')[0]
    sp = ''
    for i in range(len(s), 2):
        sp += '0'
    s = sp + s
    ft += s
    ft += ':'

    
    # milisecond
    ms = t.split('"')[1]
    msp = ''
    for i in range(len(ms), 3):
        msp += '0'
    ms += msp
    ft += ms

    if len(ft.split(':')) != 3 or len(ft) != 8:
        print('oops')

    return ft


f = open("standards_in")
out = open("standards.tsv", 'w')

p = [] 
for line in f:
    p.append(line.strip().split('\t'))

for category in range(2, len(p)):
    for time in range(2, len(p[category])):
        out.write(p[category][0])
        out.write('\t')
        out.write(p[category][1])
        out.write('\t')
        out.write(p[0][time])
        out.write('\t')
        out.write(p[1][time])
        out.write('\t')

        time = p[category][time]
        ftime = format_time(time)
        out.write(ftime)
        out.write('\n')
