import json

words = json.load(open('words.txt', 'r'))

json.dump([w for w in words if len(w)==5], open('slovko.txt', 'w'), ensure_ascii=False)