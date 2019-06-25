import datetime as dt

print( ">>> program start")
today=dt.datetime.today()
print(today)
a=[]
for i in range(10,100,7):
    a.append(i)
print(a)

b=0
for p in a:
    try:
        c=p/b
        print(c)
    except Exception as ex:
        print("error occured",ex)
    b+=1
today1=dt.datetime.today()
print(today1-today)

print( " >>> end program")
