import random

def play_random(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 17
    in_drawer = list(range(100))
    sampler2 = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler2, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
        else:
            print("none")
    return pardoned / n * 100   # %

def play_optimal(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 100
    in_drawer = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

# New Code for
print('Go Getters !!!!!! Test for merge Error')

if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_random(n):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(n):4.4f}% of simulations")
