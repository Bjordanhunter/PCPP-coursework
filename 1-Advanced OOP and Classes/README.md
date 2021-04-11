# Directory and Course Description:
These are some files I made as part of my PCPP course (PCPP1 1/5 Advanced Object-Oriented Programming and Classes on edube.org) focussing on learning about classes, instances, attributes, and methods; shallow and deep operations, polymorphism, special methods, static and class methods, abstract classes, method overriding, composition, inheritance, subclassing, encapsulation, advanced techniques of exception handling, serialization of Python objects (the pickle module), the shelve module, decorators, and metaprogramming.

The 'Objectives' and 'Scenarios' parts of each of these descriptions in this readme are taken from their respective pages on edube.org. they are the only information I got for each assignment, all accompanying code (other than the examples) is mine. 

# Scenarios and Explanations of Contents 

1. [1.1.1.6-Phone_class - lab](#1116-Phone_class)  
2. [1.2.1.7-Phone_super_class_example - example](#1217-Phone_super_class_example)  
3. [1.2.1.8-Apples - lab](#1218-Apples)  
4. [2.1.1.10-Time_class_1 - lab](#21110-Time_class_1)  
5. [2.1.1.11-Time_class_2 - lab](#21111-Time_class_2)  
6. [2.2.1.6-Multiple_inheritance - lab](#2216-Multiple_inheritance)
7. [2.4.1.7-Timestamp_logger - lab](#2417-Timestamp_logger)
8. [2.4.1.12-Car_mileage_decorator_example - lab](#24112-Car_mileage_decorator_example)
9. [2.5.1.9-Watch_method_decorators - lab](#2519-Watch_method_decorators)
10. [2.6.1.8-Abstract_printer_scanner - lab](#2618-Abstract_printer_scanner)

---
## 1.1.1.6-Phone_class:
### Objectives
- creating classes, methods, and variables;
- calling methods;
- getting simple access to instance variables;  


### Scenario
- create a class representing a mobile phone;
- your class should implement the following methods:
    - `__init__` expects a number to be passed as an argument; this method stores the number in an instance variable `self.number`
    - `turn_on()` should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
    - `turn_off()` should return the message 'mobile phone is turned off';
    - `call(number)` should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
- create two objects representing two different mobile phones; assign any random phone numbers to them;
- implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
- turn off both mobiles.

Example output:  
```
mobile phone 01632-960004 is turned on  
mobile phone 01632-960012 is turned on  
calling 555-34343  
mobile phone is turned off  
mobile phone is turned off  
```

### My results:  
As demonstrated in the code, phone numbers can be strings, as maybe need if numbers include a separator for the prefix i.e. `1234 56789, 9876-54321` as opposed to all one number `123456789`.
```
mobile phone 1000 is turned on  
mobile phone 2000 is turned on  
calling 3000  
mobile phone is turned off  
mobile phone is turned off  
```

---
## 1.2.1.7-Phone_super_class_example:
Useful example of super classes and instance/class variables. (not mine):  

Another example shows that a class variable of a super class can be used to count the number of all objects created from the descendant classes (subclasses). We'll achieve this by calling the superclass `__init__` method.

Another class variable is used to keep track of the serial numbers (which in fact are also counters) of particular subclass instances. In this example, we are also storing instance data (phone numbers) in instance variables.

The class `Phone` is a class representing a blueprint of generic devices used for calling. This class definition delivers the `call` method, which displays the object’s variable, which holds the phone number. This class also holds a class variable that is used to count the number of instances created by its subclasses.

Subclasses make use of the superclass `__init__` method, then instances are created. This gives us the possibility to increment the superclass variable.

---
## 1.2.1.8-Apples:
### Objectives
- creating classes, class and instance variables;
- accessing class and instance variables;

### Scenario
Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

- the number of apples processed, stored as a class variable;
- the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;  

Hint: Use a `random.uniform(lower, upper)` function to create a random number between the **lower** and **upper** float values.

### My results:
Ran 5 times, the weight was often the limiting factor, with the total number of apples usually around 855 (+/-10).
```
total number of apples: 855
total weight of apples: 299.98589109958203

total number of apples: 861
total weight of apples: 299.96240624314885

total number of apples: 856
total weight of apples: 299.7373326346645

total number of apples: 856
total weight of apples: 299.9091643876073

total number of apples: 861
total weight of apples: 299.7265408900911
```
It did still work with a higher weight of 350, stopping at 1000 apples more often.
```
total number of apples: 996
total weight of apples: 349.9308339267708

total number of apples: 1000
total weight of apples: 344.48903914769346

total number of apples: 1000
total weight of apples: 346.52638648407566
```
An alternate solution could be where you get the random weight in the `__init__` and have a 'remove apple' method to remove it from the totals. Which you could call if the weight goes over 300, as it often would with having `Apple.totalWeight < maxWeight` in the while loop condition (total weight of 299.9 and the loop would run, adding a random apple weight of, at lest, 0.2. The total weight would then be 300.1 which is, obviously, over 300).  
Or some kind of 'apple crate' super class, for which you make an apple, but only add it to the crate if it wouldn't exceed the maximum weight/number of apples already in the 'crate'.

---
## 2.1.1.10-Time_class_1:
### Objectives
- improving the student's skills in operating with special methods

### Scenario
- Create a class representing a time interval;
- the class should implement its own method for addition, subtraction on time interval class objects;
- the class should implement its own method for multiplication of time interval class objects by an integer-type value;
- the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
- the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
- check the argument type, and in case of a mismatch, raise a TypeError exception.

### Hint #1
- just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
- for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

Test data:
- the first time interval (fti) is hours=21, minutes=58, seconds=50
- the second time interval (sti) is hours=1, minutes=45, seconds=22
- the expected result of addition (fti + sti) is 23:44:12
- the expected result of subtraction (fti - sti) is 20:13:28
- the expected result of multiplication (fti * 2) is 43:57:40

### Hint #2
- you can use the assert statement to validate if the output of the '__str__' method applied to a time interval object equals the expected value.

### My results:
Although I did look at the hints, I didn't look at them until I was almost finished, so I could make sure I had understood the requirement correctly as I did find the phrasing a bit confusing in places.  


**Variables**
|variable|hours|minutes|seconds|
|--      |--   |--     |--     |
|time 1  |   21|     58|     50|
|time 2  |    1|     45|     22|

**Success:**  
|test       |output    |expected |  
|-----------|----------|---------|
|time1+time2| 23:44:12 |23:44:12 |  
|time1-time2| 20:13:28 |20:13:28 | 
|time2-time1| -20:13:28|-20:13:28|  
|time1*2    | 43:57:40 |43:57:40 |  

**Errors:**
|test |output|expected|
|-    |-     |-       |
| timeError = Time(0,"2",30) | TypeError: Time only takes type int for args, not 'str' | TypeError: [message] |
| print(t1+2) | TypeError: can only add Time (not 'int') to Time |  TypeError: [message] |
| print(t1-2) | TypeError: can only subtract Time (not 'int') from Time | TypeError: [message] |
| print(t1*t2) | TypeError: can only multiply Time (not 'Time') by int | TypeError: [message] |

---
## 2.1.1.11-Time_class_2:
### Objectives
- improving the student's skills in operating with special methods

### Scenario
- Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
- to add an integer to a time interval object means to add seconds;
- to subtract an integer from a time interval object means to remove seconds.

### Hint
- in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.

Test data:
- the time interval (tti) is hours=21, minutes=58, seconds=50
- the expected result of addition (tti + 62) is 21:59:52
- the expected result of subtraction (tti - 62) is 21:57:48

### My results:
Again I only looked at the hint after I had finished, but I found that I implemented it differently than suggested - creating a new time instance out of the int. Instead I just added (or subtracted) the int on to the total seconds; creating a whole new time object seamed unnecessarily complicated, at least for how I had already implemented it. I also added in some doc strings on some of the methods.

**Variables**
|variable|hours|minutes|seconds|
|--      |--   |--     |--     |
|time    |   21|     58|     50|

**Success:**
|test       |output    |expected |  
|-----------|----------|---------|
|time1+time2| 21:59:52 |21:59:52 |  
|time1-time2| 21:57:48 |21:57:48 |

**Errors:**
|test |output|expected|
|-    |-     |-       |
| print(t+"a") | TypeError: can only add Time or int (not 'str') to Time | TypeError: [message] |
| print(t-"a") | TypeError: can only subtract Time or int (not 'str') from Time | TypeError: [message] |  

(Error messages updated to reflect integer option.)  

---

## 2.2.1.6-Multiple_inheritance:
### Objectives
- improving the student's skills in operating with multiple inheritance;
- pointing out the nature of multiple inheritance problems.

### Scenario
- Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
- The methods are delivered by the following classes:
    - scan(), delivered by the Scanner class;
    - print(), delivered by the Printer class;
    - send() and print(), delivered by the Fax class.
- Each method should print a message indicating its purpose and origin, like:
    - 'print() method from Printer class'
    - 'send() method from Fax class'
- create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
- create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
- on each object call the methods: scan(), print(), send();
- observe the output differences. Was the Printer class utilized each time?

### My results:
Printer was only used when initialised first.
```
Printer THEN Fax
scan() method from Scanner
print() method from Printer
send() method from Fax

Fax THEN Printer
scan() method from Scanner
print() method from Fax
send() method from Fax
```

---

## 2.4.1.7-Timestamp_logger:
### Objectives
- Improving the student's skills in creating decorators and operating with them.

### Scenario
- Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
- Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
- Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

### Hint:

To print the current time, you could use the following code:
```
# import module responsible for time processing
from datetime import datetime

# get current time using now() method
timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print(string_timestamp)
```


### My results:
This did take me a little longer then I would've liked as I was overthinking it a bit and added the ability to track how long the function took.

output:
```

2021-03-15 11:46:45
2+0= 2
'add' took 0.028887s to run

2021-03-15 11:46:45
2*0= 0
'mult' took 0.013019s to run
----------

2021-03-15 11:46:47
2+1= 3
'add' took 0.022045s to run

2021-03-15 11:46:47
2*1= 2
'mult' took 0.020017s to run
----------

2021-03-15 11:46:48
2+2= 4
'add' took 0.028801s to run

2021-03-15 11:46:48
2*2= 4
'mult' took 0.02099s to run
----------
```
## 2.4.1.12-Car_mileage_decorator_example:
Example class decorators (Car class from 2.4.1.11, not mine)  

Now let's create a function that will decorate a class with a method that issues alerts whenever the 'mileage' attribute is read.

Look at the code in the [file]. Let's analyse it:

-   line 1:  `def object_counter(class_):`  – this line defines a decorating function that accepts one parameter 'class_' (note the underscore)
-   line 2:  `class_.__getattr__orig = class_.__getattribute__`  – the decorator makes a copy of the reference to the  `__getattribute__`  special method. This method is responsible for returning the attribute values. The reference to this original method will be used in a modified method;
-   line 4:  `def new_getattr(self, name):`  – a definition of the method playing the role of the new  `__getattribute__`  method starts here. This method accepts an attribute name – it’s a string;
-   line 5:  `if name == 'mileage':`  – in case some code asks for the 'mileage' attribute, the next line will be executed;
-   line 6:  `print('We noticed that the mileage attribute was read')`  – a simple alert is issued;
-   line 7:  `return class_.__getattr__orig(self, name)`  – the original method  `__getattribute__`  referenced by  `class.__getattr__orig`  is called. This ends the 'new_getattr' function definition;
-   line 9:  `class_.__getattribute__ = new_getattr`  – now the 'new_getattr' is defined, so it can now be referenced as the new '\_\_getattribute__' method by a decorated class;
-   line 10:  `return class_`  – every well behaved and developed decorator should return the decorated object – in our case it is a decorated class.
- [line 13-20: Car class and code taken from previous page (2.4.1.11).]

The last thing we should do is decorate the Car class:
```
@object_counter
class Car:
```
When you run the code, you can see that access to the 'mileage' attribute has been detected:
```
We noticed that the mileage attribute was read 
The mileage is 0 
The VIN is ABC123
```
---
## 2.5.1.9-Watch_method_decorators:
### Objectives

-   improving the student's skills in operating with static and class methods

### Scenario

-   Create a class representing a luxury watch;
-   The class should allow you to hold a number of watches created in the  `watches_created`  class variable. The number could be fetched using a class method named  `get_number_of_watches_created`;
-   the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular  `__init__`  method should not allow ordering engravings;
-   the regular  `__init__`  method should only increase the value of the appropriate class variable;

The text intended to be engraved should follow some restrictions:

-   it should not be longer than 40 characters;
-   it should consist of alphanumerical characters, so no space characters are allowed;
-   if the text does not comply with restrictions, an exception should be raised;

before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

-   Create a watch with no engraving
-   Create a watch with correct text for engraving
-   Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
-   After each watch is created, call class method to see if the counter variable was increased

### My results:
Having the 'validate_engraving' return true is slightly redundant as the exception would stop execution, I had to guess on the error type as I wasn't 100% on what type to use. I  also changed some of the names because I kept misspelling them.
It will attempt to make 6 watches (1 no engraving, 3 valid engravings, 2 invalid engravings).
Output:
```
foo@baz.com was not valid
hello world was not valid
number of watches created: 4
```
---
## 2.6.1.8-Abstract_printer_scanner:
### Objectives

-   Creation of abstract classes and abstract methods;
-   multiple inheritance of abstract classes;
-   overriding abstract methods;
-   delivering multiple child classes.

### Scenario
-   You are about to create a multifunction device (MFD) that can scan and print documents;
-   the system consists of a scanner and a printer;
-   your task is to create blueprints for it and deliver the implementations;
-   create an abstract class representing a scanner that enforces the following methods:
	-   **scan_document**  – returns a string indicating that the document has been scanned;
	-   **get_scanner_status**  – returns information about the scanner (max. resolution, serial number)

-   Create an abstract class representing a printer that enforces the following methods:
	-   **print_document**  – returns a string indicating that the document has been printed;
	-   **get_printer_status**  – returns information about the printer (max. resolution, serial number)

-   Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
	-   MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
	-   MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
	-   MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.

-   Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

### My results:

---
