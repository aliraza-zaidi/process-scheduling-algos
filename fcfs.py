import pandas as pd


n = int(input('Enter the number of processes: '))

p = [i for i in range(n)]
ats = []
bts = []
for i in range (n):
    at = int(input(f'Enter Arrival Time for P{i}: '))
    bt = int(input(f'Enter Burst Time for P{i}: '))    
    ats.append(at)
    bts.append(bt)
save_ats = ats.copy()
save_bts = bts.copy()
wt = []
ft = []
tat = []
t = 0
W = 0
for i in range (n):    
    at =  ats.pop(0)
    bt = bts.pop(0)
    if t < at:
        t += (at-t)
    w = t-at
    W += w    
    wt.append(w)
    if i==0:
        t = at
    t += bt 
    ft.append(t)
    tat.append(t-at)    


df = pd.DataFrame({
    'Process': p,
    'Arrival Time': save_ats,
    'Burst Time': save_bts,
    'Finish Time': ft,
    'Waiting Time': wt,
    'Turnaround Time': tat
})

print('\n',df)
print('\nTotal Running Time is: ', t)
print('Average Waiting Time is: ', W / n)