from random import sample
import random
from typing import List

from pcb import PCB


class RR:
    def __init__(self, 
        line_numb: int, 
        process_numb: int
        ):

        self.numbers = sample(range(0,50), process_numb)
        self.numb: int = line_numb
        self.processQueue: List[PCB] = [
            PCB(self.numbers.pop(), random.randint(3,9))
            for _ in range(process_numb)
        ]
        self.quantum = random.randint(1,7)
        self.priority: int = random.randint(1,10)
        self.ended: bool = False
        self.currentProcess: int = 0

    def printQueue(self):
        for process in self.processQueue:
            print(process)

    def process_Queue(self)-> str:
        if len(self.processQueue) == 0:
            self.ended = True
            return

        self.processQueue[self.currentProcess].processing(self.quantum)

        if self.processQueue[self.currentProcess].ended:
            print(len(self.processQueue))
            self.processQueue.pop(self.currentProcess)

            if self.currentProcess == len(self.processQueue) and len(self.processQueue) != 0:
                self.currentProcess = 0
            return

        if self.currentProcess == len(self.processQueue) and len(self.processQueue) != 0:
            self.currentProcess = (self.currentProcess + 1) % len(self.processQueue)
            return

        self.currentProcess = (self.currentProcess + 1) % len(self.processQueue)