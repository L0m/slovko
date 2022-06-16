import json
import random

words = json.load(open('slovko.txt', 'r'))

GREY = [[], [], [], [], []]
YELLOW = [[], [], [], [], []]
GREEN = ['', '', '', '', '']

def FILTER(words, grey, yellow, green):
    grey_filtered = []
    for word in words:
        valid = True
        for i, c in enumerate(word):
            if c in grey[i]:
                valid = False
        if valid:
            grey_filtered.append(word)
    green_filtered = []
    for word in grey_filtered:
        valid = True
        for i, c in enumerate(word):
            if green[i] and green[i] != c:
                valid = False
        if valid:
            green_filtered.append(word)
    yellow_filtered = []
    for word in green_filtered:
        valid = True
        for i, cc in enumerate(yellow):
            for c in cc:
                if c not in word[:i]+word[i+1:]:
                    valid = False
                if word[i] == c:
                    valid = False
        if valid:
            yellow_filtered.append(word)
    return yellow_filtered


while words:
    print(f"Current {len(words)} words.")
    guess = random.choice(words)  # TODO: Should I do main algo here?
    print(f"Suggest: {guess}")
    if len(words) <= 200:
        print(words)
    guess = input("Results:").split()
    if not guess:
        continue
    grey, yellow, green = guess
    for i, g in enumerate(grey):
        if g.isalpha():
            if (yellow+green).count(g):
                GREY[i].append(g)
            else:
                for j in range(5):
                    GREY[j].append(g)
    for i, y in enumerate(yellow):
        if y.isalpha():
            YELLOW[i].append(y)
    for i, g in enumerate(green):
        if g.isalpha():
            GREEN[i] = g
    words = FILTER(words, GREY, YELLOW, GREEN)
