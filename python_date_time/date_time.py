import datetime

date = datetime.date(2025, 1, 2)
print(date)                 # 2025-01-02

time = datetime.time(12, 30, 0)
print(time)                 # 12:30:00

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)

# to check if the date passed the target date

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print ("Target date has passed")
else:
    print("Target date has not passed")