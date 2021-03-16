class Scanner:
    def scan(self):
        print("scan() method from Scanner")

class Printer:
    def print(self):
        print("print() method from Printer")

class Fax:
    def send(self):
        print("send() method from Fax")

    def print(self):
        print("print() method from Fax")

class MDF_SPF(Scanner, Printer, Fax):
    pass

class MDF_SFP(Scanner, Fax, Printer):
    pass

# Printer first
print("Printer THEN Fax")
spf = MDF_SPF()
spf.scan()
spf.print()
spf.send()

# Fax first
print("\nFax THEN Printer")
sfp = MDF_SFP()
sfp.scan()
sfp.print()
sfp.send()