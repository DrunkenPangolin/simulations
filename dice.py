import pandas as pd
import random

def dice(num):
    total = 0
    for i in range(num):
        total += random.randint(1,6)
    return total

def sim(runs,num=1):
    rolls = []
    for i in range(runs):
        if (i)%round(runs/10) == 0:
            print(f'running simulation {round(i/runs*100)}% complete')
        rolls.append(dice(num))
    outcome = {}
    for i in rolls:
        if i not in outcome:
            outcome[i] = rolls.count(i)/runs
    return outcome

df = pd.DataFrame.from_dict(sim(4688754,1),orient='index')
print(df.sort_values([0]))