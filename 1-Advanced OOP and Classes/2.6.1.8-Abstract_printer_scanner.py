import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document():
        pass
    
    @abc.abstractmethod
    def get_scanner_status():
        pass

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document():
        pass

    @abc.abstractmethod
    def get_printer_status():
        pass


class CheapMFD(Scanner, Printer):
    instanceCount = 0
    def __init__(self):
        CheapMFD.instanceCount += 1
        self.serialNumber = f"C{CheapMFD.instanceCount}"
        self.resolution = "720x480"

    def scan_document(self):
        return "document has been scaned"

    def get_scanner_status(self):
        return self.resolution, self.serialNumber

    def print_document(self):
        return "document has been scaned"

    def get_printer_status(self):
        return self.resolution, self.serialNumber

class MidMFD(Scanner, Printer):
    instanceCount = 0
    def __init__(self):
        MidMFD.instanceCount += 1
        self.serialNumber = f"M{MidMFD.instanceCount}"
        self.resolution = "1280x720"

    def scan_document(self):
        return "document has been scaned"

    def get_scanner_status(self):
        return self.resolution, self.serialNumber

    def print_document(self):
        return "document has been scaned"

    def get_printer_status(self):
        return self.resolution, self.serialNumber

    def get_print_history(self):
        pass

class PremMFD(Scanner, Printer):
    instanceCount = 0
    def __init__(self):
        PremMFD.instanceCount += 1
        self.serialNumber = f"P{PremMFD.instanceCount}"
        self.resolution = "1920x1080"

    def scan_document(self):
        return "document has been scaned"

    def get_scanner_status(self):
        return self.resolution, self.serialNumber

    def print_document(self):
        return "document has been scaned"

    def get_printer_status(self):
        return self.resolution, self.serialNumber

    def get_print_history(self):
        pass

    def fax(self):
        pass


mdf1 = CheapMFD()

print(mdf1.get_scanner_status())
