import pandas as pd
import heapq

class Process:
    def __init__ (self, pid, at, bt, ft=0):
        self.pid = pid
        self.at = at 
        self.bt = bt 
        self.ft = ft
n = int(input('Enter the number of processes: '))

p = [i for i in range(n)]
queue = []

for i in range (n):
    at = int(input(f'Enter Arrival Time for P{i}: '))
    bt = int(input(f'Enter Burst Time for P{i}: '))    
    queue.enqueue(Process(i, at, bt))

save_queue = queue.queue.copy()


def scan_queue (t, q):            
    valid = filter(lambda x: (x.at <= t) and (x.bt != 0), q)
    if len(valid) == 1:
        return valid[0].pid
    else:
        srt = filter(lambda x, y: min(x.bt, y.bt) and (x.bt != 0) and (y.bt != 0), q)
        return srt[0].pid

def update_bt (q, pid):
    for i in range (len(q)):
        if pid == q[i].pid:
            q[i].bt -= 1
            return q

def update_queue (q, ft, t):
    for i in range (len(q)):
        if q[i].bt == 0:
            f = q.pop(i)
            f[i].ft = t
            ft.append(f)
            return q, ft

t = 0
ft = []
while queue:
    p = scan_queue(queue, t)
    queue = update_bt(queue, p)
    queue, ft = update_queue(queue, ft, t)
    t += 1