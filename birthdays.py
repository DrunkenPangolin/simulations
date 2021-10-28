import random

def birthday(num=23):
    dates = []
    for i in range(num):
        day = random.randint(1,(365.25*4))
        if day == 1461:
            bday = 366
        else:
            bday = day%365
        dates.append(bday)
        if dates.count(bday) > 1:
            return True
    return False

def sim(runs,num=23):
    total = []
    for i in range(runs):
        if (i)%round(runs/10) == 0:
            print(f'running simulation {round(i/runs*100)}% complete')
        total.append(birthday(num))
    return sum(total)/runs

print(sim(1000000))