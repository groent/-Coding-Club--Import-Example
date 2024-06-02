from alt import greeting as welcome
import random, os, time, datetime

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