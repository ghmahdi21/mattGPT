import json
import pandas as pd

data = []
cols = ['username', 'owner_id', 'id', 'timestamp', 'caption', "likes", "comments"]
file_name = 'data/posts.jsonl'

counter = 0

with open(file_name) as f:
    for line in f:
        counter += 1
        print(counter)

        doc = json.loads(line)
        id = doc['id']
        owner_id = doc['owner']['id']
        username = doc['owner']['username']
        timestamp = doc['taken_at_timestamp']
        likes = doc['edge_media_preview_like']['count']
        comments = 0
        if "edge_media_preview_comment" in doc:
            comments = doc['edge_media_preview_comment']['count']
        caption = ''
        if len(doc['edge_media_to_caption']['edges']):
            caption = doc['edge_media_to_caption']['edges'][0]['node']['text']

        lst = [username, owner_id, id, timestamp, caption, likes, comments]
        data.append(lst)

df = pd.DataFrame(data=data, columns=cols)
df.to_parquet("posts.parquet")
df.to_csv("posts.csv", index=False)
