import random

def cointoss(num):
    heads = 0
    for i in range(num):
        heads += random.randint(0,1)
    return heads == num

def sim(runs,num=1):
    total = []
    for i in range(runs):
        if (i)%round(runs/10) == 0:
            print(f'running simulation {round(i/runs*100)}% complete')
        total.append(cointoss(num))
    return sum(total)/runs

#print(f'Chance of heads {sim(34599,2)}')

def aim(out,num=1):
    attempts = 0
    total = []
    while sum(total) != out:
        attempts += 1
        total.append(cointoss(num))
    return attempts

#print(sim(10,5))

def aimsim(runs,out,num=1):
    total = []
    for i in range(runs):
        if (i)%round(runs/10) == 0:
            print(f'running simulation {round(i/runs*100)}% complete')
        total.append(aim(out,num))
    return sum(total)/runs

print(aimsim(10000,10,5))