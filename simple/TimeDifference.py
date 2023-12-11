import time
from datetime import datetime


if __name__ == '__main__':
    start_time_1 = 'Sun 10 May 2015 13:54:36 -0700'
    end_time_1 = 'Sun 10 May 2015 13:54:36 -0000'

    start_time_2 = 'Sat 02 May 2015 19:54:36 +0530'
    end_time_2 = 'Fri 01 May 2015 13:54:36 -0000'
    #print(time.strftime('Day dd Mon yyyy hh:mm:ss +xxxx', start_time_1))
    #print(start_time_2 - start_time_1)

    print(datetime.strptime(start_time_1, 'Day dd Mon yyyy hh:mm:ss +xxxx'))