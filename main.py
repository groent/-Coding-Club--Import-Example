from alt import greeting as welcome
import random, os, time, datetime
import objects

date = datetime.datetime.now()


name = input("What's your name?\n> ")
welcome(name)
print(f"Today is {date.strftime('%A')} of week {date.strftime('%W')} ")

userInp = input("What range would you like? (start;end)\n> ")
range = userInp.split(";")
start = int(range[0])
end = int(range[1])


num = random.randint(start, end)

print(f"Your number is {num}")

os.mkdir(f"{num}")

files = os.listdir()
print(files)

time.sleep(5)

os.system("cls")

print("=== Dealership ===\nAquire a vehicle in record time!\n")
print("Recent Sale History:\n-------------------\n")
print(f"Type: {objects.hatchback.type}\nBrand:{objects.hatchback.brand}\nYear: {objects.hatchback.year}")
print(f"\nType: {objects.sport_car.type}\nBrand:{objects.sport_car.brand}\nYear: {objects.sport_car.year}")
print(f"\nType: {objects.queen_of_the_skies.type}\nBrand:{objects.queen_of_the_skies.brand}\nYear: {objects.queen_of_the_skies.year}")


query = input("Would you like a plane or a car?\n> ")
if query.lower() == "car":
    brand = input("What brand do you want?\n> ")
    year = input("What year do you want?\n> ")

    output = objects.vehicle(brand,year,"car")
    print(f"\nCongratulations! You are now a proud owner of a {output.year}, {output.brand}, {output.type}")
elif query.lower() == "plane":
    brand = input("What manufacturer do you want?\n> ")
    year = input("What year do you want?\n> ")
    engine = input("What engine do you want?\n> ")

    output = objects.plane(brand,year,engine)
    print(f"\nCongratulations! You are now a proud owner of a {output.year}, {output.brand}, {output.type}. Powered by a {output.turbine}")

else: 
    print("Enter a valid vehicle")



