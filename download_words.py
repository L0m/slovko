import requests
import json
import bs4


result = []


for letter in range(1, 34):
    start_page = 1
    while True:
        url = f"https://slovnyk.ua/index.php?s1={letter}&s2={start_page}"
        print(f"Processing {url}...")

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)

        words = soup.find_all("p", {"class": "cont_p"})

        if not words:
            print(f"Done, totals:{len(result)}")
            break

        for word in words:
            content = word.find('a').text
            result.append(content)

        start_page += 1

json.dump(result, open('words.txt', 'w'))