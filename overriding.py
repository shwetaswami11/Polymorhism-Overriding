# 1. Animal sound
class Animal:
    def sound (self):
        print("animal makes a sound")
class Cat(Animal):
    def sound(self):
        print("Cat says:Meow") 
c=Cat()
c.sound()

# 2.Vehicle Fuel 
class Vehicle:
    def fuel(self):
        print("Uses petrol or diesel")
class ElectricCar(Vehicle):
    def fuel(self):
        print("Uses electric battery")
e = ElectricCar()
e.fuel()  

# 3.Greeting
class Parent:
    def greet(self):
        print("Welcome from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Welcome from Child")
c = Child()
c.greet()

# 4. Bank interest rate
class Bank:
    def rate_of_interest(self):
        return 5.0
class HDFC(Bank):
    def rate_of_interest(self):
        return 7.5
h = HDFC()
print("Interest Rate:", h.rate_of_interest()) 

# 5 Employee
class Employee:
    def __init__(self, name):
        self.name = name
class Manager(Employee):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept
m = Manager("Rohan", "HR")
print(m.name, "-", m.dept)  

# 6 Shape area
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return 4 * 4
s = Square()
print("Square Area:", s.area())

# 7 Bird Flying 
class Bird:
    def fly(self):
        print("Bird can fly high")
class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")
o = Ostrich()
o.fly() 

# 8. House
class Grandparent:
    def house(self):
        print("Old Village House")
class Parent(Grandparent):
    def house(self):
        print("City Apartment")
class Child(Parent):
    def house(self):
        print("Modern Villa")
c = Child()
c.house()  

# 9 
class Base:
    def display(self):
        print("Base display")
class Derived(Base):
    def display(self):
        Base.display(self)
        print("Derived display")
d = Derived()
d.display()

# 10 . Employee Bonus Calculation
class Staff:
    def bonus(self):
        return 2000
class Developer(Staff):
    def bonus(self):
        return super().bonus() + 5000
dev = Developer()
print("Total Bonus:", dev.bonus()) 

# 11.Mobile phone Camera
class BasicPhone:
    def camera(self):
        print("2 MP Camera")
class SmartPhone(BasicPhone):
    def camera(self):
        print("50 MP AI Camera")
sp = SmartPhone()
sp.camera()  

# 12 srt overriding
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Student Name: {self.name}"
s = Student("Ananya")
print(s)  

# 13 Restaurant Discount 
class Restaurant:
    def discount(self):
        print("Discount: 5%")
class PremiumMember(Restaurant):
    def discount(self):
        print("Discount: 20%")
p = PremiumMember()
p.discount()  

# 14 Class Attribute Overriding
class Course:
    duration = "3 Months"
class PythonCourse(Course):
    duration = "6 Weeks"
pc = PythonCourse()
print("Course Duration:", pc.duration) 

# 15 Game Character
class Character:
    def attack(self):
        print("Basic punch")
class Warrior(Character):
    def attack(self):
        print("Sword slash!")
w = Warrior()
w.attack() 

# 16 with argument
class Worker:
    def calculate_pay(self, hours):
        return hours * 100
class Engineer(Worker):
    def calculate_pay(self, hours):
        return hours * 250
eng = Engineer()
print("Pay:", eng.calculate_pay(8))

# 17 Notification
class Notification:
    def send(self):
        print("Sending general alert")
class EmailNotification(Notification):
    def send(self):
        print("Sending Email alert")
en = EmailNotification()
en.send() 

# 18 school 
class School:
    @classmethod
    def info(cls):
        print("General School")
class HighSchool(School):
    @classmethod
    def info(cls):
        print("High School (Grades 9-12)")
HighSchool.info()  

# 19 Helper
class MathHelper:
    @staticmethod
    def message():
        print("Standard Math Helper")
class AdvancedMath(MathHelper):
    @staticmethod
    def message():
        print("Advanced Calculus Helper")
AdvancedMath.message()

# 20 payment
class Payment:
    def status(self):
        print("Payment pending")
class CashPayment(Payment):
    def status(self):
        print("Paid in Cash")
class OnlinePayment(Payment):
    def status(self):
        print("Paid Online")
CashPayment().status()    
OnlinePayment().status()  

# Method overloading 
# 1 addition
class Addition:
    def add(self, *nums):
        return sum(nums)

obj = Addition()
print(obj.add(10, 20))         
print(obj.add(10, 20, 30, 40))  

# 2 Multiplying
class Math:
    def multiply(self, *nums):
        ans = 1
        for n in nums:
            ans = ans * n
        return ans
m = Math()
print(m.multiply(2, 3))        
print(m.multiply(2, 3, 4, 5))

