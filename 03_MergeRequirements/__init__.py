import textdistance as td

def bullscows(guess:str, secret:str) -> (int, int):
    bulls = len(guess) - td.hamming(guess, secret)
    cows = int(td.sorensen_dice(guess, secret) * len(guess))
    return (bulls, cows)

guess = input()
secret = input()
print(bullscows(guess, secret))
