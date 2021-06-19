from datetime import *

def cardvalidation(expdate):
    if expdate>datetime.now().date():
        return "valid"
    else:
        return "expired"

