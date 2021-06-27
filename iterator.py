import random

def f(tick =1):
    x = random.randint(1,3)
    if x == 3:
        print("ticking")
        return
    else:
        print("no tick")
        tick -=1
        if tick == 0:
            return
        f(tick)
