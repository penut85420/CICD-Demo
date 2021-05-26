import datetime as dt

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def intdiv(a, b):
    return a // b

def moddiv(a, b):
    return a % b

def get_time(tz=8):
    tz = dt.timedelta(hours=tz)
    ts = dt.datetime.utcnow() + tz
    return ts.strftime('%Y-%m-%d %H:%M:%S')
