import random
from datetime import datetime
import time


class PCB:
    def __init__(self, pid: int, quantum: int,):
        self.name = random.choice(firstName) + " " + random.choice(lastName)
        self.pid = pid
        self.priority = random.randint(1, 10)
        self.date = datetime.now()
        self.start = random.randint(1, 10) + self.priority
        self.end = self.start + self.pid

        self.time_left = quantum

        self.ended = False

    def __str__(self):
        return  f"\n{self.name} ({self.time_left}s)\n pid: {self.pid}\n priority: {self.priority} \n date: {self.date} \n start addres: {self.start}\n end addres: {self.end}"
        

    def processing(self, quantum):
        while True:
            if quantum != 0 and self.time_left != 0:
                time.sleep(1)
                quantum -= 1
                self.time_left -= 1

                if quantum == 0:
                    self.ended = True
                    break

                if self.time_left == 0:
                    break


firstName = [
    'LOL',
    'Valorant',
    'Steam',
    'Discord',
    'VSCode'
]

lastName = [
    'Service',
    'Host',
]
