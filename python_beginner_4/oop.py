class Dog:

    def __init__(self, name, age):
        self.kontostand = 0
        self.age = age
        self.name = name

    def sit(self):
        print(self.name + " is now sitting.")

    def roll_over(self):
        print(self.name + " rolled over!")
    
    def set_age(self, new_age):
        self.age = new_age
        self.kontostand += 10
        self.roll_over()
    
    def print_info(self):
        print(str(self.age))
        print(self.name)
        
cooper = Dog("cooper", 5)
cooper.roll_over()
cooper.sit()
cooper.set_age(6)
cooper.kontostand += 1000
cooper.print_info()