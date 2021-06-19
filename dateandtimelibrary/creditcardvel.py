from datetime import *

def validatecard(expdate):
    if expdate>datetime.now().date():
        print(" valid ")
    else:
        print(" expired")

validatecard(date(2020,3,2))