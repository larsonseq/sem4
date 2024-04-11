from threading import Thread, Lock
import time

class GreetingThread(Thread):
    def __init__(self, name, age, lock):
        super().__init__()
        self.name = name
        self.age = age
        self.lock = lock
    
    def run(self):
        for i in range(3):
            self.lock.acquire()
            try:
                print("Hi", self.name)
                time.sleep(2)
                print("Your age is", self.age)
            finally:
                self.lock.release()

# Create a lock object 
thread_lock = Lock()

# Create threads
t1 = GreetingThread("Nikki", 19, thread_lock)
t2 = GreetingThread("Nancy", 9, thread_lock)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
