class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def start(self):
        print(self.year, self.make, self.model, "is starting.")
    
    def stop(self):
        print(self.year, self.make, self.model, "is stopping.")
        
    def honk(self):
        print(self.year, self.make, self.model, "is honking.")
        
    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        
        
my_car = Car("Subaru", "Outback", 2007, "White")

