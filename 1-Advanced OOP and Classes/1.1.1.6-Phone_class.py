class Phone:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return f"mobile phone {self.number} is turned on"

    def turn_off(self):
        return "mobile phone is turned off"

    def call(self, number):
       return f"calling {number}"

mob1 = Phone("1000")
mob2 = Phone(2000)

print(mob1.turn_on())
print(mob2.turn_on())

print(mob1.call(3000))

print(mob1.turn_off())
print(mob2.turn_off())