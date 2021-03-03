class Time:
    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0):
        for argType in [type(hours), type(minutes), type(seconds)]:
            if argType != int:
                raise TypeError(f"Time only takes type int for args, not '{argType.__name__}'")
        
        self.timeInSeconds = (hours*60*60)+(minutes*60)+seconds

    def time_to_string(self,time=None):
        """convert a time value of total seconds into a string in the format of 'HH:MM:SS'"""
        if not time:
            time = self.timeInSeconds
        
        if type(time) != int:
            raise TypeError(f"can only convert int of time in seconds (not '{type(time).__name__}') to string of 'HH:MM:SS' format")

        prefix = "-" if time < 0 else ""
        time = abs(time)

        hours, minutes, seconds = time//(60*60), (time//60)%60, time%60
        return f"{prefix}{hours:02}:{minutes:02}:{seconds:02}"
    
    def __add__(self, otherTime):
        """return sum of either int or another Time instance added to this Time's value"""
        if type(otherTime) == type(self):
            newTime = self.timeInSeconds + otherTime.timeInSeconds
        elif type(otherTime) == int:    
            newTime = self.timeInSeconds + otherTime
        else:
            raise TypeError(f"can only add Time or int (not '{type(otherTime).__name__}') to Time")
        
        return self.time_to_string(newTime)

    def __sub__(self, otherTime):
        """return sum of either int or another Time instance subtracted from this Time's value"""
        if type(otherTime) == type(self):
            newTime = self.timeInSeconds - otherTime.timeInSeconds
        elif type(otherTime) == int:    
            newTime = self.timeInSeconds - otherTime
        else:
            raise TypeError(f"can only subtract Time or int (not '{type(otherTime).__name__}') from Time")
        
        return self.time_to_string(newTime)

    def __mul__(self, mult):
        """multiply the time by a given integer"""
        if type(mult) != int:
            raise TypeError(f"can only multiply Time (not '{type(mult).__name__}') by int")
        
        newTime = self.timeInSeconds*mult
        return self.time_to_string(newTime)

    def __str__(self):
        return self.time_to_string()
    

t = Time(21,58,50)

print(t+62)
print(t-62)

# print(t+"a")
print(t-"a")