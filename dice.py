import pandas as pd
import matplotlib.pyplot as plt
import random

def dice(num):
    total = 0
    for i in range(num):
        total += random.randint(1,6)
    return total

def sim(runs,num=1):
    print(f'Running {runs} simulations')
    rolls = []
    total = 0
    for i in range(runs):
        roll = dice(num)
        total += roll
        if (i)%round(runs/10) == 0:
            print(f'simulation {round(i/runs*100)}% complete')
        rolls.append(roll)
    outcome = {}
    for i in rolls:
        if i not in outcome:
            outcome[i] = rolls.count(i)/runs
    average = total/runs

    df = pd.DataFrame.from_dict(outcome,orient='index')
    df = df.sort_index()
    print(df)
    print(f'Average = {average}')
    graph(df)
    return

def graph(df):
    # define graph and add lines
    ax = df.plot()
    plt.show()
    return

if __name__ == '__main__':
    sim(10000000,2)