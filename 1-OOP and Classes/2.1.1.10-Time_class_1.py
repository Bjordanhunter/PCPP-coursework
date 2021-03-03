class Time:
    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0):
        for argType in [type(hours), type(minutes), type(seconds)]:
            if argType != int:
                raise TypeError(f"Time only takes type int for args, not '{argType.__name__}'")
        
        self.timeInSeconds = (hours*60*60)+(minutes*60)+seconds

    def time_to_string(self,time=None):
        if not time:
            time = self.timeInSeconds

        prefix = "-" if time < 0 else ""
        time = abs(time)

        hours, minutes, seconds = time//(60*60), (time//60)%60, time%60
        return f"{prefix}{hours:02}:{minutes:02}:{seconds:02}"
    
    def __add__(self, otherTime):
        if type(otherTime) != type(self):
            raise TypeError(f"can only add Time (not '{type(otherTime).__name__}') to Time")
        
        newTime = self.timeInSeconds + otherTime.timeInSeconds
        return self.time_to_string(newTime)

    def __sub__(self, otherTime):
        if type(otherTime) != type(self):
            raise TypeError(f"can only subtract Time (not '{type(otherTime).__name__}') from Time")
        
        newTime = self.timeInSeconds - otherTime.timeInSeconds
        return self.time_to_string(newTime)

    def __mul__(self, mult):
        if type(mult) != int:
            raise TypeError(f"can only multiply Time (not '{type(mult).__name__}') by int")
        
        newTime = self.timeInSeconds*mult
        return self.time_to_string(newTime)

    def __str__(self):
        return self.time_to_string()
    

t1 = Time(21,58,50)
t2 = Time(hours=1, minutes=45, seconds=22)

print(t1+t2, '(t1+t2)=="23:44:12"')
print(t1-t2, '(t1-t2)=="20:13:28"')
print(t2-t1, '(t2-t1)=="-20:13:28"')
print(t1*2,  '(t1*2) =="43:57:40"')


# timeError = Time(0,"2",30)

# print(t1+2)
# print(t1-2)
# print(t1*t2)