#Days between
def days_diff(date1,date2):
    import datetime
​
    d1 = datetime.date(date1[0],date1[1],date1[2])
    d2 = datetime.date(date2[0],date2[1],date2[2])
    difference = d1 - d2
    return abs(difference.days)


print(days_diff((2012,2,29), (2014,2,28)))
print(days_diff((1982,4,19), (1982,4,22)))
