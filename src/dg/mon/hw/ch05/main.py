#!/bin/python
#__encoding=utf-8__
import time
import datetime


def log(func):
    def wrapper(*args, **kwargs):
        print 'call function : %s' % func.__name__
        startTime = time.ctime()
        print 'start time : %s ' % startTime
        print 'memory address : %s ' % func
        returnVaule = func(*args, **kwargs)
        endTime = time.ctime()
        print 'end time :%s ' % endTime
        runTime = datetime.datetime.strptime(endTime, "%a %b %d %H:%M:%S %Y") - datetime.datetime.strptime(startTime,
                                                                                                           "%a %b %d %H:%M:%S %Y")
        runSeconds = runTime.total_seconds()
        print 'time : %s' % runSeconds
        return returnVaule

    return wrapper


@log
def now():
    print 'now time : %s ' % time.ctime()
    time.sleep(3)


if __name__ == "__main__":
    now()
