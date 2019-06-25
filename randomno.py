import datetime as dt
def randomnum(num):
    r=len(str(num))
    p=-6+r
    return str(dt.datetime.today())[-6:p]
print(randomnum(10000))
