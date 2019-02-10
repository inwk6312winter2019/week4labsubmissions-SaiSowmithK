class Time(object):
    """represents the time of the day"""
time=Time()
time.hour=10
time.minute=47
time.second=28
def print_time(time):
    print("%.2d:%.2d:%.2d"%(time.hour,time.minute,time.second))
print_time(time)
