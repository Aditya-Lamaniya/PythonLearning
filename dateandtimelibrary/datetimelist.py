from datetime import date
import time

starttime = time.perf_counter()
ld=[]
d1=date(2016,8,12)
d2=date(2017,9,22)
d3=date(2018,6,26)

ld.append(d1)
ld.append(d2)
ld.append(d3)

ld.sort()

time.sleep(0)
for i in ld:
    print(i)

endtime=time.perf_counter()

print('excecution time is = ',endtime-starttime)
