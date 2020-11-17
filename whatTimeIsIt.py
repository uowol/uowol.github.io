import datetime as dt

# Get what date is it today.
now = dt.datetime.now()
nowdate = now.strftime('%Y-%m-%d')
nowtime = now.strftime('%H:%M:%S')
print(nowtime) # 2020-MM-DD
print(nowdate)