import textdistance as td
import random


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = len(guess) - td.hamming(guess, secret)
    cows = int(td.sorensen_dice(guess, secret) * len(guess))
    return bulls, cows


def gameplay(ask: callable, inform: callable, words) -> int:
    random.seed()
    attempts = 0
    secret = random.choice(words)
    bulls = 0
    while bulls < len(secret):
        guess = ask("Введите слово: ", words)
        attempts += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
    return attempts


def ask(prompt: str, valid = None) -> str:
    answer = input(prompt)
    if valid is not None:
        while answer not in valid:
            answer = input(prompt)
    return answer


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
