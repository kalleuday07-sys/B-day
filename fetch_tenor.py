import os
import requests
import time

def fetch_tenor(query, filename):
    url = f"https://g.tenor.com/v1/search?q={query}&key=LIVDSRZULELA&limit=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                media_url = data['results'][0]['media'][0]['gif']['url']
                print(f"Downloading {media_url} for {query}")
                img_data = requests.get(media_url).content
                with open(filename, 'wb') as f:
                    f.write(img_data)
                print(f"Saved {filename}")
            else:
                print(f"No results for {query}")
        else:
            print(f"Error {response.status_code} for {query}")
    except Exception as e:
        print(f"Failed {e}")

images = [
    ("shinchan excited", "media/shinchan-excited.gif"),
    ("shinchan happy", "media/shinchan-happy.gif"),
    ("shinchan angry", "media/shinchan-angry.gif"),
    ("shinchan cute", "media/shinchan-cute.gif"),
    ("cute gift box bounce", "media/gift-box.png"),
    ("birthday cake bounce transparent", "media/cake-graphic.png")
]

if not os.path.exists("media"):
    os.makedirs("media")

for q, f in images:
    fetch_tenor(q, f)
    time.sleep(0.5)
