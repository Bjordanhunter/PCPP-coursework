# Course Discription:
These are some files I made as part of my PCPP course (PCPP1 1/5 Advanced Object-Oriented Programming and Classes on edube.org) focussing on learning about classes, instances, attributes, and methods; shallow and deep operations, polymorphism, special methods, static and class methods, abstract classes, method overriding, composition, inheritance, subclassing, encapsulation, advanced techniques of exception handling, serialization of Python objects (the pickle module), the shelve module, decorators, and metaprogramming.

# Senarios and Explnations of Contents 

## 1.1.1.6-Phone_class:
### Objectives
- creating classes, methods, and variables;
- calling methods;
- getting simple access to instance variables;  

![Mobile phone]()

### Scenario
- create a class representing a mobile phone;
- your class should implement the following methods:
    - __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
    - turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
    - turn_off() should return the message 'mobile phone is turned off';
    - call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
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
As demonstrated in the code, phone numbers can be strings, as maybe need if numbers include a separator for the prefix i.e. `1234 56789, 9876-54321` as aposed to all one number `123456789`.
```
mobile phone 1000 is turned on  
mobile phone 2000 is turned on  
calling 3000  
mobile phone is turned off  
mobile phone is turned off  
```


## 1.2.1.7-Phone_super_class_example:
Useful example of super classes and instanse/class variables. (not mine)
Another example shows that a class variable of a super class can be used to count the number of all objects created from the descendant classes (subclasses). We'll achieve this by calling the superclass `__init__` method.

Another class variable is used to keep track of the serial numbers (which in fact are also counters) of particular subclass instances. In this example, we are also storing instance data (phone numbers) in instance variables.

The class `Phone` is a class representing a blueprint of generic devices used for calling. This class definition delivers the `call` method, which displays the object’s variable, which holds the phone number. This class also holds a class variable that is used to count the number of instances created by its subclasses.

Subclasses make use of the superclass `__init__` method, then instances are created. This gives us the possibility to increment the superclass variable.


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
It did still work with a higher weight of 350, stoping at 1000 apples more often.
```
total number of apples: 996
total weight of apples: 349.9308339267708

total number of apples: 1000
total weight of apples: 344.48903914769346

total number of apples: 1000
total weight of apples: 346.52638648407566
```
An alternate soution could be where you get the random weight in the `__init__` and have a 'remove apple' method to remove it from the totals. Which you could call if the weight goes over 300, as it often would with having `Apple.totalWeight < maxWeight` in the while loop condition (total weight of 299.9 and the loop would run, adding a random apple weight of, at lest, 0.2. The total weight would then be 300.1 which is, obviously, over 300).  
Or some kind of 'apple crate' super class, for which you make an apple, but only add it to the crate if it wouldn't excced the maximum weight/number of apples already in the 'crate'.

## 