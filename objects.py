# Initialize Objects
class vehicle: 
    #Possible parameters that can be filled for the object
    brand = None
    year = None
    type = None
    #Determines what parameters must be set to create the object
    def __init__(self, brand, year, type):
        self.brand = brand
        self.year = year
        self.type = type

class plane(vehicle):
    turbine = None
    def __init__(self, brand, year, turbine):
        self.brand = brand
        self.year = year
        self.type = "Aircraft"
        self.turbine = turbine


#Create two different cars
sport_car = vehicle("Porsche", "1978", "car")
hatchback = vehicle("Audi", "1995", "car")
queen_of_the_skies = plane("Boeing", "1966", "Pratt & Whitney JT9D")

#print(hatchback.brand)
#print(sport_car.brand)