import requests
import json

for i in range(1, 6):
    result = requests.get(f"https://jsonplaceholder.typicode.com/posts/{i}")
    posts = json.loads(result.content)
    print(f"{posts['title']}\n{posts['body']}\n")
