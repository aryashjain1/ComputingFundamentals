import random

def tortoise_prob(pos):
    prob = random.randint(1, 20)
    if prob <= 8:
        pos += 3
    elif prob <= 10 and pos >= 6:
        pos += -6
    elif prob <= 10 and pos < 6:
        pos = 0
    else:
        pos += 1
    return pos

def hare_prob(pos):
    prob = random.randint(1, 20)
    if prob <= 2:
        pos += 0
    elif prob <= 8:
        pos += 9
    elif prob <= 10 and pos >= 12:
        pos += -12
    elif prob <= 10 and pos < 12:
        pos = 0
    elif prob <= 14:
        pos += 1
    elif prob <= 20 and pos >= 2:
        pos += -2
    else:
        pos = 0
    return pos

track = ["-"] * 95
tortoise, hare = 1,1
tortoise_wins, hare_wins = 0,0
print("BANG! AND THEY'RE OFF!!!!!")
tortoise = tortoise_prob(tortoise)
hare = hare_prob(hare)
for _ in range(50):
    tortoise, hare = 1,1
    while (tortoise < 95 or hare < 95):
        if tortoise != hare:
            track[tortoise - 1] = ('T')
            track[hare - 1] = ('H')
        else:
            track[tortoise - 1] = ('OUCH!!!')
        print(track)
        track[tortoise-1] = ('-')
        track[hare-1] = ('-')
        tortoise = tortoise_prob(tortoise)
        hare = hare_prob(hare)
        if tortoise >= 95:
            print("TORTOISE WINS!!! YAY!!!”")
            tortoise_wins += 1
            break
        if hare >= 95:
            print("HARE WINS. YUCH!")
            hare_wins += 1
            break

print(f'Tortoise wins:\t\t{tortoise_wins}')
print(f'Hare wins:\t\t{hare_wins}')