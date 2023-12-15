#!/bin/python3

import datetime as dt

def timeConversion(s):
    x = dt.datetime.strptime(s, '%I:%M:%S%p')
    return "{:02d}".format(x.hour) + ":" + "{:02d}".format(x.minute) \
                + ":" + "{:02d}".format(x.second)

if __name__ == '__main__':
    print(timeConversion('12:01:00PM'))
    print(timeConversion('12:01:00AM'))
    print(timeConversion('01:01:00AM'))
