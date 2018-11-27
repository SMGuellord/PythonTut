import threading


class Messenger(threading.Thread): #Inherit from Thread class
    def run(self):
        for _ in range(10): # _ means that we don't really care about the starting number we just want the loop to run a number of times
            print(threading.currentThread().getName()+"\n")


m = Messenger(name='Send out messages')
m1 = Messenger(name='Receive message')

m.start()
m1.start()