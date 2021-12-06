from random import randint
from typing import List

from RR import RR


class App:
    def __init__(self):
        self.queues: List[RR] = []
        for i in range(4):
            self.queues.append(
                RR(i + 1, randint(1, 7))
            )

        self.sortedQueue = sorted(
            self.queues, key=lambda a: a.priority, reverse=True
        )
        self.current_queue = 0

    def run(self):
        while True:
            if self.sortedQueue[self.current_queue].ended:
                self.current_queue = (self.current_queue + 1) % len(self.sortedQueue)
            else:
                self.sortedQueue[self.current_queue].process_Queue()
                self.sortedQueue[self.current_queue].printQueue()

            
            if(sum([len(process.processQueue) for process in self.sortedQueue]) == 0):
                break
            
            

App().run()