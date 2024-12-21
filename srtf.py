import pandas as pd
import heapq

class Process:
    def __init__ (self, at, bt):
        self.at = at 
        self.bt = bt 
    
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        heapq.heappush(self.queue, (x.bt, x))

    def dequeue(self):        
        return heapq.heappop(self.queue)[1]    
    
    def is_empty(self):
        return len(self.queue) == 0
    
n = int(input('Enter the number of processes: '))

p = [i for i in range(n)]
queue = PriorityQueue()

for i in range (n):
    at = int(input(f'Enter Arrival Time for P{i}: '))
    bt = int(input(f'Enter Burst Time for P{i}: '))    
    queue.enqueue(Process(at, bt))

save_queue = queue.queue.copy()

t = 0
ft = []

for i in range (n):
    p = queue.dequeue()
    while p.bt != 0:
        t += 1
        p.bt -= 1
        srt = queue.dequeue()
        if srt.bt < p.bt:
            queue.enqueue(p)            
            break
        else:
            queue.enqueue(srt)
    ft.append(t)
       