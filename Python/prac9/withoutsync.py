from threading import Thread
import time

class GreetingThread(Thread):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def run(self):
        for i in range(3):
            print("Hi", self.name)
            time.sleep(2)
        print("Your age is", self.age)

# Creating instances of the Greeting Thread class
t1 = GreetingThread("Nancy", 19)
t2 = GreetingThread("Nikki", 12)

# Starting the threads
t1.start()
t2.start()

# Waiting for the threads to complete
t1.join()
t2.join()

print("Complete")
