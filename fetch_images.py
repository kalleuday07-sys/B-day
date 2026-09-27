import os
import requests
from duckduckgo_search import DDGS
import time

def download_image(query, filename, img_type="gif"):
    print(f"Searching for {query}...")
    try:
        with DDGS() as ddgs:
            results = ddgs.images(
                keywords=query,
                safesearch="off",
                type_image=img_type,
                max_results=3
            )
            results = list(results)
            for res in results:
                image_url = res['image']
                print(f"Found image: {image_url}")
                try:
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        with open(filename, 'wb') as f:
                            f.write(response.content)
                        print(f"Saved {filename}")
                        return
                except:
                    continue
            print(f"Failed to download {filename}")
    except Exception as e:
        print(f"Error: {e}")

images = [
    ("shinchan excited gif tenor", "media/shinchan-excited.gif", "gif"),
    ("shinchan happy gif tenor", "media/shinchan-happy.gif", "gif"),
    ("shinchan angry gif tenor", "media/shinchan-angry.gif", "gif"),
    ("shinchan cute gif tenor", "media/shinchan-cute.gif", "gif"),
    ("cute red gift box icon transparent png", "media/gift-box.png", "transparent"),
    ("birthday cake vector graphic transparent png", "media/cake-graphic.png", "transparent")
]

if not os.path.exists("media"):
    os.makedirs("media")

for q, f, t in images:
    download_image(q, f, t)
    time.sleep(1)
