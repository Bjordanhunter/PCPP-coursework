from datetime import datetime
from time import sleep

def log_time(func):
    def wapper(a,b):
        startTime = datetime.now()
        print("\n"+startTime.strftime("%Y-%m-%d %H:%M:%S"))
        func(a,b)
        
        # extra functionality 
        endTime = datetime.now()
        timeDiff = (endTime-startTime).total_seconds()
        print(f"'{func.__name__}' took {timeDiff}s to run") 
    return wapper

@log_time
def mult(a,b):
    print(f"{a}*{b}= {a*b}")


@log_time
def add(a,b):
    print(f"{a}+{b}= {a+b}")


for i in range(3):
    add(2,i)
    mult(2,i)
    print("-"*10)
    sleep(1.1)
