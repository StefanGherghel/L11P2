import random
from threading import Thread, Condition
import time
from queue import Queue

coada = Queue()


class Consumator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consumator(self):
        x = coada.get()
        print("Am consumat nr: "+str(x)+"\n")

    def run(self):
        while(True):
            self.consumator()


class Producator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def producator(self):
        x = random.randint(0,100)
        print("Pun "+str(x)+"in coada\n")
        coada.put(x)
        #time.sleep(1)

    def run(self):
        while(True):
            self.producator()


if __name__ == '__main__':
    producator = Producator()
    consumator = Consumator()
    consumator.start()
    producator.start()

    consumator.join()
    producator.join()
