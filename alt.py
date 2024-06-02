import time
def greeting(name):
    greeting = f"Welcome {name}" 
    list = [i for i in greeting]
    for i in list:
        print(f"{i}")
        time.sleep(0.1)